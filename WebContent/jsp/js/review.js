$(document).ready(function(){
	var review = document.getElementById("reviewBox");
	review.style.display = 'none';
	const chart = document.getElementById("myChart");
	Chart.defaults.global.maintainAspectRatio = false;

    var ctx = document.getElementById("myChart").getContext('2d');
    var myPieChart = new Chart(ctx,{type: 'pie'});
    myPieChart.destroy()
    
    var container = document.getElementById("container");
	container.style.display = 'none';

});

$("#reviewForm").submit(function(e){
	var formObj = $(this),
		url = formObj.attr('action'),
		method = formObj.attr('method'),
		formData = formObj.serialize();
		$.ajax({
		url:url,
		type:method,
		data:formData,
		success:function(response){
			
			var dat1 = []
			dat1 = response.split('(split)')
			var dat = JSON.parse(dat1[0]);
			var filtered = dat1[1].replace('reviews,,','');
			var reviewArr = filtered.split(',,')
		    var data = {
		    	    labels: [ "Positive Reviews","Negative Reviews",],
		    	    datasets: [
		    	        {
		    	            data: dat,
		    	            backgroundColor: ["#73B836","#F46344"],
		    	            hoverBackgroundColor: ["#73B836","#F46344"]
		    	        }],
		    	      options:{
						animation:{
								animationScale : true
						},
		    	      }
		    	};
			var element = document.getElementById("searchInput");
			element.style.display = 'none';
			
			var ctx = document.getElementById("myChart").getContext('2d');
			var myPieChart = new Chart(ctx,{type: 'pie',data: data});
			myPieChart.render();
		
			var container = document.getElementById("container");
			container.style.display = 'block';
			
			var review = document.getElementById("reviewBox");
			review.style.display = 'block';
		
			var hotelname = document.getElementById("displayname");
			review.style.display = 'block';
			
			$(hotelname).html('<h3>'+reviewArr[0]+'<h3>');
			console.log(reviewArr[0])
			
			var i;
			var arr = []
			for(i=1;i<20;i++){
				arr.push(reviewArr[i])
				arr.push('<br>')
				console.log(reviewArr[i]);
			}
			$(review).html(arr);
			
		}
	});
	return false;
});