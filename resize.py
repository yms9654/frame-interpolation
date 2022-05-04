from PIL import Image
import glob


path = '/mnt/c/data/0420/05/*.jpg'
files = glob.glob(path)

for file in files:
    img = Image.open(file)
    img_resize = img.resize((int(img.width/2), int(img.height/2)))
    img_resize.save(file)