import pytest
import requests
import json


url = 'http://127.0.0.1:5000'
payload = {"email": "mariolycanreddfox@gmail.com","username": "marioredfoxfshm"}
payload_put = {"email": "lyca@gmail.com","username": "lycan"}


headers = {"content-type": "application/json"}

def test_user_add():
    r = requests.post(url+'/user', data=json.dumps(payload), headers=headers)
    assert r.json()['email'] == payload['email']
    assert r.json()['username'] == payload['username']
    assert r.status_code == 200


def test_user_all():
    r = requests.get(url+'/user') 
    assert r.status_code == 200 

def test_user_id():
    r = requests.get(url+'/user/6') 
    assert r.status_code == 200 

def test_user_update():
    r = requests.put(url+'/user/8', data=json.dumps(payload_put), headers=headers) 
    assert r.json()['email'] == payload_put['email']
    assert r.json()['username'] == payload_put['username']
    assert r.status_code == 200
    
def test_user_delete():
    r = requests.delete(url+'/user/6') 
    if r :
        assert r.status_code == 200 
    else:
        assert r.status_code == 500 