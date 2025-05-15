import os
from .person import Person

class Cat(Person):
    def __init__(self, name="喵喵", image_path=None, position=(5, 20)):
        if image_path is None:
            current_dir = os.path.dirname(__file__)
            image_path = os.path.join(current_dir, "img/cat_dithered.bmp")
        super().__init__(name, image_path, position)
        self.voice_lines = [
            "記得多喝水喔～",
            "你今天好棒！",
            "想不想摸摸我？"
        ]

