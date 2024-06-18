import os
from pages.click_page import ButtonPage
from dotenv import load_dotenv

load_dotenv()


class TestButton:
    base_url = os.getenv("BUTTON_URL")

    def test_double_click(self, driver):
        page = ButtonPage(driver, self.base_url)
        page.open()
        text = page.double_click_to_elem()
        assert text == "You have done a double click"

    def test_right_click(self, driver):
        page = ButtonPage(driver, self.base_url)
        page.open()
        text = page.right_click_to_elem()
        assert text == "You have done a right click"
