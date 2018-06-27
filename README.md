# minuku_backend

#This is minuku backend

URL = https://minukutest.nctu.me

<h2>URI</h2>

<p>1./minukutest/login<br></p>
  <p>method : post<br></p> 
  <p>input : {'signupAccount':'your signup email addr','signupPassword':'your password'}<br></p>
  <p>response1 : {'msg':'success'},200  # login success<br></p>
  <p>response2 : {'error':'wrong password'},404 #wrong pw<br></p>
  <p>response3 : {'error':'no this account'},404 #wrong account<br></p>

<p>2. /minukutest/signup<br></p>
   <p>method : post<br></p>
   <p> input : {'signupAccount':'your email addr','userName':'your name','signupPassword':'your passwrod,'signupEmail':'your email addr']}<br></p>
   <p>response1 : {'error':'this account already used'},404<br></p>
   <p>response2 : {"msg":"create account success","userName":"armuro"},200<br></p>

