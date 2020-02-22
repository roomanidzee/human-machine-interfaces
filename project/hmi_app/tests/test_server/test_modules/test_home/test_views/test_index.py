
def test_index_page(app_client):
    resp = app_client.get('/index/')
    
    assert resp.status_code == 200
    assert b'Hello!' in resp.data
    assert b'Go to test!' in resp.data