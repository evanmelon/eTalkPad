import os
from .person import Person

class Cat(Person):
    def __init__(self, name="喵喵", image_path=None, position=(5, 20)):
        # 根據關鍵字可動態替換整體貓咪圖像
        current_dir = os.path.dirname(__file__)
        if image_path is None:
            image_path = os.path.join(current_dir, "img/cat_dithered.bmp")
        super().__init__(name, image_path, position)
        self.voice_lines = [
            "記得多喝水喔～",
            "你今天好棒！",
            "想不想摸摸我？"
        ]
        # 記錄最後對話，用於依關鍵字切換圖像
        self.last_text = None
        # 儲存預設圖像與關鍵字對應圖檔路徑
        # 使用前請於 img/ 資料夾放置對應貓咪圖片，如 cat_water.bmp, cat_star.bmp
        self.default_image = self.image
        self.keyword_images = {
            # 關鍵字 : 圖檔路徑
            "水": os.path.join(current_dir, "img/cat_dithered.bmp"),
            "棒": os.path.join(current_dir, "img/cat_dithered.bmp"),
            # 可自行新增更多對應關鍵字與圖檔
        }

    def say(self, text):
        # 紀錄對話內容，並返回文字氣泡
        self.last_text = text
        return super().say(text)

    def render(self, canvas):
        # 根據最後對話文字動態選擇貓咪圖像
        self._update_image()
        super().render(canvas)
        # 如需額外裝飾，可保留或呼叫 decorate
        # self._decorate(canvas)

    def _update_image(self):
        """
        根據 self.last_text 中關鍵字，嘗試載入對應整體貓咪圖像，若無則回復預設
        """
        from PIL import Image
        # 無對話或關鍵字不符時，使用預設圖像
        if not self.last_text:
            self.image = self.default_image
            return
        # 檢查每個關鍵字，首次符合則載入對應圖檔
        for key, img_path in self.keyword_images.items():
            if key in self.last_text:
                try:
                    img = Image.open(img_path).convert("1").resize(self.image.size)
                    self.image = img
                except Exception:
                    # 載入失敗則忽略，保留原圖
                    pass
                return
        # 若無任何關鍵字符合，恢復預設圖像
        self.image = self.default_image

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

