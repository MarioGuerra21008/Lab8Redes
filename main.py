from PIL import Image

img = Image.new('RGB', (100, 100), color='red')

img.save('prueba_pillow.png')

img.show()
