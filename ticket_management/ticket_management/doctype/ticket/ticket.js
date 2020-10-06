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
		if(frm.doc.ticket_owner!=user&& frm.doc.expected_start_date!=null &&frm.doc.expected_end_date!=null) {
			frappe.msgprint(__("Only Ticket Owner Allowed to Change Date"));
			validated = false;
			
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
	},
	expected_start_date:function(frm,cdt,cdn){
        var d =locals[cdt][cdn];
        if(d.expected_start_date && d.expected_end_date) {
            

			var from_date = Date.parse(d.expected_start_date);
			var to_date = Date.parse(d.expected_end_date);

			if(to_date < from_date){
				frappe.msgprint(__("Planned Start Date Should be Before Planned End Date"));
				frm.set_value('expected_start_date', '');
				return;
			}
		}
	},
	expected_end_date:function(frm,cdt,cdn){
        var d =locals[cdt][cdn];
        if(d.expected_start_date && d.expected_end_date) {
            

			var from_date = Date.parse(d.expected_start_date);
			var to_date = Date.parse(d.expected_end_date);

			if(to_date < from_date){
				frappe.msgprint(__("Planned End Date Should be After Planned Start Date"));
				frm.set_value('expected_end_date', '');
				return;
			}
		}
	},
	completion_date:function(frm,cdt,cdn){
        var d =locals[cdt][cdn];
        if(d.expected_start_date && d.completion_date) {
            

			var from_date = Date.parse(d.expected_start_date);
			var to_date = Date.parse(d.completion_date);

			if(to_date < from_date){
				frappe.msgprint(__("Actual Date Should be After Planned Start Date"));
				frm.set_value('completion_date', '');
				return;
			}
		}
	},
	validate:function(frm,cdt,cdn){	
		var d = locals[cdt][cdn];
	$.each(frm.doc.details || [], function(i, v) {
		var from_date = Date.parse(d.expected_start_date);
			var to_date = Date.parse(v.date);
			var date = Date.parse(d.completion_date);
		if((from_date >to_date)||(date<to_date)){
			frappe.msgprint(__("Start Date Should be Within the Ticket Planned Start Date and Planned End Date"));
			validated = false;
		}
	});
}
});
frappe.ui.form.on('Ticket Details', {
	status:function(frm,cdt,cdn){
		var d = locals[cdt][cdn];
	$.each(frm.doc.details || [], function(i, v) {
		var from_date = Date.parse(d.expected_start_date);
			var to_date = Date.parse(v.date);
			var date = Date.parse(d.completion_date);
		if((from_date >to_date)||(date<to_date)){
			frappe.msgprint(__("Start Date Should be Within the Ticket Planned Start Date and Planned End Date"));
			validated = false;
		}
	})
	var count=0
	var count1=0
	var entry_datetime=d.start_time
	var res = entry_datetime.split(":");
	var displayVal = res[0]+ ':' + res[1]
	var exit_datetime=d.end_time
	var end = exit_datetime.split(":");
	var End_val = end[0]+ ':' + end[1]
	$.each(frm.doc.details || [], function(i, v) {
		var entry_datetime=v.start_time
		var res1 = entry_datetime.split(":");
		var displayVal1 = res1[0]+ ':' + res1[1]
		var exit_datetime1=v.end_time
		var end1 = exit_datetime1.split(":");
		var End_val1 = end1[0]+ ':' + end1[1]
		var a=0;
		
		if((d.date==v.date)&&(displayVal==displayVal1)&&(End_val1==End_val))
		{
			count1++;
		}
		if((d.type_of_task==v.type_of_task)&&(d.date==v.date)&&(displayVal==displayVal1)&&(End_val1==End_val))
		{
			count++;
		}
		

	})
	if(count1>1)
	{
		frappe.msgprint(__("Can't Enter Different Activity on Same Duration"));
		validated = false;
		frappe.model.set_value(d.doctype, d.name,"type_of_task",'')
		frappe.model.set_value(d.doctype, d.name,"date",'')
		frappe.model.set_value(d.doctype, d.name,"start_time",'')
		frappe.model.set_value(d.doctype, d.name,"end_time",'')
		frappe.model.set_value(d.doctype, d.name,"status",'')
		
	}
	if(count>1)
	{
		frappe.msgprint(__("Activity alredy Entered"));
		validated = false;
		frappe.model.set_value(d.doctype, d.name,"type_of_task",'')
		frappe.model.set_value(d.doctype, d.name,"date",'')
		frappe.model.set_value(d.doctype, d.name,"start_time",'')
		frappe.model.set_value(d.doctype, d.name,"end_time",'')
		frappe.model.set_value(d.doctype, d.name,"status",'')
        //frm.doc.details.splice(frm.doc.details[details_idx], 1)
		//frm.refresh_field('details')
		
	}

	
},

type_of_task:function(frm,cdt,cdn){
	var d = locals[cdt][cdn];
$.each(frm.doc.details || [], function(i, v) {
	var from_date = Date.parse(d.expected_start_date);
		var to_date = Date.parse(v.date);
		var date = Date.parse(d.completion_date);
	if((from_date >to_date)||(date<to_date)){
		frappe.msgprint(__("Start Date Should be Within the Ticket Planned Start Date and Planned End Date"));
		validated = false;
	}
})
var count=0
var entry_datetime=d.start_time
var res = entry_datetime.split(":");
var displayVal = res[0]+ ':' + res[1]
var exit_datetime=d.end_time
var end = exit_datetime.split(":");
var End_val = end[0]+ ':' + end[1]
$.each(frm.doc.details || [], function(i, v) {
	var entry_datetime=v.start_time
	var res1 = entry_datetime.split(":");
	var displayVal1 = res1[0]+ ':' + res1[1]
	var exit_datetime1=v.end_time
	var end1 = exit_datetime1.split(":");
	var End_val1 = end1[0]+ ':' + end1[1]
	var a=0;
	if((d.date==v.date)&&(displayVal==displayVal1)&&(End_val1==End_val))
	{
		count++;
	}

})
if(count>1)
{
	frappe.msgprint(__("Cant Enter Two activities in same duration"));
	validated = false;
	frappe.model.set_value(d.doctype, d.name,"type_of_task",'')
	frappe.model.set_value(d.doctype, d.name,"date",'')
	frappe.model.set_value(d.doctype, d.name,"start_time",'')
	frappe.model.set_value(d.doctype, d.name,"end_time",'')
	frappe.model.set_value(d.doctype, d.name,"status",'')
	//frm.doc.details.splice(frm.doc.details[details_idx], 1)
	//frm.refresh_field('details')
	
}
}
});