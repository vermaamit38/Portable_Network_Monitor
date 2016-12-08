<!DOCTYPE>
<html>
 <body bgcolor="#CEF6F5">
	<title>
IP & MAC address
	
	

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

 <h2>Ip_MAc Count</h2>


        %for row in data:
          <td>{{row}}</td>
          <br>
          %end

     
<br><br>
    
	
 
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


        



