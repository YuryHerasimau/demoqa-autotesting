from locators.drag_and_drop_locators import DragAndDropLocators
from pages.base_page import BasePage


class DragAndDropPage(BasePage):
    locators = DragAndDropLocators()

    def drag_and_drop(self):
        what = self.element_is_visible(self.locators.DRAG_SIMPLE)
        where = self.element_is_visible(self.locators.DROP_SIMPLE)
        self.drag_and_drop_to_element(what, where)
        text = self.element_is_visible(self.locators.DROP_TEXT).text
        return text

    def drag_and_drop2(self):
        what = self.element_is_visible(self.locators.DRAG_SIMPLE)
        where = self.element_is_visible(self.locators.DROP_SIMPLE)
        self.click_and_hold(what)
        self.move_to_element(where)
        self.release(what)
        text = self.element_is_visible(self.locators.DROP_TEXT).text
        return text
