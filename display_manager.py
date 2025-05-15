from waveshare_epd import epd2in13_V4
from PIL import Image
import logging

class EpaperDisplayManager:
    def __init__(self):
        logging.info("Initializing e-Paper display...")
        self.epd = epd2in13_V4.EPD()
        self.epd.init()
        self.width = self.epd.height  # 注意這邊是 height -> width（橫向）
        self.height = self.epd.width

    def display_image(self, image: Image.Image):
        """
        將 PIL Image 顯示到電子紙上。
        圖像尺寸應與 epd 大小一致，否則可能會有問題。
        """
        logging.info("Displaying image on e-Paper...")
        self.epd.display(self.epd.getbuffer(image))

    def clear(self):
        """清除畫面"""
        logging.info("Clearing e-Paper...")
        self.epd.Clear(0xFF)

    def sleep(self):
        """進入省電模式"""
        logging.info("Putting e-Paper to sleep...")
        self.epd.sleep()

    def init_fast(self):
        """快速初始化（適合頻繁刷新）"""
        logging.info("Fast init for e-Paper...")
        self.epd.init_fast()

    def display_partial(self, image: Image.Image):
        """只更新局部區塊（需要先用 displayPartBaseImage）"""
        self.epd.displayPartial(self.epd.getbuffer(image))

    def display_base(self, image: Image.Image):
        """設定基礎底圖（供 partial update 使用）"""
        self.epd.displayPartBaseImage(self.epd.getbuffer(image))

