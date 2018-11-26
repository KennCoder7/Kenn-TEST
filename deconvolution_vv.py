import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def plot_axis(dataset, num, axis, time, s):
    if (axis > 0) & (axis < (3+1)):
        data = dataset[num][axis - 1]
        data = data.reshape([1, 40]).transpose()
        data = data[0:time]
        plt.plot(data+s)


data = 10 * np.random.random(size=120)
data = data.reshape((1, 3, 40, 1))

Data = tf.placeholder(tf.float32, (None, 3, 40, 1))
conv1 = tf.layers.conv2d(
    inputs=Data,
    filters=1,
    kernel_size=[3, 2],
    strides=[1, 1],
    padding="same"
)
deconv1 = tf.layers.conv2d_transpose(
    inputs=conv1,
    filters=1,
    kernel_size=[3, 2],
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
    deconv1_run = sess.run(deconv1, feed_dict={Data: data})
    for i in range(3):
        plot_axis(data, 0, i+1, 40, i*15)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel("time")
    plt.ylabel("axis 1,2,3")
    plt.title("original data")
    plt.show()
    for i in range(3):
        plot_axis(deconv1_run, 0, i+1, 40, i*15)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel("time")
    plt.ylabel("axis 1,2,3")
    plt.title("deconv data")
    plt.show()
    for i in range(3):
        plot_axis(data, 0, i+1, 40, i*15)
    for i in range(3):
        plot_axis(deconv1_run, 0, i+1, 40, i*15)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel("time")
    plt.ylabel("axis 1,2,3")
    plt.title("compare")
    plt.show()



