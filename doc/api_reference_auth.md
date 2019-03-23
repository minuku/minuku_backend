API Reference_auth
===
**URIs relative to <em style='color:Dark'><code>http:///minukutest</code></em>,unless otherwise noted.**

# login

- ### Http request  
<code> POST /login </code>

- ### Path parameter 

    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>token<b></em> | contain account  | Required |


- ### Request body 
	
    `{'account':'user account','password':'user password'}`

    | Key   |      Type     |  Value | Note  |
    |------|------------|------|------|
    | <b>account</b> | string |  user's signup account| unWritable|
    | <b>password</b> | string |  user's signup password| writable|

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{'access_token':'your token(binary)','token_type':'Bearer','expires_in':default is 3600 sec}` |
    |<b>Error message</b> | 404 | `{"error":"wrong password"}` |
    |<b>Error message</b> | 404 | `{"error":"no this account"}` |

---

# signup

- ### Http request 
<code> POST /signup </code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |:----------:|:------------:|:------:|
    |None |   |  |

- ### Request body

    `{'account':'you email address','username':'username','password':'password'}`

     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>account</b> | string | user signup account | unWritable |   
    |<b>username</b> | string |  | writable |
    |<b>password</b> | string |  |writable  |
- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{'access_token':'your token(binary)','token_type':'Bearer','expires_in':default is 3600sec}` |
    |<b>Error message</b> | 404 | `{"error":"this account already used"}` |
    
