
def test_save_dict(test_app, redis_service):
    test_dict = {
        1: 'test',
        2: 'test1',
        3: 'test2'
    }

    assert not redis_service.save_dict(test_dict)

def test_validate_for_keys(test_app, redis_service):

    test_keys = {'1', '2', '3'}

    result = redis_service.validate_for_keys(test_keys)

    assert len(result) != 0
