import frappe

def execute():
    """Initial patch for Trade India integration"""
    if not frappe.db.exists('Custom Field', {'dt': 'Lead', 'fieldname': 'trade_india_id'}):
        frappe.get_doc({
            'doctype': 'Custom Field',
            'dt': 'Lead',
            'label': 'Trade India ID',
            'fieldname': 'trade_india_id',
            'fieldtype': 'Data',
            'insert_after': 'source',
            'unique': 1,
            'read_only': 1
        }).insert()