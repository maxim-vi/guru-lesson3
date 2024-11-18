import pytest
from selene import browser, be, have



@pytest.fixture
def size_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768

def test_find_pass(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_find_fail(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('FGDGFD *ˆ% G').press_enter()
    browser.element('[id="topstuff"]').should(have.text('Нет результатов для FGDGFD *ˆ% G.'))