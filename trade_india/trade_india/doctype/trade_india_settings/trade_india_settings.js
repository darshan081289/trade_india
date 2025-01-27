frappe.ui.form.on('Trade India Settings', {
    refresh: function (frm) {
        frm.add_custom_button(__('Sync Now'), function () {
            frappe.call({
                method: 'trade_india.trade_india.api.fetch_trade_india_leads',
                callback: function (r) {
                    frappe.show_alert({
                        message: __('Sync Started'),
                        indicator: 'green'
                    });
                }
            });
        });
    },

    validate: function (frm) {
        if (!frm.doc.api_key && frm.doc.enabled) {
            frappe.throw(__('API Key is required when integration is enabled'));
        }
    }
});