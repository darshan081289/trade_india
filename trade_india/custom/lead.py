# Create a new file: trade_india/trade_india/custom/lead.py
import frappe

def create_custom_fields():
    custom_fields = {
        'Lead': [
            {
                'fieldname': 'trade_india_section',
                'label': 'Trade India Details',
                'fieldtype': 'Section Break',
                'insert_after': 'notes'
            },
            {
                'fieldname': 'trade_india_id',
                'label': 'Trade India ID',
                'fieldtype': 'Data',
                'unique': 1,
                'read_only': 1,
                'insert_after': 'trade_india_section'
            },
            {
                'fieldname': 'trade_india_data',
                'label': 'Trade India Data',
                'fieldtype': 'Code',
                'options': 'JSON',
                'read_only': 1,
                'insert_after': 'trade_india_id'
            }
        ]
    }
    
    create_custom_fields(custom_fields)