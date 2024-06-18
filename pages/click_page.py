from locators.click_locators import ClickLocators
from pages.base_page import BasePage


class ButtonPage(BasePage):
    locators = ClickLocators()

    def double_click_to_elem(self):
        button = self.element_is_clickable(self.locators.DOUBLE_CLICK)
        self.double_click(button)
        text = self.element_is_visible(self.locators.DOUBLE_TEXT).text
        return text

    def right_click_to_elem(self):
        button = self.element_is_clickable(self.locators.RIGHT_CLICK)
        self.right_click(button)
        text = self.element_is_visible(self.locators.RIGHT_TEXT).text
        return text
