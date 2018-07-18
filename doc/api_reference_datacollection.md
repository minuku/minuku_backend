API Reference_datacollection
===
**URIs relative to <em style='color:Dark'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create datacollection

- ### Http request 
<code> POST /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/datacollection </code> 

- ### Path parameter 
 
    | Field   |      Description     |  Note |
    |----------|------------|------|
    | <em><b>projectname<b></em> |  | Required |
    | <em><b>situationname<b></em> |  | Required |
 


- ### Request body
     `{'account':'your email','datacollectionName':'name'}`
 
     | Key   |      Type     |  Value | Note  |
    |:------|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |
    | <b>datacollectionName</b> | string | condition name | Required |
 
     

- ### Response message
    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `{"msg":"datacollection create success"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection already exist"}` |
    
---

# Delete datacollection

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>conditionname</b></em></code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
     
- ### Request body
     `{'account':'your email'}`

     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `{"msg":"datacollection delete success"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection Not exist"}` |


---

# Get datacollection

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition/<em><b>datacollectionname</b></em></code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    |<em><b>datacollectionname</b></em> |  | Required |
     
- ### Request body
     `{'account':'your email'}`

     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|------------|------|
    |<b>Success message</b> | 200 | `{"createTime": "Sun Jul 15 11:16:51 2018", "datacollectionType": "datacollection", "lastEdittime": "", "devices": [], "datacollectionName": "datacollection1"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
    |<b>Error message</b> | 404 | `{"error":"datacollection Not exist"}` |

    
---

# Get all datacollections

- ### Http request 
<code> DELETE /project/<em><b>projectname</b></em>/situation/<em><b>situationname</b></em>/condition</code>

- ### Path parameter 
    | Field    |      Description     |  Note |
    |----------|:------------:|:------:|
    |<em><b>projectname</b></em> |  | Required |
    |<em><b>situationname</b></em> |  | Required |
    
- ### Request body
    `{'account':'your email'}`

     | Key   |      Type     |  Value | Note  |
    |:------:|:------------:|:------:|:------:|
    |<b>account</b> | string | user account | Required |

- ### Response message

    | Type   |      Code     |  Message |
    |----------|:------------:|:------:|
    |<b>Success message</b> | 200 | `["datacollection2", "datacollection1"]` |
    |<b>Error message</b> | 404 | `{"error":"datacollectionArray empty"}` |
