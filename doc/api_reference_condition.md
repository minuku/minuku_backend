API Reference_condition
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create condition

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition?<em><b>token</b></em>=token </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |---------|----------------------|----------------|
    | <em><b>projectname<b></em> |  | Required |
    | <em><b>situationname<b></em> |  | Required |
 	| <em><b>token<b></em> | contain account | Required |



- ### Request body
     
	 `{'conditionName':'name','conditionContent':'whatever you need'}`
 
    | Key   |      Type     |  Value | Note  |
    |:------|:-------------:|:------:|:-----:|
    | <b>conditionName</b> | string | condition name | Required |
 	| <b>conditionContent</b> |  | condition content | Required |
     

- ### Response message
    
	| Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"condition create success"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition already exist"}` |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Delete condition

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 

    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>conditionname</b></em> |  | Required |
	| <em><b>token<b></em> | contain account  | Required |
     
- ### Request body

    | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"condition delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Get condition

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>conditionname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------| 
	|<b>Success message</b> | 200 | `{"createTime": "Sat Jul 14 15:27:01 2018",  "lastEditTime": "", "conditionName": "condition1","conditionContent":"whatever you need"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    
---

# Get all conditions

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>account</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
    
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `[...]`(whole condition array of this situation) |
    |<b>Error message</b> | 200 | `[]`  (if conditionArray is empty, just return an empty array) |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Edit condition

- ### Http request 
<code> PUT /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>conditionname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>conditionName</b> | string  | new condition name | required |
	|<b>conditionContent</b> |   | new condition content(anything would be accepted) | required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------| 
	|<b>Success message</b> | 200 | `{"msg":"condition edit success"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |


