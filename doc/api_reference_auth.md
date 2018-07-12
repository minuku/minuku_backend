API Reference_auth
===
**URIs relative to <em style='color:red'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**

# login


- ### Http request 
    <code> POST https://minukutest.nctu.me/minukutest/login </code>

- ### Path parameter 
 
    <table>
        <col width="20%">
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
                <td></td>
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
            <tr><td colspan="4"><code>{'<b>account</b>':'<i>your email addr</i>','<b>password</b>':'<i>passwrod</i>'}</code></td></tr>
        </thead>
        <tbody>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user's signup account</td>
                <td>unWritable</td>
            </tr>
            <tr>
            <td><b>password</b></td>
                <td>string</td>
                <td>user's signup password</td>
                <td>Writable</td>
            </tr>
        </tbody>
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
                <td><code>{ msg:'success', username:'your username', account: 'your signup email addr'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{'error': 'wrong password'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{'error': 'no this account'}</code></td>
            </tr>
        </tbody>
    </table>

---

# signup

- ### Http request 
    <code> POST https://minukutest.nctu.me/minukutest/signup </code> 

- ### Path parameter 
 
    <table>
        <col width="20%">
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
                <td></td>
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
            <tr><td colspan="4"><code>{'<b>account</b>':'<i>your email addr</i>','<b>username</b>':'<i>username</i>','<b>password</b>':'<i>passwrod</i>}</code></td></tr>
        </thead>
        <tbody>
            <tr>
            <td><b>account</b></td>
                <td>string</td>
                <td>user's signup account</td>
                <td>unWritable</td>
            </tr>
            <tr>
            <td><b>username</b></td>
                <td>string</td>
                <td></td>
                <td>writable</td>
            </tr>
            <tr>
            <td><b>password</b></td>
                <td>string</td>
                <td>user's signup password</td>
                <td>Writable</td>
            </tr>
        </tbody>
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
                <td><code>{ msg:'create account success', 'username':'username','account':'your signup email addr'}</code></td>
            </tr>
            <tr>
            <td><b>Error message</b></td>
                <td>404</td>
                <td><code>{'error': 'this account already used'}</code></td>
            </tr>
        </tbody>
    </table>

---

# Get user profile

- ### Http request 
    <code> GET https://minukutest.nctu.me/minukutest/<em style="color:DeepPink ">user_account</em>/profile </code> 
    <code> GET https://minukutest.nctu.me/minukutest/profile<em style="color:DeepPink ">?user_account=user_account</em> </code>

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
                <td style="color:DeepPink ">user_account</td>
                <td>string</td>
                <td><b></b></td> 
            </tr>
            <tr>
                <td style="color:DeepPink ">?user_account=user_account</td>
                <td>string</td>
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
            <tr><td colspan="4">None</td></tr>
        </thead>
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
                <td><code>{"account":"your email addr","email":"your email addr","password":"your password","username":"your name","signupTime":"your signuptime"}</code></td>
            </tr>
        </tbody>
    </table>
    
---

# Update user profile

- ### Http request 
    <code> PUT https://minukutest.nctu.me/minukutest/profile<em style="color:DeepPink ">?user_account=user_account</em> </code>

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
                <td style="color:DeepPink ">?user_account=user_account</td>
                <td>string</td>
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
            <tr><td colspan="4"><code>{'<b>username</b>':'<i>username</i>','<b>password</b>':'<i>passwrod</i>,'<b>email</b>':'<i>new email</i>'}</code></td></tr>
        </thead>
        <tbody>
            <tr>
            <tr>
            <td><b>username</b></td>
                <td>string</td>
                <td></td>
                <td>writable</td>
            </tr>
            <tr>
            <td><b>password</b></td>
                <td>string</td>
                <td>user's signup password</td>
                <td>writable</td>
            </tr>
            <td><b>email</b></td>
                <td>string</td>
                <td>user's new email</td>
                <td>writable</td>
            </tr>
        </tbody>
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
                <td colspan="4"><code>{'<b>account</b>':'<i>your email addr</i>','<b>username</b>':'<i>username</i>','<b>password</b>':'<i>passwrod</i>}</code></td>
            </tr>
            <tr>
            <td></td>
            <td></td>
            <td></td>
            </tr>
        </tbody>
    </table>
