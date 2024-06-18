from locators.hover_locators import HoverLocators
from pages.base_page import BasePage


class HoverPage(BasePage):
    locators = HoverLocators()

    def hover(self):
        elem = self.element_is_visible(self.locators.HOVER_BUTTON)
        color_before_navigating = elem.value_of_css_property("background-color")
        self.move_to_element(elem)
        text = self.element_is_visible(self.locators.HOVER_TEXT).text
        color_after_navigating = elem.value_of_css_property("background-color")
        # cursor = elem.value_of_css_property("cursor")
        button_class = elem.get_attribute("class")
        return text, color_before_navigating, color_after_navigating, button_class
