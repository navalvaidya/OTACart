$("#searchForm").submit(function(e){
	var formObj = $(this),
		url = formObj.attr('action'),
		method = formObj.attr('method'),
		formData = formObj.serialize();
	
		$("#resultContainer").html("<p style='color:green' class='alert alert-success'>Waiting for results</p>");
		$("#resultContainer").delay(100).fadeIn(300);
	
		$.ajax({
		url:url,
		type:method,
		data:formData,
		success:function(response){
			
			
			var i;
			response=response.replace('[','').replace(']','')
			//.replace(/\(Same\)/g,'');
			
			var data = response.split(',')
			var container = "#priceData";
			for(i=0;i<data.length;i++){
				var cell = container.concat(i);
				var col = data[i].split(" ")
				var j=0;
				var str="a"
				var arr = [];
				console.log(col)
				for(j=0;j<col.length;j++){
					
						
						if(col[j].indexOf("(S)")>-1){
							str1 = "<font color='red'>"
							strN = col[j-1]
							str2 = col[j]
							console.log(str2)
							strN2 = str2.replace("(S)","")
							str3 = "</font><br>"
							str4= str1+""+strN+" "+strN2+""+str3;
							arr.push(str4)
							
						}
						
						if(col[j].indexOf("(N)")>-1){
							str1 = "<font color='blue'>"
							strN = col[j-1]
							str2 = col[j]
							strN2 = str2.replace("(N)","")
							str3 = "</font><br>"
							str4= str1+""+strN+" "+strN2+""+str3;
							arr.push(str4)
							
						}
	
				}
				$(cell).html(arr);
				console.log(str)
			}	
			$("#resultContainer").delay(1200).fadeOut(800);
		}
	});
	return false;
});