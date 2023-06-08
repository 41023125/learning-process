from PIL import Image

def get_image_size(path):
    with Image.open(path) as img:
        return img.size

image_path = "1234.jpg"
image_size = get_image_size(image_path)
if image_size == (900, 1600):
    print(f"The image size is: {image_size}")
else : print(f"The image size is: {image_size}")
''''''
