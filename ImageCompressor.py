# install pillow by typing pip install pillow in cmd prompt and press enter
from PIL import Image
import os

image = Image.open('naruto.jpg')

width,height=image.size
new_size = (width//2, height//2)

resized_img=image.resize(new_size)

resized_img.save('naruto_compressed.jpg')

original_img=os.path.getsize('naruto.jpg')

compressed_img=os.path.getsize('naruto_compressed.jpg')

print('original size: ',original_img)
print('compressed size ', compressed_img)
