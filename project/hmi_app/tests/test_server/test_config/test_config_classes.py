
def test_dev_config_init(dev_app):
    assert dev_app.config['FLASK_DEBUG'] == 1

def test_prod_config_init(prod_app):
    assert prod_app.config['FLASK_DEBUG'] == 0