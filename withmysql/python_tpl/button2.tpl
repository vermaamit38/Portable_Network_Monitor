<!DOCTYPE>
<html>
 <body bgcolor="#CEF6F5">
	<title>
Uses of all Connected Computers
	
	  //

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

<p>Show uses of all Connected Computers</p> 

<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_ipv6_packet</th></tr>
    </thead>
    <tbody>
     %for row in rows1:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

<br><br>
<!-- -->

<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_ipv4_packet</th></tr>
    </thead>
    <tbody>
     %for row in rows2:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

 <br><br>
<!-- -->

<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_nbns_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows3:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

 <br><br>
<!-- -->

<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_http_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows4:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

<br><br>
<!-- -->


<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_igmp_protocol</th></tr>
    </thead>
    <tbody>
    
        %for row in rows5:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

  <br><br>
<!-- -->


<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_dns_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows6:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

<br><br>
<!-- -->


<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_dhcp_protocol</th></tr>
    </thead>
    <tbody>
    %for row in rows7:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

<br><br>

<!-- -->
<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_arp_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows8:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

 <br><br>
<!-- -->
<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_nbdgm:smb:browser_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows9:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

<br><br>
<!-- -->


     
<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_bootp_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows10:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

 <br><br>
<!-- -->
     

 
     
<table class="table table-striped">
    <thead>
     <tr><th>Mac</th><th>count_http:data_protocol</th></tr>
    </thead>
    <tbody>
     %for row in rows11:
          <tr>
          %for col in row:
          <td>{{col}}</td>
          %end
         </tr>
        %end
    </tbody>
  </table>

 <br><br>
<!-- -->
     
     
     
<br>
    
	
 
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


        


