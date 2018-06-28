# minuku_backend
**This is minuku backend**

# REST API Documentation

#### URL = https://minukutest.nctu.me/minukutest

## login
Login method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/login`  |
  | Method  | **POST** |
  | URL Params | **Required:** <br/> `id=[integer]` |
  | Data Params | **Required:** <br/> `{signupAccount: 'signup@email',signupPassword: 'password'}` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{ msg:'success', userName:'your name', signupAccount: 'your signup email addr'}` |
  | Error Response  | **Code:** 404 WRONG PW <br /> **Content:** ` {'error': 'wrong password'}` |
  | Error Response  | **Code:** 404 WRONG ACCOUNT <br /> **Content:** ` {'error': 'no this account'}` |

* **Sample Call:**

  ```curl
  curl -iX POST -H "Content-Type:application/json" -d '{"signupAccount":"armuro@test.com","userName":"armuro","signupPassword":"minuku","signupEmail":"armuro@test.com"}' https://minukutest.nctu.me/minukutest/login
  ```
  * response: ```{"msg":"success","signupAccount":"armuro@test.com","userName":"armuro"}```

## signup
signup method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/signup`  |
  | Method  | **POST** |
  | URL Params | none |
  | Data Params | **Required:** <br/> `{'signupAccount':'your email addr','userName':'userName','signupPassword':'passwrod,'signupEmail':'your email addr'}` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{ msg:'create account success', 'userName':'userNamee','signupAccount':'your signup email addr'}` |
  | Error Response  | **Code:** 404 DUPLICATE ACCOUNT <br /> **Content:** ` {'error': 'this account already used'}` |

* **Sample Call:**

  ```curl
  curl -iX POST -H "Content-Type:application/json" -d '{"signupAccount":"jack@test.com","userName":"jack","signupPassword":"123","signupEmail":"jack@test.com"}' https://minukutest.nctu.me/minukutest/signup
  ```
  * response: ```{"msg":"create account success","signupAccount":"jack@test.com","userName":"jack"}```


## login
Login method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/minukutest/<string:signupAccount>/profile`  |
  | Method  | **GET** |
  | URL Params | **Required:** <br/> `id=[integer]` |
  | Data Params | none |
  | Success Response  | **Code:** 200 <br /> **Content:** `{"signupAccount":"your email addr","signupEmail":"your email addr","signupPassword":"your password","userName":"your name","signupTime":"your signuptime"}` |

* **Sample Call:**

  ```curl
  curl -iX GET -H "Content-Type:application/json" https://minukutest.nctu.me/minukutest/test@test.com/profile
  ```
  * response: ```{"signupAccount":"test@test.com","signupEmail":"test@test.com","signupPassword":"minuku","userName":"armuro","signupTime":"******"}```
