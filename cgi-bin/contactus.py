import cgi,cgitb
import sys
cgitb.enable()
form=cgi.FieldStorage()
import sqlite3 as s
conn=s.connect('reg.db')
d=conn.execute("select  name,message,status from contact")
data=d.fetchall()
print('content-type:text/html')
print()
print('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Sports</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link href="/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/georgia.js"></script>
<script type="text/javascript" src="js/cuf_run.js"></script>
</head>
<body>
<!-- START PAGE SOURCE -->
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="logo">
        <h1><a href="index.html"><small><h1>SPORTS!!!</h1><h6>Refuse to lose</h6></small><br />
         <marquee><h1 <font color="blue"/> Sports-e-magzine!!</h1></marquee></a></h1>
      </div>
      
    
    <div class="headert_text_resize">
      <div class="menu">
        <ul>
          <li><a href="/index.html">Home</a></li>
          <li><a href="/services.html">News</a></li>
          <li><a href="/about.html" class="active">Register Here</a></li>
        
		  <li><a href="/login.html">login</a></li>
        </ul>
      </div>
      <div class="clr"></div>
      
      <div class="headert_text">
              </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="body">
    <div class="body_resize">
      <div class="left">
        <h2><center>view the posts!!</center></h2>
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>sports e-MAGAZINE</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="tooplate_style.css" rel="stylesheet" type="text/css" />
<!--   Free Website Template by t o o p l a t e . c o m   -->
<script language="javascript" type="text/javascript">
function clearText(field)
{
    if (field.defaultValue == field.value) field.value = '';
    else if (field.value == '') field.value = field.defaultValue;
}
</script>

<link rel="stylesheet" type="text/css" href="css/jquery.lightbox-0.5.css" />    
    
<!-- Arquivos utilizados pelo jQuery lightBox plugin -->
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/jquery.lightbox-0.5.js"></script>
<link rel="stylesheet" type="text/css" href="css/jquery.lightbox-0.5.css" media="screen" />
<!-- / fim dos arquivos utilizados pelo jQuery lightBox plugin -->

<!-- Ativando o jQuery lightBox plugin -->
<script type="text/javascript">
$(function() {
    $('.lightbox').lightBox();
});
</script>
<!--   Free Website Template by t o o p l a t e . c o m   -->
<style>
form {
    border: 3px solid #f1f1f1;
}


input[type=text], input[type=password] {
    width: 35%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
}

label{
display:inline-block;
width:120px;
text-align:right;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 10%;
}

button:hover {
    opacity: 0.8;
}

.cancelbtn {
    width: auto;
    padding: 10px 18px;
    background-color: #f44336;
}

.imgcontainer {
    text-align: center;
    margin: 24px 0 12px 0;
}

img.avatar {
    width: 40%;
    border-radius: 50%;
}

.container {
    padding: 16px;
}

span.psw {
    float: right;
    padding-top: 16px;
}
a:hover {
    opacity: 0.8;
	color="green"
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
    span.psw {
       display: block;
       float: none;
    }
    .cancelbtn {
       width: 100%;
    }
}
</style>


</head>

<body>



<div id="tooplate_wrapper">

	<div id="tooplate_header">
    	
        <div id="tooplate_menu">
  
            <div class="cleaner"></div>
        </div> <!-- end of menu -->
 
        
		
    </div> <!-- end of header -->
 </body>
 </html>
      ''')
print(''' <center><table border=1><th>name:</th><th>message:</th><th>status:</th>''');
for i in data:
          print('''
            <form action="accept.py" method="post"><input type="hidden" value=''',i[0],''' name="ac"/>
              <tr><td>''',i[0],'''</td><td>''',i[1],'''</td>
                                 <td>''',i[2],'''</td>
      
<td><input type="submit" value="accept"/></td></form><br>''')
print('''</center></table>''')

conn.commit();
conn.close();
