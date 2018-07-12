API Reference_project
===
**URIs relative to <em style='color:red'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**


# Create project

- ### Http request 
    <code> POST https://minukutest.nctu.me/minukutest/createProject </code> 

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
                <td>None</td>
                <td></td>
                <td><b></b></td> 
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
            <tr><td colspan="4"><code>{'account':'your email','projectName':'name'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user account</td>
                <td></td>
            </tr>
            <tr>
            <td><b>projectName</b></td>
                <td>string</td>
                <td>project name</td>
                <td></td>
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
                <td><code>{"datacollections": [], "schedules": [], "conditions": [], "projectName": "name", "situations": [], "createTime": "Thu Jul 12 07:22:32 2018"}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{"error":"project already exist"}</code></td>
            </tr>
        </tbody>
    </table>
    
---

# Delete project

- ### Http request 
    <code> POST https://minukutest.nctu.me/minukutest/updateProfile/deleteProject</code>

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
                <td>None</td>
                <td></td>
                <td><b></b></td> 
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
            <tr><td colspan="4"><code>{'account':'your email','projectName':'name'}</code></td></tr>
        </thead>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user account</td>
                <td></td>
            </tr>
            <tr>
            <td><b>projectName</b></td>
                <td>string</td>
                <td>project name</td>
                <td></td>
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
                <td colspan="4"><code>[{"situations": [], "datacollections": [], "projectName": "minuku", "conditions": [], "createTime": "Wed Jul 11 12:50:11 2018", "schedules": []}, {"situations": [], "datacollections": [], "projectName": "sleep", "conditions": [], "createTime": "Wed Jul 11 12:56:24 2018", "schedules": []}, {"situations": [], "datacollections": [], "projectName": "second", "conditions": [], "createTime": "Thu Jul 12 07:35:41 2018", "schedules": []}]</code></td>
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
        </tbody>
    </table>
