import pytest
import requests
import json

headers = {"content-type": "application/json"}

def test_user_add(input_url):
    r = requests.post(input_url[0]+'/user', data=json.dumps(input_url[1]), headers=headers)
    assert r.json()['email'] == input_url[1]['email']
    assert r.json()['username'] == input_url[1]['username']
    assert r.status_code == 200

def test_user_all(input_url):
    r = requests.get(input_url[0]+'/user') 
    assert r.status_code == 200 

def test_user_id(input_url):
    r = requests.get(input_url[0]+'/user/6') 
    assert r.status_code == 200 

def test_user_update(input_url):
    r = requests.put(input_url[0]+'/user/8', data=json.dumps(input_url[2]), headers=headers) 
    assert r.json()['email'] == input_url[2]['email']
    assert r.json()['username'] == input_url[2]['username']
    assert r.status_code == 200
    
def test_user_delete(input_url):
    r = requests.delete(input_url[0]+'/user/6') 
    if r :
        assert r.status_code == 200 
    else:
        assert r.status_code == 500 