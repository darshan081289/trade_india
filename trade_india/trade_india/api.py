import frappe
import requests
from frappe import _
from frappe.utils import now_datetime
from frappe.utils.background_jobs import enqueue
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password

@frappe.whitelist()
def fetch_trade_india_leads():
    """Fetches leads from Trade India API"""
    settings = frappe.get_single("Trade India Settings")
    
    if not settings.enabled:
        frappe.msgprint(_("Trade India Integration is disabled"))
        return
        
    if not settings.api_key:
        frappe.throw(_("API Key not configured in Trade India Settings"))
    
    frappe.msgprint(_("Started fetching leads from Trade India"))
    
    try:
        api_url = " https://www.tradeindia.com/utils/my_inquiry.html?userid=319805&profile_id=356907&key=de5f2c5589d2c94feba0a2d4aa03aaa7&from_date=2025-01-27&to_date=2025-01-27&limit=10&page_no=1"  # Replace with actual endpoint
        headers = {
            "Authorization": f"Bearer {settings.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        leads = response.json()
        frappe.log_error(f"Received {len(leads)} leads", "Trade India Debug")
        
        for lead_data in leads:
            create_lead(lead_data, settings)
            
        settings.last_sync = now_datetime()
        settings.save()
        
        frappe.msgprint(_(f"Successfully synced {len(leads)} leads from Trade India"))
        
    except Exception as e:
        frappe.log_error(f"Trade India API Error: {str(e)}", "Trade India Integration")
        frappe.throw(_("Failed to fetch leads from Trade India. Check Error Log for details."))