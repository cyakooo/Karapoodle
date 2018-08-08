import os
import glob

path = "./img_data/original_karaage_dir"
files = glob.glob(path + '/*.jpg')

for i, f in enumerate(files, 1):
    os.rename(f, os.path.join(path, 'karaage_{0:04d}.jpg'.format(i)))