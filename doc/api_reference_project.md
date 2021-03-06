API Reference_project
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create project

- ### Http request 
<code> POST /project?<em><b>token</b></em>=token </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
 	| <em><b>token<b></em> | contain account  | Required |


- ### Request body
     `{'projectName':'name'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    | <b>projectName</b> | string | project name | Required |

- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"project create success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project already exist"}` |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Delete project

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>?<em><b>token</b></em>=token</code>

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
    |<b>Success message</b> | 200 | `{"msg":"project delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Edit project

- ### Http request 
<code> PUT /project/<em><b>projectname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>newProjectName</b> | string | new project name | option |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"project edit success"}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |



---


# GET project

- ### Http request 
<code>PUT /project/<em><b>projectname</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>token<b></em> | contain account  | Required |

- ### Request body
    
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
	|<b>None</b> |  |  |  |
- ### Response message

    | Type   |      Code     |  Message |
    |----------|------------|------|
    |<b>Success message</b> | 200 | `{"projectName": "projectname", "questionnaires": [], "createTime": "Thu Dec 13 06:42:29 2018", "dataCollections": [], "situations": [], "lastEditTime": ""}` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"project Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
    
---

# Get all projects

- ### Http request 
<code>GET /project?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    | <em><b>token<b></em> | contain account  | Required |
- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `["project2", "project2"]` |
    |<b>Error message</b> | 404 | `{"error":"projectArray empty"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
