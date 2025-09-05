import time
import pytest

from pages import login_page
from pages.header import *
from utils.waits import *
from pages.login_page import *


def test_logout(logged_in_driver):
    header = Header(logged_in_driver)
    header.logout()
    wait_for_title(logged_in_driver, "Sign in [Jenkins]")
    assert "Sign in [Jenkins]" in logged_in_driver.title


def test_search(logged_in_driver):
    text = ""

    header = Header(logged_in_driver)
    header.search(text)
    #time.sleep(10)

    if text == "ddd":
        assert f"No results for" in header.get_no_result()

    if text == "m":
        assert any(text.lower() in result.lower() for result in header.get_results)

    if text == "":
        assert f"Get help using Jenkins search" in header.get_results

@pytest.mark.parametrize("text_, expected", [
    ("ddd", "no_results"),
    ("m", "results"),
    ("", "help")
])
def test_search_version2(logged_in_driver, text_, expected):
    header = Header(logged_in_driver)
    result_type = header.search(text_)
    print(print(f"Search returned: {result_type}"))

    if expected == "no_results":
        assert "No results for" in header.get_no_result

    elif expected == "results":
        assert any(text_.lower() in result.lower() for result in header.get_results)

    elif expected == "help":
        assert "Get help using Jenkins search" in header.get_results