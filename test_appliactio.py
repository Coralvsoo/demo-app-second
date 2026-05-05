from application import application

def test_hello():
    client = application.test_client()
    resp = client.get('/')
    assert resp.status_code == 200

def test_health():
    client = application.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200