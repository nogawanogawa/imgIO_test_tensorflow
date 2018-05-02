import sys
import tensorflow as tf
import imageManager as im

imMgr = im.imageManager

### READのFlowを定義
image = imMgr.read("sample.png")

### WRITEのFlowを定義
output = imMgr.write_png(image)

### Flowの実行
sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(tf.global_variables_initializer())
tf.train.start_queue_runners(sess)
x = sess.run(output)

### File書き込み
filepath="./output/000.png"
with open(filepath, 'wb') as fd:
    fd.write(x)
