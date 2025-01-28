app_name = "trade_india"
app_title = "Trade India Integration"
app_publisher = "Your Company"
app_description = "Trade India Integration for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your.email@example.com"
app_license = "MIT"

# Scheduled Tasks
scheduler_events = {
    "daily": [
        "trade_india.trade_india.api.fetch_trade_india_leads"
    ]
}

# Document Events
doc_events = {
    "Lead": {
        "after_insert": "trade_india.trade_india.api.process_lead"
    }
}