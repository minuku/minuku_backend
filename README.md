# minuku_backend
**This is minuku backend**

## REST API Documentation

#### URL = https://minukutest.nctu.me/minukutest
Endpoints for minuku project.

* [Login](#login) : `POST /login`
* [Signup](#signup) : `POST /signup`
* [Show User Profile](#user-profile) : `GET /:signupAccount/profile`
* [Show User Profile](#user-profile) : `GET /profile2`


### login
Login method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/login`  |
  | Method  | **POST** |
  | URL Params | none |
  | Data Params | **Required:** <br/> `{account: 'signup@email',password: 'password'}` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{ msg:'success', username:'your username', account: 'your signup email addr'}` |
  | Error Response  | **Code:** 404 WRONG PW <br /> **Content:** ` {'error': 'wrong password'}` |
  | Error Response  | **Code:** 404 WRONG ACCOUNT <br /> **Content:** ` {'error': 'no this account'}` |

* **Sample Call:**

  ```curl
  curl -iX POST -H "Content-Type:application/json" -d '{"account":"test@test.com","username":"armuro","password":"minuku","email":"test@test.com"}' https://minukutest.nctu.me/minukutest/login
  ```
  * response: ```{"msg":"success","signupAccount":"test@test.com","username":"armuro"}```

### signup
signup method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/signup`  |
  | Method  | **POST** |
  | URL Params | none |
  | Data Params | **Required:** <br/> `{'account':'your email addr','username':'username','password':'passwrod,'email':'your email addr'}` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{ msg:'create account success', 'username':'username','account':'your signup email addr'}` |
  | Error Response  | **Code:** 404 DUPLICATE ACCOUNT <br /> **Content:** ` {'error': 'this account already used'}` |

* **Sample Call:**

  ```curl
  curl -iX POST -H "Content-Type:application/json" -d '{"account":"jack@test.com","username":"jack","password":"123","email":"jack@test.com"}' https://minukutest.nctu.me/minukutest/signup
  ```
  * response: ```{"msg":"create account success","account":"jack@test.com","username":"jack"}```


### User Profile
Return json data about uesr porfile.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/<string:account>/profile`  |
  | Method  | **GET** |
  | URL Params | **Required:** <br/> `account=[string]` |
  | Data Params | none |
  | Success Response  | **Code:** 200 <br /> **Content:** `{"account":"your email addr","email":"your email addr","password":"your password","username":"your name","signupTime":"your signuptime"}` |

* **Sample Call:**

  ```curl
  curl -iX GET -H "Content-Type:application/json" https://minukutest.nctu.me/minukutest/test@test.com/profile
  ```
  * response: ```{"account":"test@test.com","email":"test@test.com","password":"minuku","username":"armuro","signupTime":"******"}```


### User Profile 
Return json data about uesr porfile.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/profile?account=useraccount`  |
  | Method  | **GET** |
  | URL Params | **Required:** <br/> `account=[string]` |
  | Data Params | none |
  | Success Response  | **Code:** 200 <br /> **Content:** `{"account":"your email addr","email":"your email addr","password":"your password","username":"your name","signupTime":"your signuptime"}` |

* **Sample Call:**

  ```curl
  curl -iX GET -H "Content-Type:application/json" https://minukutest.nctu.me/minukutest/profile2?account=test@test.com
  ```
  * response: ```{"account":"test@test.com","email":"test@test.com","password":"minuku","username":"armuro","signupTime":"******"}```





