from PIL import Image, ImageDraw

from .message import MessageBubble

class PetCanvas:
    def __init__(self, size=(250, 122)):
        self.size = size
        self.canvas = Image.new("1", size, 1)
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def render_all(self):
        draw = ImageDraw.Draw(self.canvas)
        for obj in self.objects:
            if hasattr(obj, "render"):
                obj.render(draw if isinstance(obj, MessageBubble) else self.canvas)

    def preview(self):
        self.canvas.show()

    def save(self, path):
        self.canvas.save(path)

