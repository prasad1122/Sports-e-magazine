import cgi,cgitb
cgitb.enable()
form=cgi.FieldStorage()
regno=form.getvalue('regno')
password=form.getvalue('password')
ad={'regno':'admin','password':'12345'}
import sqlite3
conn=sqlite3.connect('reg.db')
d=conn.execute('select * from regestration where  regno=? and password=?',(regno,password))
data=d.fetchall()
if(regno==ad['regno'] and password==ad['password']):
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
          
        
		  <li><a href="/index.html">logout</a></li>
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
        <h2><center>welcome to admin!!</center></h2>
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
 
   
    
  
     
       <a href='contactus.py'>click here to view message</a> 
		
    
		   
      
  
  ''')
elif(len(data)==1):
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
<script src="js/jquery.js" type="text/javascript"></script>
</head>
<body>
<!-- START PAGE SOURCE -->
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="logo">
        <h1><a href="index.html"><small>Refuse to lose</small><br />
          <marquee>Sports.</marquee></a></h1>
      </div>
      <div class="logo_text"><a href="#">Help</a> | <a href="#">Search</a> | <a href="#">Contacts</a></div>
      <div class="clr"></div>
    </div>
    <div class="headert_text_resize">
      <div class="menu">
        <ul>
          <li><a href="/index.html">Home</a></li>
          <li><a href="/services.html">News</a></li>
          <li><a href="/about.html">Register here</a></li>
          
		  <li><a href="/index.html">logout</a></li>
        </ul>
      </div>
        <div class="body">
    <div class="body_resize">
      <div class="left">
        <h2>contact</h2>
        <form action="/cgi-bin/contact.py" method="post" id="contactform">
          <ul>
            <li>
              <label for="name">Your Name*  </label>
              <input id="name" name="name" class="text" />
            </li>
            
         
            <li>
              <label for="message">Your Message*</label>
              <textarea id="message" name="message" rows="6" cols="50"></textarea>
            </li>
            <li class="buttons">
              <input type="submit" name="imageField" id="imageField"  value="Send message" class="send" />
              <div class="clr"></div>
            </li>
          </ul>
        </form>
      </div>

       </body>
</html>

     <h1><center>Login successfully!!</center><h1> 
  
               
      ''')



else:
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
        <h2><center>Login Failed!!</center></h2>
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
 <center><h1>Login Failed!!!</h1></center>
   
    ''')
		
        
		
   
	
conn.commit()
conn.close()
