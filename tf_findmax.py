import tensorflow as tf
import numpy as np
import random

aa = []
for i in range(42):
    aa.append(random.randint(11, 100))
a = np.array(aa)
a = a.reshape(7, 6)
A = tf.constant(a)
B = tf.reshape(A, [-1, 2, 3])  # 变成7个2*3
c = tf.argmax(B, 2)  # 按第二个维度求最大值所在的位置,7个样本，每个样本对应2个位置（3个中最大的位置）

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(A))
    print(sess.run(B))
    print(sess.run(B).shape)
    print(sess.run(c))
    print(sess.run(c).shape)
