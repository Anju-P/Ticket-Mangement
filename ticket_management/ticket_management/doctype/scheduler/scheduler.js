// Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('scheduler', {
	validate: function(frm) {
		frm.clear_table("scheduler_details");
		frm.refresh_field("scheduler_details")
		//debugger;
		
			var  d=frm.add_child("scheduler_details");
			var x=new Date();
			//alert(x)
			var end =frm.doc.planned_end_date
			var date=frappe.datetime.add_days(x)
			frappe.model.set_value(d.doctype,d.name,"date", frappe.datetime.add_days(x));
			if(frm.doc.sunday==1)
			{
				alert("Sunday")
			}
			if(frm.doc.monday==1)
			{
				alert("monday")
			}
			if(frm.doc.tuesday==1)
			{
				alert("monday")
			}
	if(frm.doc.sunday==1||frm.doc.monday==1||frm.doc.tuesday==1)
	{
		if(frm.doc.sunday==1)
		{
			var sun;
			var result = [];
			var days = {sun:0,mon:1,tue:2,wed:3,thu:4,fri:5,sat:6};
			var day = sun;
			// Copy start date
			var current = date;
			// Shift to next of required days
			//if(frm.doc.sunday)
			current.setDate(current.getDate() + (day - current.getDay() + 7) % 7);
			// While less than end date, add dates to result array
			while (current < end) {
			  result.push(new Date(+current));
			  current.setDate(current.getDate() + 7);
			}
			alert(result)
		}
	}

	}
});
