from PIL import Image
def resize_image(image, new_width):
    width, height = img.size
    aspect_ratio = new_width/width
    new_height = aspect_ratio * height
    return image.resize((new_width, int(new_height)))

def image_to_ascii(image, ascii_pixels: str):
    width, height = image.size
    final_str = ""
    for h in range(height):
        if h != 0:
            final_str = final_str + "\n"
        for w in range(width):
            r, g, b = map(int, image.getpixel((w, h)))
            if (r,g,b) == (0,0,0):
                ascii_letter = " "
            else:
                ascii_letter = ascii_pixels[((r + g + b) // 3) % len(ascii_pixels)]
            final_str = final_str + ascii_letter
    return final_str


ascii_pixels = "@%#*+◉•:."
img = Image.open('Fauna.jpg')
#does not work for images with too much colour
img_2 = Image.open("Mika Pikazo Art.jpg")

resized_image = resize_image(img, 300)
print(image_to_ascii(resized_image, ascii_pixels))

