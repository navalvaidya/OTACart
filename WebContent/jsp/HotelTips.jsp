<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- Bootstrap Core CSS -->
		<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<script src="https://code.jquery.com/jquery-3.2.1.js"></script>
		<title>Hotel Tips</title>
		<style>
			.chart01 {
  				position: absolute;
  				top: 50px;
  				left: 20px;
				}
				
			.container{
				position: absolute;
				top: 50px;
				left: 500px;
			}
		</style>
	</head>
<body>
			<nav class="navbar navbar-inverse navbar-fixed-top" >
				<div class="container-fluid">
					<div class="navbar-header">
       					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">                    
          					<span class="icon-bar"></span>
          					<span class="icon-bar"></span>
          					<span class="icon-bar"></span>
       					</button>
       
       
   						<a class="navbar-brand page-scroll" href="/OTACart1/jsp/index.jsp">Revnomix</a>
   					</div>
    				<div class="collapse navbar-collapse" id="myNavbar">
      					<ul class="nav navbar-nav">
        					<li><a href="/OTACart/jsp/index.jsp">Price</a></li>
        					<li><a href="/OTACart/jsp/ReviewSearchPage.jsp">Reviews</a></li>
        					
        			    </ul>
    				</div>
    			</div>
 			</nav>
	<div class="chart01"><canvas id="myChart" height="350" width="350"></canvas></div>
	
	<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
	<script src="js/chart1.js"></script>
	
	<div class="container">
			<h3>Reviews</h3>
	</div>
  	
	
</body>
</html>