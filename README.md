# minuku_backend

#This is minuku backend

URL = https://minukutest.nctu.me

<h2>URI</h2>

1.<p>/minukutest/logini<br></p>
  <p>method : post<br></p> 
  <p>input : {'signupAccount':'your signup email addr','loginPassword':'your password'}<br></p>
   response1 : {'msg':'success'},200  # login success<b>
   response2 : {'error':'wrong password'},404 #wrong pw<b>
   response3 : {'error':'no this account'},404 #wrong account<b>

2. /minukutest/signup<b>
    method : post<b>
    input : {'signupAccount':'your email addr','userName':'your name','signupPassword':'your passwrod,'signupEmail':'your email addr']}<b>
    response1 : {'error':'this account already used'},404<b>
    response2 : {"msg":"create account success","userName":"armuro"},200<b>

