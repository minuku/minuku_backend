API Reference_situation
===
**URIs relative to <em style='color:red'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create situation

- ### Http request 
<code> POST https://minukutest.nctu.me/minukutest/<em>projectname</em>/situation </code> 

- ### Path parameter 
 
     <table>
        <col width="40%">
        <col width="100%">
        <col width="30%">
        <thead>
            <tr>
                <th>Field</th>
                <th>Description</th>
                <th>Note</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><em>projectname</em></td>
                <td></td>
                <td>Required</td> 
            </tr>
        </tbody>
      </table>


- ### Request body
 
     <table>
        <col width="25%">
        <col width="15%">
        <col width="100%">
        <col width="15%">
        <thead>
            <tr>
                <th>Key</th>
                <th>Type</th>
                <th>Value</th>
                <th>Note</th>
            </tr>
            <tr><td colspan="4"><code>{'account':'your email','situationName':'name'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user account</td>
                <td>Required</td>
            </tr>
            <tr>
            <td><b>situationName</b></td>
                <td>string</td>
                <td>situation name</td>
                <td>Required</td>
            </tr>
    </table>

- ### Response message

     <table>
        <thead>
            <tr>
                <th>Type</th>
                <th>Code</th>
                <th>Message</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><b>Success message</b></td>
                <td>200</td>
                <td><code>{"msg":"situation create success"}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{"error":"projectArray empty"}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{"error":"project Not exist"}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{"error":"situation already exist"}</code></td>
            </tr>
        </tbody>
    </table>
    
---

# Delete situation

- ### Http request 
<code> DELETE https://minukutest.nctu.me/minukutest/project/<em>projectname</em>/situation/<em>situationname</em></code>

- ### Path parameter 
 
     <table>
        <col width="40%">
        <col width="100%">
        <col width="30%">
        <thead>
            <tr>
                <th>Field</th>
                <th>Description</th>
                <th>Note</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><em>projectname</em>em></td>
                <td></td>
                <td>Required</td> 
            </tr>
            <tr>
                <td><em>situationname<em></td>
                <td></td>
                <td>Required</td> 
            </tr>
        </tbody>
      </table>


- ### Request body
 
     <table>
        <col width="25%">
        <col width="15%">
        <col width="100%">
        <col width="15%">
        <thead>
            <tr>
                <th>Key</th>
                <th>Type</th>
                <th>Value</th>
                <th>Note</th>
            </tr>
            <tr><td colspan="4"><code>{'account':'your email'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user account</td>
                <td>Required</td>
            </tr>
    </table>

- ### Response message

     <table>
        <thead>
            <tr>
                <th>Type</th>
                <th>Code</th>
                <th>Message</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><b>Success message</b></td>
                <td>200</td>
                <td colspan="4"><code>{'msg':'project delete success'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'project Not exist'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'projectArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situationArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situation Not exist'}</code></td>
            </tr>
        </tbody>
    </table>
    

---

# Get situation

- ### Http request 
<code> GET https://minukutest.nctu.me/minukutest/project/<em>projectname</em>/situation/<em>situationname</em></code>

- ### Path parameter 
 
     <table>
        <col width="40%">
        <col width="100%">
        <col width="30%">
        <thead>
            <tr>
                <th>Field</th>
                <th>Description</th>
                <th>Note</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><em>projectname</em></td>
                <td></td>
                <td>Required</td> 
            </tr>
            <tr>
            <td><em>situationname</em></td>
                <td></td>
                <td>Required</td> 
            </tr>
        </tbody>
      </table>


- ### Request body
 
     <table>
        <col width="25%">
        <col width="15%">
        <col width="100%">
        <col width="15%">
        <thead>
            <tr>
                <th>Key</th>
                <th>Type</th>
                <th>Value</th>
                <th>Note</th>
            </tr>
            <tr><td colspan="4"><code>{'account':'your email'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td></td>
                <td>Required</td>
            </tr>
    </table>

- ### Response message

     <table>
        <thead>
            <tr>
                <th>Type</th>
                <th>Code</th>
                <th>Message</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><b>Success message</b></td>
                <td>200</td>
                <td colspan="4"><code>{"dataCollections": [], "situationName": "test", "conditions": [], "createTime": "Sat Jul 14 01:27:38 2018", "lastEditTime": ""}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'project Not exist'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'projectArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situationArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situation Not exist'}</code></td>
            </tr>
        </tbody>
    </table>
    
---

# Get all situations

- ### Http request 
<code> GET https://minukutest.nctu.me/minukutest/project/<em>projectname</em>/situation</code>

- ### Path parameter 
 
     <table>
        <col width="40%">
        <col width="100%">
        <col width="30%">
        <thead>
            <tr>
                <th>Field</th>
                <th>Description</th>
                <th>Note</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><em>projectname</em></td>
                <td></td>
                <td>Required</td> 
            </tr>
        </tbody>
      </table>


- ### Request body
 
     <table>
        <col width="25%">
        <col width="15%">
        <col width="100%">
        <col width="15%">
        <thead>
            <tr>
                <th>Key</th>
                <th>Type</th>
                <th>Value</th>
                <th>Note</th>
            </tr>
            <tr><td colspan="4"><code>{'account':'your email'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td></td>
                <td>Required</td>
            </tr>
    </table>

- ### Response message

     <table>
        <thead>
            <tr>
                <th>Type</th>
                <th>Code</th>
                <th>Message</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td><b>Success message</b></td>
                <td>200</td>
                <td colspan="4"><code>["situation2", "situation1"]</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'projectArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'project Not exist'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situationArray empty'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td colspan="4"><code>{'error':'situation Not exist'}</code></td>
            </tr>
        </tbody>
    </table>
