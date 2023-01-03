import easyocr
import glob

path = './*.jpg'
for filename in glob.glob(path):
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext(filename)
    print(result)

    for i in range(0, len(result)):
        print(i, result[i])
    
    print("===========================")

exit()