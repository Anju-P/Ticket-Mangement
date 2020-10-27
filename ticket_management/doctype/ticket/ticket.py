# -*- coding: utf-8 -*-
# Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc  
from frappe.model.document import Document
from frappe.model.document import get_doc
from frappe.model.document import Document
from datetime import date 
#from dateutil.relativedelta import relativedelta
#from calendar import monthrange
#from frappe.utils import nowdate

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
 
        

#def create_ticket():
#        ticket_list = frappe.db.sql("""select s.title,s.description,s.posting_date,s.owner,s.recurrence_pattern,s.allocated_to,e.date, 
#        from `tabSchedular Events` as s inner join `tabSchedular Event Date` as e where s.name=e.parent""", as_dict=1)
#        for d in ticket_list:
#                ticket = frappe.new_doc('Ticket')
#                ticket.allocated_to = d.allocated_to
#                ticket.frequency = d.frequency
#                ticket.flags.ignore_permissions  = True
#                ticket.flags.ignore_mandatory = True
#                action_list = frappe.db.sql("""select d.type_of_task 
#                from `tabTicket` as t inner join `tabTicket Details` as d 
#                where t.name=d.parent and allocated_to='anu@gmail.com'""", as_dict=1)
#                for x in action_list:
#                        ticket.flags.ignore_permissions  = True
#                       ticket.flags.ignore_mandatory = True
#                        ticket.append('details', {
#                                'type_of_task': x.type_of_task
#                        })  
#                ticket.update({
#                        'allocated_to': ticket.allocated_to,
#                       'frequency': ticket.frequency,
#                        'details': ticket.details
#               }).insert()        
#              return  
#       return





#        return

#        ticket.frequency = 'Monthly'
#        today = date.today()
#        d = today - relativedelta(months = 2)
#        first_day = date(d.year,d.month,1)
#        ticket.start_date = first_day
#        ticket.end_date = first_day.replace(day = monthrange(first_day.year, first_day.month)[1])
#    
#        ticket.flags.ignore_permissions  = True
#        ticket.flags.ignore_mandatory = True
#        ticket.update({
#                'frequency': ticket.frequency,
#                'start_date': ticket.start_date,
#                'end_date': ticket.end_date
#        }).insert()




#        ticket_list = frappe.db.sql("""select name from tabTask where status='Open'""",as_dict = 1)
#        for ticket in ticket_list:
#                doc = frappe.get_doc('Ticket',ticket.get("name"))
#                doc.status = "Closed"
#                doc.flags.ignore_permissions = True
#                doc.flags.ignore_mandatory = True
#                doc.save()
        
#        frappe.msgprint(msg = 'Ticket has been created',
#                title = 'Notification',
#                indicator = 'green'
#        )
        


        
        
#def get_permission_query_conditions(user):
#        return "(tabTicket.ticket_owner='{user}'".format(user=frappe.session.user)