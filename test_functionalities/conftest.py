from pathlib import Path
import sys

from playwright.sync_api import Page ,expect
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utilities import readconfigurations


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(request, page: Page):
    url = readconfigurations.read_configuration("basic info", "url")
    page.goto(url)
    if request.cls is not None:
        request.cls.page = page
        request.cls.expect = expect
    yield
    page.close()
