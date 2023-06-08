from PIL import Image, ImageDraw

def draw_red_box(image_path, left, top, width, height, output_path):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        draw.rectangle((left, top, left + width, top + height), outline='red', width=3)
        img.save(output_path)
image_path = "1234.jpg"
output_path = "frame.jpg"
x1 = 230
y1 = 1950
w1 = 160
h1 = 45
x2 = 552
y2 = 1960
w2 = 93
h2 = 45

# draw_red_box(image_path, x1, y1, w1, h1, output_path)
# draw_red_box(image_path, x2, y2, w2, h2, output_path)