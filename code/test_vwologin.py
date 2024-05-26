import pytest
import allure

from playwright.sync_api import Page, expect, sync_playwright


# Page class will help to interact with the html elements
# expect class will help to validate the expected result == actual result
# validation pytest assert is also available

# structure of playwright testcases are
# browser and page
# code interaction with html web page
# validation

def test_vwo_login():
    # browser and page
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()

    # code interaction with html web page
    page.goto("https://app.vwo.com")

    breakpoint()## IS USED TO DEBUG IN PLAYWRIGHT

    # validation
    expect(page).to_have_title("Login - VWO")
