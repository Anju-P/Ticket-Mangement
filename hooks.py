# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ticket_management"
app_title = "Ticket Management"
app_publisher = "Momscode Technologies Pvt.Ltd"
app_description = "to identify,record,manage,resolve tasks"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@momscode.in"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ticket_management/css/ticket_management.css"
# app_include_js = "/assets/ticket_management/js/ticket_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/ticket_management/css/ticket_management.css"
# web_include_js = "/assets/ticket_management/js/ticket_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ticket_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ticket_management.install.before_install"
# after_install = "ticket_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ticket_management.notifications.get_notification_config"
notification_config = "ticket_management.ticket_management.notifications.get_notification_config"
# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#permission_query_conditions = {
   # "Ticket": "ticket_management.ticket_management.doctype.ticket.ticket.get_permission_query_conditions",
#}
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
doctype_js = {
    "Quotation":"public/js/quotation.js",
    "Sales Order":"public/js/sales_order.js",
    "Purchase Invoice":"public/js/purchase_invoice.js",
    "Delivery Note":"public/js/delivery_note.js",
    "Expense Claim":"public/js/expense_claim.js",
    "Journal Entry":"public/js/journal_entry.js",
    "Lead":"public/js/lead.js",
    "Material Request":"public/js/material_request.js",
    "Payment Entry":"public/js/payment_entry.js",
    "Production Plan":"public/js/production_plan.js",
    "Sales Invoice":"public/js/sales_invoice.js",
    "Purchase Order":"public/js/purchase_order.js",
    "Purchase Receipt":"public/js/purchase_receipt.js",
    "Stock Entry":"public/js/stock_entry.js",
    "Ticket Details":"public/js/ticket_details.js",
    "Opportunity":"public/js/opportunity.js",
    }
doc_events = {
 	"Schedular Events": {
 		"on_submit": "ticket_management.ticket_management.doctype.schedular_events.schedular_events.on_schedular_events_on_submit"
# 		"on_cancel": "method",
# 		"on_trash": "method"
	}
 }

# Scheduled Tasks
# ---------------

scheduler_events = {
 	"all": [
		"ticket_management.ticket_management.doctype.schedular_events.schedular_events.on_schedular_events_on_submit"
 	]
# 	"daily": [
# 		"ticket_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"ticket_management.ticket_management.doctype.schedular_events.schedular_events.on_schedular_events_on_submit"
# 	]
# 	"weekly": [
# 		"ticket_management.ticket_management.doctype.ticket.ticket.create_ticket"
# 	],
# 	"monthly": [
# 		"ticket_management.doctype.ticket.ticket.create_ticket"
# 	]
}

# Testing
# -------

# before_tests = "ticket_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ticket_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ticket_management.task.get_dashboard_data"
# }
fixtures = ["Custom Field"]


