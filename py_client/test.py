import requests

def get_auth(username, password):
    auth_url = "http://127.0.0.1:8000/api/auth/"
    payload = {
        "username": username,
        "password": password
    }
    res = requests.post(auth_url, data=payload)
    
    return res.json()['token']
     
def get_multimedia_value_video(username, password):
    url = "http://127.0.0.1:8000/api/device_info/video/"
    token = get_auth(username, password)
    headers = {
        "Authorization": f"Token {token}"
    }
    res = requests.get(url, headers=headers)
    print(f"{res.status_code}\n{res.content}")
    
def set_multimedia_value_video(username, password):
    url = "http://127.0.0.1:8000/api/device_info/video/update/"
    token = get_auth(username, password)
    headers = {
        "Authorization": f"Token {token}"
    }
    res = requests.post(url, headers=headers)
    
    

username = "admin"
password = "admin"

# get_multimedia_value_video(username, password)
set_multimedia_value_video(username, password)