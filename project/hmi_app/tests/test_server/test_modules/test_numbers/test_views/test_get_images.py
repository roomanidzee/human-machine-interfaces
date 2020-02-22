
def test_get_images(app_client):

    resp = app_client.get('/numbers/get_images')

    assert resp.status_code == 200
    assert b'img' in resp.data

def test_check_memory(app_client):

    resp = app_client.get('/numbers/get_images')

    assert resp.status_code == 200
    assert b'img' in resp.data
