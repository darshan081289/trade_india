import frappe
from frappe.model.document import Document

class TradeIndiaSettings(Document):
    def validate(self):
        if self.enabled and not self.api_key:
            frappe.throw("API Key is required when integration is enabled")
            
    def on_update(self):
        frappe.cache().delete_key('trade_india_settings')