from test_resources.locators import Locators


def test_navigate_to_home_page(setup_teardown):
    pages = setup_teardown
    pages.user_is_on_home_page()


def test_click_on_about_me_upper_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.about_me_upper_button)
    pages.user_is_on_about_me_page()


def test_click_on_cv_upper_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.cv_upper_button)
    pages.user_is_on_cv_page()


def test_click_on_contact_upper_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.contact_upper_button)
    pages.user_is_on_contact_page()


def test_click_on_home_upper_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.home_upper_button)
    pages.user_is_on_home_page()


def test_click_on_about_me_lower_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.about_me_lower_button)
    pages.user_is_on_about_me_page()


def test_click_on_cv_lower_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.cv_lower_button)
    pages.user_is_on_cv_page()


def test_click_on_contact_lower_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.contact_lower_button)
    pages.user_is_on_contact_page()


def test_click_on_home_lower_button(setup_teardown):
    pages = setup_teardown
    pages.click_element(Locators.home_lower_button)
    pages.user_is_on_home_page()
