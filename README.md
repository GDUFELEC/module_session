# module_session
Session module using Aliyun OTS written in Python

Making it easy to use as a session system with Aliyun OTS
## Usage
 1. Create a table on Aliyun OTS and then set a primary key named 'token'.

 2. Change the following code in session.py.
```python
OTS_ID = ""
OTS_SECRET = ""
OTS_ENDPOINT = ""
OTS_INSTANCE = ""
table_name = ''
```

3. Use it in your own script.
```python
import session
SESSION = []

def user_login(username, password):
    #Your code here
    token = session.new([
        ("openid",openid),
        ("session_key",data['session_key'])
        #And more
    ])

def verify_token(token):
    if session.check(token) == False:
        return False
    return True

def get_openid(token):
    if verify_token(token) == False: #Check the session if is vaild
        return False
    SESSION = session.read(token)
    return SESSION['openid']
```
## Method
### session.new([])
Create a new session.
### session.check(token)
Validate a session.
### session.read(token)
Read a session.

## License
MIT License
