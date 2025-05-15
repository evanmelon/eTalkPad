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
        # 記錄最後對話，用於圖像裝飾
        self.last_text = None

    def say(self, text):
        # 紀錄對話內容，並返回文字氣泡
        self.last_text = text
        return super().say(text)

    def render(self, canvas):
        # 繪製貓咪圖像，然後根據對話內容裝飾
        super().render(canvas)
        self._decorate(canvas)

    def _decorate(self, canvas):
        if not self.last_text:
            return
        from PIL import ImageDraw
        import math
        draw = ImageDraw.Draw(canvas)
        x, y = self.position
        # 包含「棒」就畫星星
        if "棒" in self.last_text:
            for cx, cy in [(x+20, y+5), (x+60, y+10)]:
                self._draw_star(draw, (cx, cy), 6)
        # 包含「水」就畫水滴
        if "水" in self.last_text:
            bbox = [x+55, y, x+65, y+12]
            draw.ellipse(bbox, outline=0, fill=0)

    def _draw_star(self, draw, center, r, fill=0):
        import math
        points = []
        for i in range(10):
            angle = math.radians(i*36 - 90)
            radius = r if i % 2 == 0 else r*0.5
            px = center[0] + radius * math.cos(angle)
            py = center[1] + radius * math.sin(angle)
            points.append((px, py))
        draw.polygon(points, fill=fill)

