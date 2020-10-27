// Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket', {
	
	validate: function(frm) {
        if(frm.doc.status=='Completed' && (frm.doc.remarks=='' || frm.doc.remarks==null)) {
           msgprint('Please enter remarks before complete the ticket.');
           validated = false;
           //frm.set_df_property('remarks', 'reqd', frm.doc.status ? 1 : 0)
         
           
        }
        if(frm.doc.status=='Closed' && frm.doc.ticket_owner!=user) {
         msgprint('Only Ticket Owner can Close the Ticket');
         validated = false;
         
        }
	
		if(frm.doc.sales_order && frm.doc.remarks &&  frm.doc.status=='Closed' )
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.sales_order_add_comments_from_tickets",
			args: {
				so: frm.doc.sales_order,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.opportunity && frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.opportunity_add_comments_from_tickets",
			args: {
				opp: frm.doc.opportunity,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.quotation&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.quotation__add_comments_from_tickets",
			args: {
				quo: frm.doc.quotation,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.purchase_order&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.purchase_order_add_comments_from_tickets",
			args: {
				po: frm.doc.purchase_order,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.delivery_note&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.delivery_note_add_comments_from_tickets",
			args: {
				dn: frm.doc.delivery_note,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.stock_entry&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.stock_entry_add_comments_from_tickets",
			args: {
				se: frm.doc.stock_entry,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.lead&& frm.doc.remarks && frm.doc.remarks && frm.doc.status=='Closed' )
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.lead_add_comments_from_tickets",
			args: {
				le: frm.doc.lead,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }	
		if(frm.doc.material_request&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method:"ticket_management.ticket_management.doctype.ticket.ticket.material_request_add_comments_from_tickets",
			args: {
				mq: frm.doc.material_request,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.sales_invoice&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.sales_invoice_add_comments_from_tickets",
			args: {
				sl: frm.doc.sales_invoice,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
		if(frm.doc.purchase_receipt&& frm.doc.remarks && frm.doc.status=='Closed')
		{
		frappe.call({
			method:"ticket_management.ticket_management.doctype.ticket.ticket.purchase_receipt_add_comments_from_tickets",
			args: {
				pr: frm.doc.purchase_receipt,
				remarks: frm.doc.remarks,
			},
			callback: function(r){
				if(r.message){
				}
			}
		});	
	  }
	}

});
/*
frappe.ui.form.on('Ticket', {	
	validate: function(frm) {
		frappe.call({
			method: "ticket_management.ticket_management.doctype.ticket.ticket.create_ticket",
			args: {
				"user": frappe.session.user 
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("allocated_to", r.message)
				}
			}
		});
		
	}
})
*/