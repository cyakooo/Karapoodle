import os, shutil

base_dir = '/home/totsugekitai/workspace/mywork/karapoodle/karaage_poodle_small'
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

train_karaage_dir = os.path.join(train_dir, 'karaage')
os.mkdir(train_karaage_dir)
train_poodle_dir = os.path.join(train_dir, 'poodle')
os.mkdir(train_poodle_dir)

validation_karaage_dir = os.path.join(validation_dir, 'karaage')
os.mkdir(validation_karaage_dir)
validation_poodle_dir = os.path.join(validation_dir, 'poodle')
os.mkdir(validation_poodle_dir)

test_karaage_dir = os.path.join(test_dir, 'karaage')
os.mkdir(test_karaage_dir)
test_poodle_dir = os.path.join(test_dir, 'poodle')
os.mkdir(test_poodle_dir)