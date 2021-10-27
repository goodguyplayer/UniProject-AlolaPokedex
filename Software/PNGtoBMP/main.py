from os import listdir
from PIL import Image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in listdir("../pokemondata"):
        if "png" in i:
            file_in = "../pokemondata/" + i
            file_out = i.replace(".png", ".bmp")
            img = Image.open(file_in)
            if len(img.split()) == 4:
                r, g, b, a = img.split()
                img = Image.merge("RGB", (r, g, b))
                img.save(file_out)
            else:
                img.save(file_out)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
