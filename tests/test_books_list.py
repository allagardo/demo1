from  application import app

client = app.test_client()

def test_book_list():
    resp = client.get('/books/')
    assert resp.status_code == 200
    assert 'result' in resp.json
    assert resp.json['result'] == []


    resp = client.post('/books/',json={
        'bookname': 'Idiot',
        'author': 'Dostoevskiy F.M',
        'year': '1876'
    } )
    data = resp.json
    assert resp.status_code == 200
    assert data['result'] == 'success'

    resp = client.get('/books/')
    assert resp.status_code == 200
    assert 'result' in resp.json
    assert resp.json['result'] == [{ 'bookname': 'Idiot',
        'author': 'Dostoevskiy F.M',
        'year': '1876'}]
