import frappe
import requests
from datetime import datetime
from frappe import _
from frappe.utils import now_datetime

def fetch_trade_india_leads():
    settings = frappe.get_single("Trade India Settings")
    
    if not settings.enabled:
        return
    
    if not settings.api_key:
        frappe.log_error("Trade India API key not configured", "Trade India Integration")
        return
        
    try:
        # Replace with actual Trade India API endpoint
        api_url = "https://api.tradeindia.com/leads"
        headers = {
            "Authorization": f"Bearer {settings.api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        leads = response.json()
        
        for lead_data in leads:
            create_lead(lead_data, settings)
            
        settings.last_sync = now_datetime()
        settings.save()
        
    except Exception as e:
        frappe.log_error(f"Trade India API Error: {str(e)}", "Trade India Integration")

def create_lead(lead_data, settings):
    try:
        # Check if lead already exists
        existing_lead = frappe.get_list(
            "Lead",
            filters={"trade_india_id": lead_data.get("id")},
            fields=["name"]
        )
        
        if existing_lead:
            return
            
        lead = frappe.get_doc({
            "doctype": "Lead",
            "lead_name": lead_data.get("name"),
            "email_id": lead_data.get("email"),
            "mobile_no": lead_data.get("phone"),
            "source": "Trade India",
            "trade_india_id": lead_data.get("id"),
            "company_name": lead_data.get("company"),
            "owner": settings.lead_owner
        })
        
        lead.insert(ignore_permissions=True)
        frappe.db.commit()
        
    except Exception as e:
        frappe.log_error(f"Lead Creation Error: {str(e)}", "Trade India Integration")

def process_lead(doc, method):
    """Hook for additional processing after lead creation"""
    pass