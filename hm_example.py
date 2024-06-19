from selene import browser, be, have

def test_positive_from_class():
    """Позитивный тест с урока"""
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    # browser.quit()


def test_positive():
    """Позитивный тест самостоятельно"""
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Стоит использовать selene или проект окончательно'))
    # browser.quit()


def test_negative():
    """Негативный тест на поиск"""

    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type(
        'rfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfrefervrfreferv').press_enter()
    browser.element('[class="w7syQmNN6Yjvw6guGJuQ"]').should(have.text('результаты не найдены'))
    browser.quit()