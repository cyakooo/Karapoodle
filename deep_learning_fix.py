# coding by utf-8
from keras import models
from keras import layers
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# データセットのパス
train_dir = '/home/totsugekitai/workspace/mywork/karapoodle/karaage_poodle_small/train'
validation_dir = '/home/totsugekitai/workspace/mywork/karapoodle/karaage_poodle_small/validation'
test_dir = '/home/totsugekitai/workspace/mywork/karapoodle/karaage_poodle_small/test'

# CNNを構成
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
# CNNの上に分類器を追加
model.add(layers.Flatten())
model.add(layers.Dropout(0, 5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# 層の構成を表示
model.summary()

# モデルのコンパイル
model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4), metrics=['accuracy'])

# ImageDataGeneratorを使ってディレクトリから画像を読み込む
# 全ての画像を1/255でスケーリング
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,  # ターゲットディレクトリ
    target_size=(150, 150),  # 全ての画像のサイズを150×150に変更
    batch_size=32,  # バッチサイズ
    class_mode='binary'  # binary_crossentropyを使用するため二値のラベルが必要
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# バッチジェネレータを使ってモデルを適合
history = model.fit_generator(train_generator, steps_per_epoch=100, epochs=100, validation_data=validation_generator, validation_steps=50)

# モデルを保存
model.save('karaage_poodle_small_2.h5')

# 訓練時の損失値と正解率をプロット
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

# 正解率をプロット
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

# 損失値をプロット
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()