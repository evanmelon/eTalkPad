from PIL import Image

from .message import MessageBubble

class Person:
    def __init__(self, name, image_path, position=(0, 0)):
        self.name = name
        self.image_path = image_path
        self.position = position
        self.image = Image.open(image_path).convert("1").resize((80, 80))

    def say(self, text):
        return MessageBubble(text, (self.position[0] + 90, self.position[1] + 10))

    def render(self, canvas):
        canvas.paste(self.image, self.position)

