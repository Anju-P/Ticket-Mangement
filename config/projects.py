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
					"name": "Ticket Actions",
					#"route": "#List/TicketActions",
					"description": _("Ticket Actions / task."),
					#"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Schedular Events",
					"description": _("Schedular Events"),
					"onboard": 1,
				}				
            ]
		}
	] 