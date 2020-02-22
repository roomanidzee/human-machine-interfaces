
def test_numbers_validation(app_client):
    resp = app_client.post(
        '/numbers/validate_numbers',
        data={
            'numbers': '1, 2'
        }
    )

    assert resp.status_code == 302
    assert b'Redirecting' in resp.data
