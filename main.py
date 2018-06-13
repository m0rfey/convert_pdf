# -*- coding: utf-8 -*-

import os
import math
from wand.image import Image, Color

from pytesseract import image_to_string, Output
from PIL import Image as image


PROJ_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_DIR = os.path.join(PROJ_DIR, 'PDF')

print(FILE_DIR)


class NewImege(Image):
    def brightness_contrast(self, brightness=0.0, contrast=0.0):
        slope=math.tan((math.pi * (contrast/100.0+1.0)/4.0))
        if slope < 0.0:
            slope=0.0
        intercept=brightness/100.0+((100-brightness)/200.0)*(1.0-slope)
        self.function("polynomial", [slope, intercept])


def get_files_by_path(prompt):
    abs_path = os.listdir(prompt)
    return abs_path


def convert_pdf_to_img(path, *args):
    """
    This function converting pdf file to image files
    :param path:
    :param args:
    :return:
    """
    for f in args:
        all_pages = Image(filename=f, resolution=500)
        for i, page in enumerate(all_pages.sequence):
            with NewImege(page) as img:
                img.format = 'png'

                img.background_color = Color('white')
                # Changed brightness and contrast
                img.brightness_contrast(-10.0, 0.0)
                img.alpha_channel = 'remove'

                image_filename = os.path.splitext(os.path.basename(f))[0]
                image_filename = '{}-{}.png'.format(image_filename, i)

                if not os.path.exists(os.path.join(path, 'img')):
                    os.makedirs(os.path.join(path, 'img'))

                image_filename = os.path.join(os.path.join(path, 'img'), image_filename)

                img.save(filename=image_filename)

    print('Convert pdf to img done!')


def convert_img_to_text(path):
    """
    This function reading text from image and save text to *.txt files
    :param path:
    :return:
    """
    imgs = get_files_by_path(os.path.join(path, 'img'))
    img_lst = []
    for file in imgs:
        if file.endswith('.png'):
            t = os.path.join(path, 'img', file)

            img_lst.append(t)

    for f in sorted(img_lst):
        print('Reading image:', f)
        txt_name = f.split('-')[0].split('/')[-1]
        img = image.open(f)
        # img.load()
        x = image_to_string(img, lang='rus')
        path_to_file = os.path.join(path, '.'.join([txt_name, 'txt']))

        if not os.path.isfile(path_to_file):
            f = open(path_to_file, 'w')
            f.close()

        with open(path_to_file, 'a') as file:
            file.write(x)
    print('Reading image files and saved text files done!')


def main(path):

    files = get_files_by_path(path)

    lst = []
    for file in files:
        if file.endswith('.pdf'):
            t = os.path.join(path, file)

            lst.append(t)

    convert_pdf_to_img(path, *lst)

    convert_img_to_text(path)


if __name__ == '__main__':
    print('Data sampling tool\n')
    # path = input('Enter path: ')
    main(FILE_DIR)