import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
import random
from PIL import Image,ImageDraw,ImageFont
import traceback
from pet import Cat, PetCanvas
from display_manager import EpaperDisplayManager
from text_chatgpt import chat_with_gpt


if __name__ == "__main__":
    cat = Cat()
    epd = EpaperDisplayManager()
    # 一開始建 base canvas（含貓咪）
    base_canvas = PetCanvas()
    base_canvas.add(cat)
    base_canvas.add(cat.say(chat_with_gpt("你好～")))
    base_canvas.render_all()
    epd.display_base(base_canvas.canvas)  # 設定成 partial update 的 base

    last_full_update_time = time.time()
    full_update_interval = 60

#     msg = cat.say("今天的你真的超棒喔！記得多喝水")

#     msg = cat.say(cat.voice_lines[random.randint(0, 2)])

    print("💬 ChatGPT CLI 模式（輸入 q 結束）")
    while True:
        user_input = input("你說：")
        if user_input.lower() == 'q':
            end_canvas = PetCanvas()
            end_canvas.add(cat)
            end_canvas.add(cat.say(" 再見！"))
            end_canvas.render_all()
            epd.display_image(end_canvas.canvas)
            print("👋 再見！")
            break

        reply = chat_with_gpt(user_input)
        # 建立新的 canvas 只放文字
        canvas = PetCanvas()
        canvas.add(cat)
        canvas.add(cat.say(reply))
        canvas.render_all()

        now = time.time()
        if now - last_full_update_time >= full_update_interval:
            # 超過設定時間，進行 full update
            epd.display_image(canvas.canvas)
            last_full_update_time = now
        else:
            # 平常使用局部更新
            epd.display_partial(canvas.canvas)

#         # epd.sleep()
