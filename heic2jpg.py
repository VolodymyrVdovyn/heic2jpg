from PIL import Image
import pyheif
import os
import shutil
import re


path = input('Absolute path to directory: ')


def create_dir(name):
    """Create dir"""
    d = os.path.join(path, name)
    if os.path.exists(d):
        if not os.path.isdir(d):
            os.remove(d)
            os.mkdir(d)
    else:
        os.mkdir(d)


create_dir('video')
video = os.path.join(path, 'video')
create_dir('photo')
photo = os.path.join(path, 'photo')

pattern = r'.\w+$'

lst = os.listdir(path)
for i in lst:
    inp = os.path.join(path, i)
    file = re.search(pattern, i).group(0).lower()
    if file in ['.mov', '.mp4']:
        print(i)
        outp = os.path.join(video, i)
        shutil.move(inp, outp)
    elif file in ['.png', '.jpg', '.jpeg']:
        print(i)
        outp = os.path.join(photo, i)
        shutil.move(inp, outp)
    elif file in ['.heic', 'heif']:
        print(i)
        outp = photo + '/' + i[:-5] + '.jpg'
        heif_file = pyheif.read_heif(inp)
        image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
        image.save(outp, "JPEG")

        """Save heic files in new dir"""
        make_dir('heic')
        heic = os.path.join(path, 'heic')
        outp = os.path.join(heic, i)
        shutil.move(inp, outp)

        """Or delete heic files"""
        # os.remove(inp)
