import tensorflow as tf
import numpy as np

data = np.array(([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]), dtype=float)
data = data.reshape((1, 4, 4, 1))

Data = tf.placeholder(tf.float32, (None, 4, 4, 1))
conv1 = tf.layers.conv2d(
    inputs=Data,
    filters=1,
    kernel_size=[2, 2],
    strides=[1, 1],
    padding="same"
)
deconv1 = tf.layers.conv2d_transpose(
    inputs=conv1,
    filters=1,
    kernel_size=[2, 2],
    strides=[1, 1],
    padding="same"
)
cost = tf.reduce_mean(tf.pow(deconv1 - Data, 2))
optimizer = tf.train.AdamOptimizer(0.01).minimize(cost)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for epoch in range(1000):
        _, loss = sess.run([optimizer, cost], feed_dict={Data: data})
        if (epoch+1) % 100 == 0:
            print("# Epoch %d, loss= %.2f" % (epoch+1, loss))
    print(data.reshape((4, 4)))
    deconv1_run = sess.run(deconv1, feed_dict={Data: data})
    print(deconv1_run.reshape((4, 4)))



