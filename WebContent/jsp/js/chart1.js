$(function () {
	const chart = document.getElementById("myChart");
	Chart.defaults.global.maintainAspectRatio = false;
    var data = {
    	    labels: [ "Positive Reviews","Negative Reviews",],
    	    datasets: [
    	        {
    	            data: [80,20],
    	            backgroundColor: ["#73B836","#F46344"],
    	            hoverBackgroundColor: ["#73B836","#F46344"]
    	        }],
    	      options:{
				animation:{
						animationScale : true
				},
	}
    	};
    var ctx = document.getElementById("myChart").getContext('2d');
    var myPieChart = new Chart(ctx,{
        type: 'pie',
        data: data,
    });
});