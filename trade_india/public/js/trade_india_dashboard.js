frappe.pages['trade-india-dashboard'] = {
    onload: function (wrapper) {
        frappe.ui.make_app_page({
            parent: wrapper,
            title: 'Trade India Dashboard',
            single_column: true
        });

        new TradeIndiaDashboard(wrapper);
    }
};

class TradeIndiaDashboard {
    constructor(wrapper) {
        this.page = wrapper.page;
        this.wrapper = $(wrapper);
        this.setup_page();
    }

    setup_page() {
        this.setup_stats();
        this.setup_filters();
        this.setup_charts();
    }

    setup_stats() {
        frappe.call({
            method: 'trade_india.trade_india.api.get_dashboard_stats',
            callback: (r) => {
                if (r.message) {
                    this.render_stats(r.message);
                }
            }
        });
    }

    setup_filters() {
        this.page.add_field({
            fieldname: 'date_range',
            label: 'Date Range',
            fieldtype: 'DateRange',
            default: [
                frappe.datetime.add_days(frappe.datetime.get_today(), -30),
                frappe.datetime.get_today()
            ],
            change: () => this.refresh_dashboard()
        });
    }

    setup_charts() {
        // Implementation for charts
    }

    render_stats(stats) {
        const stats_wrapper = $('<div class="trade-india-stats"></div>').appendTo(this.wrapper);

        Object.entries(stats).forEach(([key, value]) => {
            $(`
                <div class="trade-india-stat-card">
                    <div class="trade-india-stat-value">${value}</div>
                    <div class="trade-india-stat-label">${frappe.model.unscrub(key)}</div>
                </div>
            `).appendTo(stats_wrapper);
        });
    }

    refresh_dashboard() {
        this.setup_stats();
        this.setup_charts();
    }
}