from test_resources.locators import Locators


def test_submit_message_without_completing_fields(setup_teardown):
    p = setup_teardown
    p.user_is_on_home_page()
    p.click_element(Locators.lets_talk_button)
    p.user_is_on_contact_page()
    p.click_element(Locators.submit_button)
    assert not p.element_is_visible(Locators.message_sent)
    p.click_element(Locators.home_upper_button)
    p.user_is_on_home_page()


def test_submit_message_gradually_completing_fields(setup_teardown):
    p = setup_teardown
    p.user_is_on_home_page()
    p.click_element(Locators.lets_talk_button)
    p.user_is_on_contact_page()

    fields = [
        (Locators.contact_name, Locators.name_input),
        (Locators.contact_email, Locators.email_input),
        (Locators.contact_phone, Locators.phone_input),
        (Locators.contact_message, Locators.message_input),
    ]
    for i, (field_xpath, value) in enumerate(fields, start=1):
        p.fill_field(field_xpath, value)
        p.click_element(Locators.submit_button)
        if i < len(fields):
            assert not p.element_is_visible(Locators.message_sent)
        else:
            assert p.element_text(Locators.message_sent) == Locators.message_sent_text

    p.click_element(Locators.home_upper_button)
    p.user_is_on_home_page()


def test_submit_message_completing_required_fields(setup_teardown):
    p = setup_teardown
    p.user_is_on_home_page()
    p.click_element(Locators.lets_talk_button)
    p.user_is_on_contact_page()

    p.fill_field(Locators.contact_name, Locators.name_input)
    p.fill_field(Locators.contact_email, Locators.email_input)
    p.fill_field(Locators.contact_message, Locators.message_input)
    p.click_element(Locators.submit_button)

    assert p.element_text(Locators.message_sent) == Locators.message_sent_text
    p.click_element(Locators.home_upper_button)
    p.user_is_on_home_page()
