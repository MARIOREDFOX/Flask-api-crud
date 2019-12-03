import pytest

@pytest.fixture
def input_url():
    url = 'http://127.0.0.1:5000'
    payload = {"email": "masriolycanreddfox1@gmail.com","username": "marioresdfoxfshm1"}
    payload_put = {"email": "lycsa1@gmail.com","username": "lycsan1"}
    return [url,payload,payload_put]