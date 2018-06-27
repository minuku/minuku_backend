# minuku_backend

#This is minuku backend

URL = https://minukutest.nctu.me

<h2>URI</h2>

1. /minukutest/login 
    method : post
    input : {'signupAccount':'your signup email addr','loginPassword':'your password'}
    response1 : {'msg':'success'},200  # login success
    response2 : {'error':'wrong password'},404 #wrong pw
    response3 : {'error':'no this account'},404 #wrong account

2. /minukutest/signup
    method : post
    input : {'signupAccount':'your email addr','userName':'your name','signupPassword':'your passwrod,'signupEmail':'your email addr']}
    response1 : {'error':'this account already used'},404
    response2 : {"msg":"create account success","userName":"armuro"},200

