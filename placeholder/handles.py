import os
from PIL import Image, ImageColor, ImageDraw, ImageFont

dir_path = os.path.dirname(os.path.realpath(__file__))


def generate_placeholder(
    bg_color="e2e2e2", fnt_color="b9b9b9", size=300, text="placeholder"
) -> Image:
    color = ImageColor.getrgb(f"#{bg_color}")
    font_color = ImageColor.getrgb(f"#{fnt_color}")
    im_shape = (size, size)
    fnt_size = int(size / 10)
    txt = Image.new("RGB", im_shape, color)
    fnt = ImageFont.truetype(f"{dir_path}/ubuntu-font/Ubuntu-B.ttf", fnt_size)

    d = ImageDraw.Draw(txt)
    txt_size = d.textsize(text, font=fnt)
    tw, th = txt_size

    txt_x = (size - tw) / 2
    txt_y = (size - th) / 2

    d.text((txt_x, txt_y), text=text, font=fnt, fill=font_color)

    return txt


if __name__ == "__main__":
    placeholder = generate_placeholder()
    placeholder.show()
