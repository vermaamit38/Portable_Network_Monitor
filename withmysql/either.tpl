<!DOCTYPE>
<html>
 <body bgcolor="#CEF6F5">
	<title>

	  Network Monitor

	</title>
<center>
	<head>
		 <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<div style="text-align: center;">
	  <style>
.jumbotron { 
    background-color: #66b3ff; /* Orange */
    color: #ffffff;
}
</style>
</div>

</head>
<body>
 <div class="container">
  	<div class="jumbotron text-center">
  	  <h1>Network Monitor</h1> 
    	<p>This is Network Monitor DashBoard directly fetching data from BeagleBoneBlack</p> 
  	</div>
  	<br>

	<div class="panel-group">
     <div class="panel panel-default">
       <div class="panel-heading">Show results with Database</div>
       <div class="panel-body">Please Click Here  <button type="button" class="btn btn-default btn-sm"onclick="myfunction()" >Click</button> </div>
     </div>

     <div class="panel panel-primary">
       <div class="panel-heading"> show results with java Code</div>
       <div class="panel-body">Please Click Here  <button type="button" class="btn btn-default btn-sm" onclick="myfunction1()" >Click</button></div>
     </div>

     

     <div class="panel panel-info">
       <div class="panel-heading">Show comaprison of time of execution</div>
       <div class="panel-body">Please Click Here  <button type="button" class="btn btn-default btn-sm" onclick="myfunction3()"  >Click</button></div>
     </div>

<div class="panel panel-success">
       <div class="panel-heading">Show old records</div>
       <div class="panel-body">Please Click Here  <button type="button" class="btn btn-default btn-sm" onclick="myfunction4()"  >Click</button></div>
     </div>

    
    </div>
<br>

 


	<script language="javascript">
	
        function myfunction()
	{     
		window.open("start.tpl");
	}
        function myfunction1()
	{     
		window.open("start_java.tpl");
	}
       
        function myfunction3()
	{     
		window.open("compare.tpl");
	}
function myfunction4()
	{     
		window.open("old.tpl");
	}
 
        </script>
 
		<footer style="clear: both;
    position: relative;
    z-index: 10;
    height: 3em;
    margin-top: -3em;"><hr>
			Dropouts Technologies LLP © 2015. All Rights Reserved.
		</hr></footer>
</div>
</body>
	</center>
</html>
