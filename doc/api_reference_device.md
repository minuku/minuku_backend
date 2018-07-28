API Reference_device
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create device

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection/<em><b>datacollectionname</b></em>/device?<em><b>token</b></em>=token </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>projectname<b></em> |  | Required |
    | <em><b>situationname<b></em> |  | Required |
	| <em><b>datacollectionname<b></em> |  | Required |
 	| <em><b>token<b></em> | contain account  | Required |


- ### Request body
     `{'deviceName':'name','deviceType':'type','deviceContent':'whatever you want'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    | <b>deviceName</b> | string | device name | Required |
	| <b>deviceType</b> | string | device type | Required |     
	| <b>deviceContent</b> | string | device content | Required |
- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"device create success"}` |
    |<b>Error message</b> | 404 | `{"error":"deviceArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"device already exist"}` |
    |<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
---

# Delete device

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection/<em><b>datacollectionname</b></em>/device/<em><b>devicename</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
	|<em><b>devicename</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"device delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"deviceArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"device Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Get device

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection/<em><b>datacollectionname</b></em>/device/<em><b>devicename</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
	|<em><b>devicename</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
    
	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
	|<b>None</b> |  |  |  |
- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"device delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"deviceArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"device Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |    

---

# Get all devices

- ### Http request 
<code>GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection/<em><b>datacollectionname</b></em>/device?<em><b>token</b></em>=token</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"device delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"deviceArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"device Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

---

# Edit device

- ### Http request 
<code> PUT /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection/<em><b>datacollectionname</b></em>/device/<em><b>devicename</b></em>?<em><b>token</b></em>=token</code>

- ### Path parameter 
    
	| Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
	|<em><b>devicename</b></em> |  | Required |
    | <em><b>token<b></em> | contain account  | Required |

- ### Request body
    `{'deviceContent':'whatever you want'}`

	| Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
	| <b>deviceContent</b> | string | new device content | Required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------|
    |<b>Success message</b> | 200 | `{"msg":"device delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"deviceArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"device Not exist"}` |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |
	|<b>Error message</b> | 401 | HTTP/1.1 401 UNAUTHORIZED<br>Date: Tue, 24 Jul 2018 12:25:33 GMT<br>Server: Apache/2.4.18 (Ubuntu)<br>WWW-Authenticate: error=invalid_token,error_description=The token expired<br>Content-Length: 0<br>Access-Control-Allow-Origin: *<br>Content-Type: text/html; charset=utf-8 |

