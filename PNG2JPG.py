from PIL import Image
import cv2 as cv
import os

def png2jpg(png_path):
    img = cv.imread(png_path, 0)
    w, h = img.shape[::-1]
    infile = png_path
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    img = img.resize((int(w), int(h)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=90)
            os.remove(png_path)
        else:
            img.convert('RGB').save(outfile, quality=90)
            os.remove(png_path)
        return outfile
    except Exception as e:
        print("PNG2JPG ERROR！！！", e)

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            # print(cur_path)
            filename, ext = os.path.splitext(file)
            if ext == ".png":
                print("PNG:" + cur_path)
                png2jpg(cur_path)
            all_files.append(file)

    return all_files
