# -*- coding: utf-8 -*-
# Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc  
from frappe.model.document import Document
from frappe.model.document import get_doc
from frappe.model.document import Document

class Ticket(Document):
	pass
@frappe.whitelist()
def make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Sales Order", source_name, {
                "Sales Order": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "sales_order"

                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def purchase_invoice_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Purchase Invoice", source_name, {
                "Purchase Invoice": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "purchase_invoice"
                        }
                }
        }, target_doc)

        return doclist
@frappe.whitelist()
def make_opptickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Opportunity", source_name, {
                "Opportunity": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "opportunity"
                        }
                }
        }, target_doc)
        return doclist

@frappe.whitelist()
def make_quoopptickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Quotation", source_name, {
                "Quotation": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Quotation"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def make_stocktickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Stock Entry", source_name, {
                "Stock Entry": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Stock Entry"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def make_purchasetickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Purchase Order", source_name, {
                "Purchase Order": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Purchase Order"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def make_deliverytickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Delivery Note", source_name, {
                "Delivery Note": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Delivery Note"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def Lead_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Lead", source_name, {
                "Lead": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Lead"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def material_request_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Material Request", source_name, {
                "Material Request": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Material Request"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def sales_invoice_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Sales Invoice", source_name, {
                "Sales Invoice": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "Sales Invoice"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def journal_entry_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Journal Entry", source_name, {
                "Journal Entry": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "journal_entry"
                        }
                }
        }, target_doc)
        return doclist    
@frappe.whitelist()
def production_plan_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Production Plan", source_name, {
                "Production Plan": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "production_plan"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def purchase_receipt_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Purchase Receipt", source_name, {
                "Purchase Receipt": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "purchase_receipt"
                        }
                }
        }, target_doc)
        return doclist    
@frappe.whitelist()
def payroll_entry_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Payroll Entry", source_name, {
                "Payroll Entry": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "payroll_entry"
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def expense_claim_make_tickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Expense Claim", source_name, {
                "Expense Claim": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "expense_claim",
                                
                        }
                }
        }, target_doc)
        return doclist
@frappe.whitelist()
def payment_entry_make_tiickets(source_name, target_doc=None):
        doclist = get_mapped_doc("Payment Entry", source_name, {
                "Payment Entry": {
                        "doctype": "Ticket",
                        "field_map": {
                                "name": "payment_entry"
                        }
                }
        }, target_doc)
        return doclist

# add comments from tickets 0n 27-11-2019
@frappe.whitelist()
def opportunity_add_comments_from_tickets(opp,remarks):
	d = frappe.get_doc('Opportunity', opp)
	#to add a new comment
	d.add_comment('Comment',text=remarks)
	return d

@frappe.whitelist()
def sales_order_add_comments_from_tickets(so,remarks):
	d = frappe.get_doc('Sales Order', so)
	#to add a new comment
	d.add_comment('Comment',text=remarks)
	return d
@frappe.whitelist()
def quotation__add_comments_from_tickets(quo,remarks):
        d = frappe.get_doc('Quotation', quo)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def purchase_order_add_comments_from_tickets(po,remarks):
        d = frappe.get_doc('Purchase Order', po)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def delivery_note__add_comments_from_tickets(dn,remarks):
        d = frappe.get_doc('Delivery Note', dn)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def stock_entry__add_comments_from_tickets(se,remarks):
        d = frappe.get_doc('Stock Entry', se)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def lead_add_comments_from_tickets(le,remarks):
        d = frappe.get_doc('Lead', le)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d

@frappe.whitelist()
def material_request_add_comments_from_tickets(mq,remarks):
        d = frappe.get_doc('Material Request', mq)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def sales_invoice_add_comments_from_tickets(sl,remarks):
        d = frappe.get_doc('Sales Invoice', sl)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def productionplanadd_comments_from_tickets(pp,remarks):
        d = frappe.get_doc('Production Plan', pp)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def purchase_receipt_add_comments_from_tickets(pr,remarks):
        d = frappe.get_doc('Purchase Receipt', pr)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def purchaseinvoice_add_comments_from_tickets(pi,remarks):
        d = frappe.get_doc('Purchase Invoice', pi)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def journal_entry_add_comments_from_tickets(je,remarks):
        d = frappe.get_doc('Journal Entry', je)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def payment_entry_add_comments_from_tickets(pay,remarks):
        d = frappe.get_doc('Payment Entry', pay)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def payroll_entry_add_comments_from_tickets(pe,remarks):
        d = frappe.get_doc('Payroll Entry', pe)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
@frappe.whitelist()
def expense_claim_add_comments_from_tickets(ec,remarks):
        d = frappe.get_doc('Expense Claim', ec)
        #to add a new comment
        d.add_comment('Comment',text=remarks)
        return d
    