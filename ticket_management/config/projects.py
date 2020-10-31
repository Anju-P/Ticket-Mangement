# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
    	return [
		{
			"label": _("Projects"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Ticket",
					"description": _("Ticket master."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Ticket Action",
					#"route": "#List/TicketActions",
					"description": _("Ticket Action / task."),
					#"onboard": 1,
				},
				
            ]
		}
	] 