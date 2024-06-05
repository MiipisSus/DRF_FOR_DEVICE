import requests
import json

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
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    data = \
        {
            "profile_0": 
                {
                    "enabled": False,
                }
        }
    res = requests.post(url, headers=headers, json=data)
    print(res.status_code, res.content)
    
def set_multimedia_value_image(username, password):
    url = "http://127.0.0.1:8000/api/device_info/image/update/"
    token = get_auth(username, password)
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    data = \
        {
            "imaging_0": 
                {
                    "brightness": 40
                }
        }
    res = requests.post(url, headers=headers, json=data)
    print(res.status_code, res.content)
    
def set_basic_device_info(username, password):
    url = "http://127.0.0.1:8000/api/device_info/basic/update/"
    token = get_auth(username, password)
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    data = \
        {
            "device_name": "Gay",
        }
    res = requests.post(url, headers=headers, json=data)
    print(res.status_code, res.content)
    

username = "admin"
password = "admin"

# get_multimedia_value_video(username, password)
set_multimedia_value_video(username, password)
# set_multimedia_value_image(username, password)
# set_basic_device_info(username, password)