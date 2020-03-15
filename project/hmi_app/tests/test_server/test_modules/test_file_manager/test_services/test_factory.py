
import pytest

from server.modules.file_manager.services.factory import process_command

def test_factory_exception():

    with pytest.raises(NotImplementedError) as exc:

        process_command('create test')

    assert str(exc.value) == 'Method is not implemented yet'