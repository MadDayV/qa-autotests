import pytest

from api.client import ApiClient
from config import API_URL


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient(API_URL)
