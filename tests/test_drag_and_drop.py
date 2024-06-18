import os
from pages.drag_and_drop_page import DragAndDropPage
from dotenv import load_dotenv
import time

load_dotenv()


class TestDragAndDrop:
    base_url = os.getenv("DRAG_AND_DROP_URL")

    def test_drag_and_drop(self, driver):
        page = DragAndDropPage(driver, self.base_url)
        page.open()
        text = page.drag_and_drop()
        assert text == "Dropped!"

    def test_drag_and_drop2(self, driver):
        page = DragAndDropPage(driver, self.base_url)
        page.open()
        text = page.drag_and_drop2()
        assert text == "Dropped!"
