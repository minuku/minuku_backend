API Reference_situation
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create situation

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/situation?<em><b>token</b></em>=token </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>projectname<b></em> |   | Required |
 	| <em><b>token<b></em> | contain account  | Required |


- ### Request body
     `{'situationtName':'name'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    | <b>situationName</b> | string | situation | Required |

- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"situation create success"}` |
    |<b>Error message</b> | 404 | `{"error":"situation already exist"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project already exist"}` |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Delete situation

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"situation delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
    |<b>Error message</b> | 404 | `{"error":"situationArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"situation Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Edit situation

<code> PUT /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |


- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>newSituationName</b> | string | new situation name | option |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"project edit success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
    |<b>Error message</b> | 404 | `{"error":"situationArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"situation Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---


# GET situation

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>token<b></em> | contain account  | Required |

- ### Request body
    
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
	|<b>None</b> |  |  |  |
- ### Response message

    | Type   |      Code     |  Message |
    |----------|------------|------|
    |<b>Success message</b> | 200 | `{"dataCollections": [], "situationName": "test", "conditions": [], "createTime": "Sat Jul 14 01:27:38 2018", "lastEditTime": ""}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
    |<b>Error message</b> | 404 | `{"error":"situationArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"situation Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    
---

# Get all situations

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    | <em><b>projectname<b></em> |   | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `["situation1", "situation2"]` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"situationArray empty"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
