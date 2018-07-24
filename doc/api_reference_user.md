API Reference_user
===
**URIs relative to <em style='color:red'><code>https://minukutest.nctu.me/minukutest</code></em>,unless otherwise noted.**




# Get user profile

- ### Http request  
<code> GET /profile?<em><b>token</b></em>=token </code>

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
            <td><em><b>token</b></em></td>
                <td>contain account inside</td>
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
        </thead>
		<tbody>
			<tr><td>None</td>
				<td></td>
				<td></td>
				<td></td>
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
                <td><code>{"account":"your email addr","email":"your email addr","password":"your password","username":"your name","signupTime":"your signuptime"}</code></td>
            </tr>
			<tr>
				<td><b>Error message</b></td>
                <td>401</td>
                <td><code>HTTP/1.1 401 UNAUTHORIZED
				Date: Tue, 24 Jul 2018 03:41:06 GMT
				Server: Apache/2.4.18 (Ubuntu)
				WWW-Authenticate: error=invalid_token,error_description=The token is wrong
				Content-Length: 0
				Access-Control-Allow-Origin: *
				Content-Type: text/html; charset=utf-8</code></td>
            </tr>
			<tr>
				<td><b>Error message</b></td>
                <td>401</td>
                <td><code>HTTP/1.1 401 UNAUTHORIZED<br>
				Date: Tue, 24 Jul 2018 03:41:06 GMT<br>
				Server: Apache/2.4.18 (Ubuntu)<br>
				WWW-Authenticate: error=invalid_token,error_description=The token is expired<br>
				Content-Length: 0<br>
				Access-Control-Allow-Origin: *<br>
				Content-Type: text/html; charset=utf-8</code></td>
            </tr>
        </tbody>
    </table>
    
---

# Update user profile

- ### Http request 
<code> PUT /profile?<em><b>token</b></em>=token</code>

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
            <td><em><b>token</b></em></td>
                <td>contain account inside</td>
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
            <tr><td colspan="4"><code>{'<b>username</b>':'<i>new username</i>','<b>password</b>':'<i>new passwrod</i>,'<b>email</b>':'<i>new email</i>'}</code></td></tr>
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
                <td>update profile success</td>
            </tr>
			<tr>
				<td><b>Error message</b></td>
                <td>401</td>
                <td><code>HTTP/1.1 401 UNAUTHORIZED<br>
				Date: Tue, 24 Jul 2018 03:41:06 GMT<br>
				Server: Apache/2.4.18 (Ubuntu)<br>
				WWW-Authenticate: error=invalid_token,error_description=The token is wrong<br>
				Content-Length: 0<br>
				Access-Control-Allow-Origin: *<br>
				Content-Type: text/html; charset=utf-8</code></td>
            </tr>
			<tr>
				<td><b>Error message</b></td>
                <td>401</td>
                <td><code>HTTP/1.1 401 UNAUTHORIZED<br>
				Date: Tue, 24 Jul 2018 03:41:06 GMT<br>
				Server: Apache/2.4.18 (Ubuntu)<br>
				WWW-Authenticate: error=invalid_token,error_description=The token is expired<br>
				Content-Length: 0<br>
				Access-Control-Allow-Origin: *<br>
				Content-Type: text/html; charset=utf-8</code></td>
            </tr>
        </tbody>
    </table>
