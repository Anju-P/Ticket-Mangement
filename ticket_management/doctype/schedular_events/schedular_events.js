// Copyright (c) 2020, Momscode Technologies Pvt.Ltd and contributors
// For license information, please see license.txt


frappe.ui.form.on('Schedular Events', {
	validate:function(frm){
		if(frm.doc.document_type = 'Ticket'){
			if(frm.doc.recurrence_pattern = 'Daily'){
				frappe.call({
					method:"frappe.client.get",
					args: {
						'doctype':'Schedular Events',
						'filters':{
							'name': frm.doc.schedular_events,	
						}
												 
					},
					callback: function(r){
						if (!r.exc) {

							//alert(r.message.planned_start_date);
							//alert(r.message.planned_end_date); 
							var ps_date = r.message.planned_start_date;
							var pe_date = r.message.planned_end_date;
							var getDateArray = function(start, end) {
								var arr = new Array();
								var dt = new Date(start);
								end = new Date(end);
							  
								while (dt <= end) {
								  arr.push(new Date(dt));
								  dt.setDate(dt.getDate() + 1);
								  
								}
							  
								return arr;
							  
							}
						
							var dateArr = getDateArray(ps_date, pe_date);
							
							frm.clear_table("range_of_recurrence_section");
							frm.refresh_field("range_of_recurrence_section")
							debugger;
							for (var i = 0; i <dateArr.length; i++) {				
								var  d=frm.add_child("range_of_recurrence_section");
								var x=new Date(dateArr[i]);
								alert(x)
								//var date=dateArr[i].toJSON().slice(0,10);
								//var item=date.slice(8,10)+'-'+date.slice(5,7)+'-'+date.slice(0,4)
								//var date = parseInt(dateArr[i].toString().substring(0,10));
								//var item = date.toString().substring(8,10) + '-' +date.toString().substring(5,7) + '-'+date.toString().substring(0,4)
								frappe.model.set_value(d.doctype,d.name,"date",item)
								frm.refresh_field("range_of_recurrence_section")
								//item = frappe.utils.formatdate(item, 'dd-MM-YYYY')//new-----------
								//var date = parseInt(dateArr[i].toString().substring(0,10));
								//var item = date.toString().substring(8,10) + '-' +date.toString().substring(5,7) + '-'+date.toString().substring(0,4);
								//var x=new Date(dateArr[i]);
							}
							

							/*$.each(frm.doc.range_of_recurrence_section || [], function(i, v) {
								alert("hiiiii");
								frappe.model.set_value(v.doctype, v.name, "date", x)
							})
							frm.refresh_field('range_of_recurrence_section');
							}
								
							//for (var i = 0; i < dateArr.length; i++) {
							//var x = dateArr[i];
							//	alert("annuuuuuu");
							
							/*for (var i = 0; i < dateArr.length; i++) {
								document.write("<p>" + dateArr[i] + "</p>");
							}
							
							$.each(r.message.planned_start_date || [], function(i, v) {
								planned_start_date = v.planned_start_date +1
								p_dates.push(planned_start_date)
							})
							planned_start_date = planned_end_date;*/
							
						}
					}
				})
			}
		}	
	}
	
});

/*frappe.ui.form.on("Schedular Event Date", "Date", function(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
	child.date = dateArr[i];
	cur_frm.refresh_field("date");
});*/