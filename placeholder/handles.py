from PIL import Image, ImageColor, ImageDraw, ImageFont


def generate_placeholder(
    bg_color="e2e2e2", fnt_color="d9d9d9", size=300, text="placeholder"
) -> Image:
    color = ImageColor.getrgb(f"#{bg_color}")
    font_color = ImageColor.getrgb(f"#{fnt_color}")
    im_shape = (size, size)
    fnt_size = int(size / 10)
    txt = Image.new("RGB", im_shape, color)
    fnt = ImageFont.truetype("ubuntu-font/Ubuntu-B.ttf", fnt_size)

    d = ImageDraw.Draw(txt)
    txt_size = d.textsize(text, font=fnt)
    tw, th = txt_size

    txt_x = (300 - tw) / 2
    txt_y = (300 - th) / 2

    d.text((txt_x, txt_y), text="Jiaxin.im", font=fnt, fill=font_color)

    return txt


if __name__ == "__main__":
    placeholder = generate_placeholder()
    placeholder.show()
