# minuku_backend

#This is minuku backend

URL = https://minukutest.nctu.me

<h2>Method</h2>

<p>1./minukutest/login<br></p>
  <p>http method : post<br></p> 
  <p>input : {'signupAccount':'your signup email addr','signupPassword':'your password'}<br></p>
  <p>response1 : {'msg':'success','userName':'your name','signupAccount':'your signup email addr'},200  # login success<br></p>
  <p>response2 : {'error':'wrong password'},404 #wrong pw<br></p>
  <p>response3 : {'error':'no this account'},404 #wrong account<br></p>

<p>ex:<br>
curl -iX POST -H "Content-Type:application/json" -d '{"signupAccount":"armuro@test.com","userName":"armuro","signupPassword":"minuku","signupEmail":"armuro@test.com"}' https://minukutest.nctu.me/minukutest/login<br>
response: {"msg":"success","signupAccount":"armuro@test.com","userName":"armuro"}<br></p>


<p>2. /minukutest/signup<br></p>
   <p>http method : post<br></p>
   <p> input : {'signupAccount':'your email addr','userName':'your name','signupPassword':'your passwrod,'signupEmail':'your email addr'}<br></p>
   <p>response1 : {'error':'this account already used'},404<br></p>
   <p>response2 : {'msg':'create account success','userName':'your name','signupAccount':'your signup email addr'},200<br></p>

<p>ex:<br>
curl -iX POST -H "Content-Type:application/json" -d '{"signupAccount":"jack@test.com","userName":"jack","signupPassword":"123","signupEmail":"jack@test.com"}' https://minukutest.nctu.me/minukutest/signup<br>
response: {"msg":"create account success","signupAccount":"jack@test.com","userName":"jack"}<br></p>
<p>3. /minukutest/<string:signupAccount$gt>/profile<br></p>
   <p>http method : GET<br></p>
   <p>response1 : {"signupAccount":"your email addr","signupEmail":"your email addr","signupPassword":"your password","userName":"your name","signupTime":"your signuptime"},200<br></p>

<p>ex:</br>
curl -iX GET -H "Content-Type:application/json" https://minukutest.nctu.me/minukutest/test@test.com/profile<br>
response:{"signupAccount":"test@test.com","signupEmail":"test@test.com","signupPassword":"minuku","userName":"armuro","signupTime":"******"}<br><p> 
