def test_navigate_directly_to_home_page(setup_teardown):
    pages = setup_teardown
    pages.navigate_to_page("Home")
    pages.user_is_on_home_page()


def test_navigate_directly_to_about_me_page(setup_teardown):
    pages = setup_teardown
    pages.navigate_to_page("About me")
    pages.user_is_on_about_me_page()


def test_navigate_directly_to_curriculum_vitae_page(setup_teardown):
    pages = setup_teardown
    pages.navigate_to_page("CV")
    pages.user_is_on_cv_page()


def test_navigate_directly_to_contact_page(setup_teardown):
    pages = setup_teardown
    pages.navigate_to_page("Contact")
    pages.user_is_on_contact_page()
