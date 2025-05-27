import json

from application import app

client = app.test_client()

def test_users_api():
    resp = client.get('/users/')
    assert  resp.status_code == 200

    resp = client.post('/users/')
    assert resp.status_code == 200
    data = resp.json
    assert 'result' in data
    assert data['result'] == 'success'