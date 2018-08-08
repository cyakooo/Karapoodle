import os
import shutil

#元のデータセットを展開したディレクトリへのパス
original_poodle_dir = './img_data/original_poodle_dir'
original_karaage_dir = './img_data/original_karaage_dir'

#コピー先のディレクトリへのパス
train_poodle_dir = './img_data/train_poodle_dir'
validation_poodle_dir = './img_data/validation_poodle_dir'
test_poodle_dir = './img_data/test_poodle_dir'
train_karaage_dir = './img_data/train_karaage_dir'
validation_karaage_dir = './img_data/validation_karaage_dir'
test_karaage_dir = './img_data/test_karaage_dir'

"""
#最初の1000個のプードル画像をtrain_poodle_dirにコピー
fnames = ['poodle_{0:04d}.jpg'.format(i) for i in range(1, 1001)]
for fname in fnames:
    src = os.path.join(original_poodle_dir, fname)
    dst = os.path.join(train_poodle_dir, fname)
    shutil.copyfile(src, dst)

#次の500個のプードル画像をvalidation_poodle_dirにコピー
fnames = ['poodle_{0:04d}.jpg'.format(i) for i in range(1001, 1501)]
for fname in fnames:
    src = os.path.join(original_poodle_dir, fname)
    dst = os.path.join(validation_poodle_dir, fname)
    shutil.copyfile(src, dst)

#次の500個のプードル画像をtest_poodle_dirにコピー
fnames = ['poodle_{0:04d}.jpg'.format(i) for i in range(1501, 2001)]
for fname in fnames:
    src = os.path.join(original_poodle_dir, fname)
    dst = os.path.join(test_poodle_dir, fname)
    shutil.copyfile(src, dst)
"""

#最初の1000個のからあげ画像をtrain_karaage_dirにコピー
fnames = ['karaage_{0:04d}.jpg'.format(i) for i in range(1, 1001)]
for fname in fnames:
    src = os.path.join(original_karaage_dir, fname)
    dst = os.path.join(train_karaage_dir, fname)
    shutil.copyfile(src, dst)

#次の500個のからあげ画像をvalidation_karaage_dirにコピー
fnames = ['karaage_{0:04d}.jpg'.format(i) for i in range(1001, 1501)]
for fname in fnames:
    src = os.path.join(original_karaage_dir, fname)
    dst = os.path.join(validation_karaage_dir, fname)
    shutil.copyfile(src, dst)

#次の500個のからあげ画像をtest_karaage_dirにコピー
fnames = ['karaage_{0:04d}.jpg'.format(i) for i in range(1501, 2001)]
for fname in fnames:
    src = os.path.join(original_karaage_dir, fname)
    dst = os.path.join(test_karaage_dir, fname)
    shutil.copyfile(src, dst)
