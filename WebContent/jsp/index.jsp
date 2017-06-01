<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page import="org.joda.time.DateTime" %>   
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- Bootstrap Core CSS -->
		<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
		
		<title>Calendar</title>
		<style>
			.top-buffer { margin-top: 10px;}
			
			.col-sm-2{
				height:200px;
				border: 1px solid;
				border-color:gray;
				background-color: #ccccff;
			}
			
			@media (min-width: 768px){
 			  .seven-cols .col-md-1,
			  .seven-cols .col-sm-1,
			  .seven-cols .col-lg-1  {
			    width: 100%;
			    *width: 100%;
			  }
			}
			
			
			@media (min-width: 992px) {
			  .seven-cols .col-md-1,
			  .seven-cols .col-sm-1,
			  .seven-cols .col-lg-1 {
			    width: 14.285714285714285714285714285714%;
			    *width: 14.285714285714285714285714285714%;
			  }
			}
			
			
			@media (min-width: 1200px) {
			  .seven-cols .col-md-1,
			  .seven-cols .col-sm-1,
			  .seven-cols .col-lg-1 {
			    width: 14.285714285714285714285714285714%;
			    *width: 14.285714285714285714285714285714%;
			  }
			}
		</style>
	</head>
	<body>
		<div class="row"> 
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
		
		</div>
		
		<%
			DateTime date = new DateTime();
			//int date = 1;
			int id=0; 	
		%>
		<div class="jumbotron">
			
			<div class="row top top-buffer">
				<form name="searchForm" id="searchForm" action="/OTACart/Perhoteldata" class="ajax" method="GET" enctype="text/plain">
					<label for="hotelname" class="col col-xs-1"><span class="pull-right">Hotel Name</span></label>
					<div class="col col-xs-2"><span class="pull-right"><input type="text" id="hotelname" name="hotelname" placeholder="Enter Hotel Name" ></span></div>
					<div class="col col-xs-1"><span class="pull-left"><input type="submit" value="Search" class="btn btn-default" name="submitbtn" id="submitbtn"></span></div>
				</form>
				<div id="resultContainer"> </div>
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
				<script src="https://code.jquery.com/jquery-3.2.1.js"></script>
  				<script src="js/main.js"></script>
  		
				<h3>Price for Next 30 Days</h3>
			</div>
			
			<div class="container">
				<%for(int i=0;i<5;i++){ %>
					<div>
						<%for(int j=0;j<6;j++){ %>
						<div class="col-sm-2"><%=date.plusDays(id).getDayOfMonth()%>/<%=date.plusDays(id).getMonthOfYear()%>
							<div id="priceData<%=id%>"></div>
						</div>
						<%id++;}%>
					</div>
			<%} %>	
		</div>
		</div>
	</body>
</html>