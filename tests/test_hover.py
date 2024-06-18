import os
from pages.hover_page import HoverPage
from dotenv import load_dotenv

load_dotenv()


class TestHover:
    base_url = os.getenv("TOOL_TIPS_URL")

    def test_hover(self, driver):
        page = HoverPage(driver, self.base_url)
        page.open()
        text, color_before_navigating, color_after_navigating, button_class = (
            page.hover()
        )
        assert text == "You hovered over the Button"
        assert color_before_navigating != color_after_navigating
        assert button_class == "btn btn-success"
