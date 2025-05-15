from PIL import ImageDraw, ImageFont

from font_loader import load_font

class MessageBubble:
    def __init__(self, content, position, font_path=None, font_size=14, max_width=150):
        self.content = content
        self.position = position
        self.font = font = load_font(14)
        self.max_width = max_width

    def render(self, draw):
        x, y = self.position
        line = ""
        lines = []
        for char in self.content:
            test = line + char
            if draw.textlength(test, font=self.font) <= self.max_width:
                line = test
            else:
                lines.append(line)
                line = char
        lines.append(line)
        for i, l in enumerate(lines):
            draw.text((x, y + i * 16), l, font=self.font, fill=0)

