# minuku_backend
**This is minuku backend**

## REST API Documentation

#### URL = https://minukutest.nctu.me/minukutest
Endpoints for minuku project.

* [Login](#login) : `POST /login`
* [Signup](#signup) : `POST /signup`
* [Show User Profile](#user-profile) : `GET /:signupAccount/profile`
* [Update User Profile](#user-profile) : `PUT /updateProfile`


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
  * response: ```{"msg":"success","account":"test@test.com","username":"armuro"}```

### signup
signup method.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/signup`  |
  | Method  | **POST** |
  | URL Params | none |
  | Data Params | **Required:** <br/> `{'account':'your email addr','username':'username','password':'passwrod}` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{ msg:'create account success', 'username':'username','account':'your signup email addr'}` |
  | Error Response  | **Code:** 404 DUPLICATE ACCOUNT <br /> **Content:** ` {'error': 'this account already used'}` |

* **Sample Call:**

  ```curl
  curl -iX POST -H "Content-Type:application/json" -d '{"account":"jack@test.com","username":"jack","password":"123"}' https://minukutest.nctu.me/minukutest/signup
  ```
  * response: ```{"msg":"create account success","account":"jack@test.com","username":"jack"}```


### Get User Profile
Return json data about uesr porfile.

  | Title  | mention |
  | ------------- | ------------- |
  | URL  | `/<string:account>/profile`  |
  | Method  | **GET** |
  | URL Params | **Required:** <br/> `account=[string]` |
  | Data Params | **Optional:** <br/> `?account=[string]` |
  | Success Response  | **Code:** 200 <br /> **Content:** `{"account":"your email addr","email":"your email addr","password":"your password","username":"your name","signupTime":"your signuptime"}` |

* **Sample Call:**

  ```curl
  curl -iX GET -H "Content-Type:application/json" https://minukutest.nctu.me/minukutest/test@test.com/profile
  ```
  * response: ```{"account":"test@test.com","email":"test@test.com","password":"minuku","username":"armuro","signupTime":"******"}```


### Update User Profile
Update username, email and password

  | Title | mention |
  | -------------- | -------------- |
  | URL | `/updateProfile` |
  | Method | **PUT** |
  | URL Params | None |
  | Query Component | **Required:** <br/> `?account=[string]` |
  | Data Params | `{'username':'new username','password':'new password','email':'new email'}` |
  | Success Response | **Code:** 200 <br /> |

* **Sample Call:**

  ```curl 
  curl -iX PUT -H "Content-Type:application/json" -d '{"username":"sara","password":"123456","email":"sara@test.com"}' https://minukutest.nctu.me/minukutest/updateProfile?account=jim@test.com
  ```
  * response: ```200 ok```
