class DragAndDropLocators:

    DRAG_SIMPLE = ("css selector", "div[id='draggable']")
    DROP_SIMPLE = (
        "css selector",
        "div[class='simple-drop-container'] div[id='droppable']",
    )
    DROP_TEXT = (
        "css selector",
        "div[class='simple-drop-container'] div[id='droppable'] p",
    )
