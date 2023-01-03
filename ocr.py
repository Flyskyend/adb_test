import easyocr
import glob

path = 'trxf/trxf_12.jpg'
for filename in glob.glob(path):
    reader = easyocr.Reader(['ch_sim','en'], gpu=True) # this needs to run only once to load the model into memory
    result = reader.readtext(filename)
    print(result)

    for i in range(0, len(result)):
        print(i, result[i])
    
    print("===========================")

# from PIL import Image,ImageDraw
# image_path='XXXXXXXXXX.jpg'
# image=Image.open(image_path)
# draw = ImageDraw.Draw(image)
# draw.polygon([(902,1217),(1288,1215),(1288,1269),(903,1271)], outline=(255,0,0))
# image.show()