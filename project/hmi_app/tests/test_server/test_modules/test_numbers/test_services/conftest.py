
import pytest

from server.modules.numbers.services import(
    FilesService,
    NumbersService,
    RedisService
)

@pytest.fixture
def files_service():
    return FilesService('services')


@pytest.fixture
def numbers_service():
    return NumbersService()


@pytest.fixture
def redis_service():
    return RedisService()
