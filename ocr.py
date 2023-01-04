import easyocr
import glob
from PIL import Image,ImageDraw

path = 'trxf/trxf_*.jpg'
for filename in glob.glob(path):
    reader = easyocr.Reader(['ch_sim','en'], gpu=True) # this needs to run only once to load the model into memory
    result = reader.readtext(filename)
    print(result)

    image=Image.open(filename)
    draw = ImageDraw.Draw(image)
    for i in range(0, len(result)):
        draw.polygon([tuple(result[i][0][0]), tuple(result[i][0][1]), tuple(result[i][0][2]), tuple(result[i][0][3])], outline=(255,0,0))
        print(i, result[i])
    
    # image.show()
    image.save(filename.split('/')[1].split('.')[0] + "_res.jpg")
    
    print("===========================")
