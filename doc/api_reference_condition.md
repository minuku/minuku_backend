API Reference_condition
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create condition

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>projectname<b></em> |  | Required |
    | <em><b>situationname<b></em> |  | Required |
 


- ### Request body
     `{'account':'your email','conditionName':'name'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |
    | <b>conditionName</b> | string | condition name | Required |
 
     

- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `{"msg":"condition create success"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition already exist"}` |
    
---

# Delete condition

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em></code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>conditionname</b></em> |  | Required |
     
- ### Request body
     `{'account':'your email'}`
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `{"msg":"condition delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"condition Not exist"}` |


---

# Get condition

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em>?<em><b>account</b></em>=youraccount</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>conditionname</b></em> |  | Required |
    |<em><b>account</b></em> |  | Required |
     
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

    
---

# Get all conditions

- ### Http request 
<code> GET /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition?<em><b>account</b></em>=youraccount</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>account</b></em> |  | Required |
    
- ### Request body
     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>None</b> |  |  |  |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `["condition2", "condition1"]` |
    |<b>Error message</b> | 404 | `{"error":"conditionArray empty"}` |
