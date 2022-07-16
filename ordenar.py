
from PIL import Image

import os


folder = "C:/Users/usuario/desktop/"

if __name__ == "__main__":
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(folder + filename)

        if extension in [".pdf"]:
            pdfFolder = "C:/Users/usuario/Desktop/pdf/"
            os.rename(folder + filename, pdfFolder + filename)
