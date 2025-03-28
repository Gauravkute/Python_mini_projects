#pip install ascii-magic
#pip install pillow

from ascii_magic import AsciiArt
from PIL import ImageEnhance

my_art = AsciiArt.from_image('cat.jpg')  # take image
my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2) #enhance the image
my_art.to_terminal() #show it in terminal