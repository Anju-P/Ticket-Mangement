frappe.ui.form.on('Ticket Details', {
	refresh:function(frm)
	{
		
	}
	/*end_time: function(frm, cdt, cdn) {
			var d = locals[cdt][cdn];
			var hours=0
			var minutes=0
			var seconds=0
            var total=0
            alert("hai");
			if(d.start_time && d.end_time)
         	{
		      var startTime=moment(d.start_time, "HH:mm:ss");
		      var endTime=moment(d.end_time, "HH:mm:ss");
		      var duration = moment.duration(endTime.diff(startTime));
	          hours = parseInt(duration.asHours());
		      minutes = parseInt(duration.asMinutes())%60;
		      seconds=parseInt(duration.asSeconds())%60;
		      //console.log(hours + ' hour and '+ minutes+' minutes.' +seconds+'second');
			}
			//frappe.model.set_value(cdt,cdn,"duration",d.end_time);
			 frappe.model.set_value(cdt,cdn,"duration",hours+":"+minutes+":"+seconds);
		//frm.refresh_field("duration");
 	}*/
})