from playwright.sync_api import Page, expect
from test_resources.locators import Locators


class Pages:
    def __init__(self, page: Page):
        self.page = page

    def open_site(self):
        self.page.goto(Locators.url)

    def navigate_to_page(self, page_name: str):
        slug = Locators.page_urls[page_name]
        self.page.goto(f"{Locators.url}/{slug}")

    def click_element(self, xpath: str):
        self.page.locator(f"xpath={xpath}").click()

    def element_is_visible(self, xpath: str) -> bool:
        return self.page.locator(f"xpath={xpath}").is_visible()

    def element_text(self, xpath: str) -> str:
        return self.page.locator(f"xpath={xpath}").inner_text()

    def fill_field(self, xpath: str, value: str):
        self.page.locator(f"xpath={xpath}").fill(value)

    def check_page_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    def _nav_buttons_visible(self):
        for xpath in [
            Locators.home_upper_button,
            Locators.about_me_upper_button,
            Locators.cv_upper_button,
            Locators.contact_upper_button,
            Locators.home_lower_button,
            Locators.about_me_lower_button,
            Locators.cv_lower_button,
            Locators.contact_lower_button,
            Locators.tg_main_button,
            Locators.tg_secondary_button,
        ]:
            expect(self.page.locator(f"xpath={xpath}")).to_be_visible()

    def user_is_on_home_page(self):
        self.check_page_title(Locators.home_title)
        self._nav_buttons_visible()
        for xpath in [Locators.lets_talk_button, Locators.contact_me_button, Locators.main_skills]:
            expect(self.page.locator(f"xpath={xpath}")).to_be_visible()

    def user_is_on_about_me_page(self):
        self.check_page_title(Locators.about_me_title)
        self._nav_buttons_visible()
        expect(self.page.locator(f"xpath={Locators.contact_me_button}")).to_be_visible()

    def user_is_on_cv_page(self):
        self.check_page_title(Locators.cv_title)
        self._nav_buttons_visible()
        for xpath in [
            Locators.contact_me_button,
            Locators.anritsu,
            Locators.ness,
            Locators.barra,
            Locators.dima,
            Locators.etti,
            Locators.negruzzi,
            Locators.download_cv,
        ]:
            expect(self.page.locator(f"xpath={xpath}")).to_be_visible()

    def user_is_on_contact_page(self):
        self.check_page_title(Locators.contact_title)
        self._nav_buttons_visible()
        for xpath in [
            Locators.linkedin,
            Locators.whatsapp,
            Locators.github,
            Locators.facebook,
            Locators.instagram,
            Locators.twitter,
            Locators.submit_button,
        ]:
            expect(self.page.locator(f"xpath={xpath}")).to_be_visible()

    def verify_pdf_cv(self):
        locator = self.page.locator(f"xpath={Locators.download_cv}")
        locator.scroll_into_view_if_needed()
        assert locator.get_attribute("href") == Locators.cv_pdf_url
        assert locator.get_attribute("target") == "_blank"

    def verify_social_media_link_opens_in_new_tab(self, xpath: str, expected_url: str):
        locator = self.page.locator(f"xpath={xpath}")
        assert locator.get_attribute("href") == expected_url
        assert locator.get_attribute("target") == "_blank"

        with self.page.context.expect_page() as new_page_info:
            locator.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        new_page.close()

    def verify_email_or_phone_link(self, xpath: str, expected_href: str):
        locator = self.page.locator(f"xpath={xpath}")
        assert locator.get_attribute("href") == expected_href
