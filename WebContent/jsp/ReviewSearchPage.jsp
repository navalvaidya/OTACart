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
		<title>Search Reviews</title>

	</head>
	<style>
		.searchInput{
			position :absolute;
			top :200px;
		}
		
		.chart01 {
  			position: absolute;
  			top: 50px;
  			left: 20px;
		}
				
		.container{
			position: absolute;
			top: 50px;
			left: 400px;
		}
	</style>
	<body>

 			<nav class="navbar navbar-inverse navbar-fixed-top" >
				<div class="container-fluid">
					<div class="navbar-header">
       					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">                    
          					<span class="icon-bar"></span>
          					<span class="icon-bar"></span>
          					<span class="icon-bar"></span>
       					</button>
       
       
   						<a class="navbar-brand page-scroll" href="/OTACart/jsp/index.jsp">Revnomix</a>
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
			
			
			<div class="container" id="container">
				<h2>Reviews</h2>
				<h4>Showing top 20 Reviews</h4>
				<div id="displayname"></div>
				<div id="reviewBox"></div>
			</div>
	 			<div class="searchInput" id="searchInput">
	 				<div class="row"><div class="col-sm-12 col-sm-offset-10"><h2>Searching And Analysis of Reviews</h2></div></div>
					<form action="/OTACart/ProcessReview" id="reviewForm" name="reviewForm" class="ajax" method="GET" enctype="text/plain">
						<div class="form-group">
							<div class="row">
								<div class="col-sm-10 col-sm-offset-10">
									<label for="reviewSearch">Search Hotel</label>
									<input type="text" placeholder="Hotel Name" id="reviewSearch" name="reviewSearch" class="form-control input-md">
									<button type="submit" class="btn btn-default">Search</button>
								</div>
							</div>
						</div>
					</form>
				</div>
			
			
			<script src="js/review.js"></script>
</body>
</html>