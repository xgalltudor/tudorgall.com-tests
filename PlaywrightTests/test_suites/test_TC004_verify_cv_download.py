from test_resources.locators import Locators


def test_navigate_to_cv_page_and_check_pdf_download(setup_teardown):
    p = setup_teardown

    p.user_is_on_home_page()
    p.click_element(Locators.cv_upper_button)
    p.user_is_on_cv_page()
    p.verify_pdf_cv()
