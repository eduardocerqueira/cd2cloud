# -*- coding: UTF-8 -*-

from mutagen import File

path = "/mnt/cloud/mp3/Paulo Moura & Yamandú Costa-El Negro Del Blanco/01.El Negro Del Blanco.mp3"
file = File(path)  # mutagen can automatically detect format and type of tags
artwork = file.tags['APIC:'].data  # access APIC frame and grab the image
with open('image.jpg', 'wb') as img:
    img.write(artwork)  # write artwork to new image
