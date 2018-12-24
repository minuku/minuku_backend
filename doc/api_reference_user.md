API Reference_user
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**

# GET user profile

- ### Http request  
<code> GET /profile?<em><b>token</b></em>=token </code>

- ### Path parameter 

    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>token<b></em> | contain account  | Required |


- ### Request body 
    | Key   |      Type     |  Value | Note  |
    |------|------------|------|------|
    | <b>None</b> |  | | |



---

# Update user profile

- ### Http request 
<code> PUT /profile?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |:----------:|:------------:|:------:|
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body

    `{'username':'new username','password':'new passwrod,'email':'new email'}`

     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>username</b> | string | new username | writable |
    |<b>password</b> | string | new passwrod |writable  |
    |<b>email</b> | string | new email|writable|
- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"update profile success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

