# -*- coding: utf-8 -*-
# Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import date 
from frappe.utils import nowdate
from frappe import msgprint, _
from frappe.model.document import Document


class SchedularEvents(Document):
	pass

def on_schedular_events_on_submit(d,handler=""):
	schedular = frappe.db.sql("""select s.title,s.description,s.posting_date,s.status,s.owner,s.allocated_to,s.document_type,s.recurrence_pattern,e.date 
    from `tabSchedular Events` as s inner join `tabSchedular Event Date` as e where s.name=e.parent""", as_dict=1)
	for d in schedular:
		if d.document_type == 'Ticket':
			if d.recurrence_pattern == 'Daily':
				today = nowdate()
				frappe.msgprint(d.date)
				if d.date == today:
					frappe.msgprint('hi')
					ticket = frappe.new_doc('Ticket')
					ticket.title = d.title
					ticket.description = d.description
					ticket.posting_date = d.posting_date
					ticket.status = d.status
					ticket.owner = d.owner
					ticket.allocated_to = d.allocated_to
					ticket.document_type = d.document_type
					ticket.frequency = d.recurrence_pattern
					ticket.flags.ignore_permissions  = True
					ticket.update({
           				'title': ticket.title,
						'description': ticket.description,
						'posting_date': ticket.posting_date,
						'status': ticket.status,
						'owner': ticket.owner,
						'allocated_to': ticket.allocated_to,
						'document_type': ticket.document_type,
						'frequency': ticket.frequency          
        			}).insert()

	return

	
