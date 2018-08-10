import numpy as np
from PIL import Image
from keras import models
from keras.preprocessing.image import ImageDataGenerator

# 学習済みモデルの読み込み
model = models.load_model('karaage_poodle_small_2.h5')

# 画像ファイルの読み込み
print('画像ファイルのパスを入力してください。')
path = input()
img = Image.open(path)

images = []

# 画像データの前処理
img = img.convert("RGB")
img = img.resize((150, 150))
in_data = np.asarray(img)
images.append(in_data)

# numpy用の配列を作成
images = np.array(images)
images = images.astype('float32')  # floatに型変換
images /= 255.0  # 各画素値を正規化

# 結果の表示
prd = model.predict_classes(images, batch_size=1)
if prd == 1:
    print('トイプードル')
else:
    print('からあげ')