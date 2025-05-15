import random
from pet import Cat, PetCanvas

if __name__ == "__main__":
    cat = Cat()
    msg = cat.say("今天的你真的超棒喔！記得多喝水")

    msg = cat.say(cat.voice_lines[random.randint(0, 2)])
    canvas = PetCanvas()
    canvas.add(cat)
    canvas.add(msg)
    canvas.render_all()
    canvas.preview()
