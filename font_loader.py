import os
from PIL import ImageFont

def load_font(size=14, font_name="NotoSansTC-Regular.ttf"):
    """
    從專案內的 fonts 資料夾載入字體

    :param size: 字體大小
    :param font_name: 字體檔名（預設使用 NotoSansTC-Regular）
    :return: PIL.ImageFont 物件
    """
    current_dir = os.path.dirname(__file__)
    font_path = os.path.join(current_dir, "fonts", font_name)

    if not os.path.exists(font_path):
        raise FileNotFoundError(f"❌ 字體檔案未找到：{font_path}")

    return ImageFont.truetype(font_path, size)

