from kink import inject

@inject
class UiController:
    def __init__(self, window):
        self.window = window
    
    def update_ui_text(self, text: str):
        self.window.update_text(text)