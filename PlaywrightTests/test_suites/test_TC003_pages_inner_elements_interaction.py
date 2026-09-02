from test_resources.locators import Locators


def test_navigate_to_home_page_and_interact_with_inner_elements(setup_teardown):
    p = setup_teardown

    p.user_is_on_home_page()
    p.click_element(Locators.lets_talk_button)
    p.user_is_on_contact_page()
    p.click_element(Locators.tg_main_button)
    p.user_is_on_home_page()
    p.click_element(Locators.contact_me_button)
    p.user_is_on_contact_page()
    p.click_element(Locators.tg_secondary_button)
    p.user_is_on_home_page()
    p.click_element(Locators.main_skills)
    p.user_is_on_cv_page()
    p.click_element(Locators.contact_me_button)
    p.user_is_on_contact_page()
    p.click_element(Locators.home_upper_button)
    p.user_is_on_home_page()


def test_navigate_to_contact_page_and_check_social_media_buttons(setup_teardown):
    p = setup_teardown

    p.user_is_on_home_page()
    p.click_element(Locators.contact_me_button)
    p.user_is_on_contact_page()
    p.verify_social_media_link_opens_in_new_tab(Locators.linkedin, Locators.linkedin_url)
    p.verify_social_media_link_opens_in_new_tab(Locators.whatsapp, Locators.whatsapp_url)
    p.verify_social_media_link_opens_in_new_tab(Locators.github, Locators.github_url)
    p.verify_social_media_link_opens_in_new_tab(Locators.facebook, Locators.facebook_url)
    p.verify_social_media_link_opens_in_new_tab(Locators.instagram, Locators.instagram_url)
    p.verify_social_media_link_opens_in_new_tab(Locators.twitter, Locators.twitter_url)
    p.click_element(Locators.home_upper_button)
    p.user_is_on_home_page()


def test_navigate_to_contact_page_and_check_email_and_phone_links(setup_teardown):
    p = setup_teardown

    p.user_is_on_home_page()
    p.click_element(Locators.contact_me_button)
    p.user_is_on_contact_page()
    p.verify_email_or_phone_link(Locators.yahoo_mail, Locators.yahoo_mail_link)
    p.verify_email_or_phone_link(Locators.google_mail, Locators.google_mail_link)
    p.verify_email_or_phone_link(Locators.phone_number, Locators.phone_number_link)
