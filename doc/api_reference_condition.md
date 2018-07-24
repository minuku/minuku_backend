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
     
	 `{'conditionName':'name'}`
 
    | Key   |      Type     |  Value | Note  |
    |:------|:-------------:|:------:|:-----:|
    | <b>conditionName</b> | string | condition name | Required |
 
     

- ### Response message
    
	| Type   |      Code     |  Message |
    |----------|:------------:|:------:|
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
    |----------|:------------:|:------:|
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
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `{"timeLasting_unit": "", "createTime": "Sat Jul 14 15:27:01 2018", "rules": ["transpotation", "accelerometer", "rotation", "gravity", "gyroscope", "light", "magnetic", "pressure", "proximity", "temperature", "humidity", "appUsage", "ringer", "battery", "telephony", "connectivity"], "lastEditTime": "", "timeEnd": "", "timeStart": "", "timeLasting": "", "conditionName": "condition1"}` |
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
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `["condition2", "condition1"]` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
