import pytest
from dotenv import load_dotenv
import os
import qrono

load_dotenv()


@pytest.fixture(autouse=True)
def setup_qrono():
    orig_attrs = {
        "api_key": qrono.api_key,
    }
    qrono.api_key = os.environ.get(
        "QRONO_SECRET_KEY", "qrono_test_key")
    yield
    qrono.api_key = orig_attrs["api_key"]
