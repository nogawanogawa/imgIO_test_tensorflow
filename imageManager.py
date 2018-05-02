import tensorflow as tf

class imageManager:

    #　読み込み
    def read(filename):
        img = tf.read_file(filename)
        return tf.image.decode_png(img, channels=3)

    # 書き出し(jpeg)
    def write_jpg(data):
        sample = tf.image.encode_jpeg(data, format='rgb', quality=100)
        return sample

    # 書き出し(png)
    def write_png(data):
        sample = tf.image.encode_png(data)
        return sample
