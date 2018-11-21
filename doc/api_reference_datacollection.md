API Reference_datacollection
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create datacollection

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/datacollection?<em><b>token</b></em>=token </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>projectname<b></em> |  | Required |
 	| <em><b>token<b></em> | contain account  | Required |


- ### Request body
     `{'datacollectionType':'type','datacollectionName':'name'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    | <b>datacollectionName</b> | string | datacollection name | Required |
	| <b>datacollectionType</b> | string | datacollection type | Required |     

- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"datacollection create success"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection already exist"}` |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Delete datacollection

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/datacollection/<em><b>datacollectionname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"datacollection delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Get datacollection

- ### Http request 
<code>GET /project/<em><b>projectname</b></em>/datacollection/<em><b>datacollectionname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
    
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
	|<b>None</b> |  |  |  |
- ### Response message

    | Type   |      Code     |  Message |
    |----------|------------|------|
    |<b>Success message</b> | 200 | `{"createTime": "Sun Jul 15 11:16:51 2018", "datacollectionType": "datacollection", "lastEdittime": "", "devices": [], "datacollectionName": "datacollection1"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    
---

# Get all datacollections

- ### Http request 
<code>GET /project/<em><b>projectname</b></em>/datacollection?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |
- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `["datacollection2", "datacollection1"]` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
