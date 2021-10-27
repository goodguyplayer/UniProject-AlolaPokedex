from os import listdir
from PIL import Image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in listdir("../pokemondata"):
        if "png" in i:
            file_in = "../pokemondata/" + i
            file_out = i.replace(".png", ".bmp")
            img = Image.open(file_in)
            helper = img.split()
            if len(img.split()) == 1:
                #r, g, b, a = img.split()
                #img = Image.merge("RGBA", (r, g, b, a)).convert("P", palette=Image.ADAPTIVE, colors=24)
                img = img.convert("RGB", colors=24)
                #img = changeColorDepth(im, 16).convert("P", palette=Image.ADAPTIVE, colors=8)
                img.save(file_out)
            else:
                img.save(file_out)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
