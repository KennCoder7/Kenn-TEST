import tensorflow as tf
import numpy as np


def Normalize(data):
    m = np.mean(data)
    mx = max(data)
    mn = min(data)
    return np.array([(float(i) - m) / (mx - mn) for i in data])


def variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, dtype=tf.float32)


data = np.array(([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]), dtype=float)
print(data.shape)
data = data.reshape((1, 4, 4, 1))
print(data.reshape((4, 4)))


Data = tf.placeholder(tf.float32, (None, 4, 4, 1))
Conv = tf.placeholder(tf.float32, (None, 4, 4, 1))
print(Data.shape)

# kernel = variable([2, 2, 1, 1])
# d_kernel = variable([2, 2, 1, 1])
# conv1 = tf.nn.conv2d(
#     input=Data,
#     filter=kernel,
#     strides=[1, 1, 1, 1],
#     padding="SAME"
# )
# deconv1 = tf.nn.conv2d_transpose(
#     value=conv1,
#     filter=d_kernel,
#     output_shape=[1, 4, 4, 1],
#     strides=[1, 1, 1, 1],
#     padding="SAME"
# )
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
    # print(sess.run(kernel).shape)
    for epoch in range(2000):
        _, loss = sess.run([optimizer, cost], feed_dict={Data: data})
        if (epoch+1) % 100 == 0:
            print("# Epoch %d, loss= %.2f" % (epoch+1, loss))
    print(data.reshape((4, 4)))
    # conv1_run = sess.run(conv1, feed_dict={Data: data})
    # print(conv1_run.reshape((4, 4)))
    deconv1_run = sess.run(deconv1, feed_dict={Data: data})
    print(deconv1_run.reshape((4, 4)))


# Epoch 50, loss= 0.45
# Epoch 100, loss= 0.12
# Epoch 150, loss= 0.05
# Epoch 200, loss= 0.02
# Epoch 250, loss= 0.01
# Epoch 300, loss= 0.01
# Epoch 350, loss= 0.00
# Epoch 400, loss= 0.00
# Epoch 450, loss= 0.00
# Epoch 500, loss= 0.00
# Epoch 550, loss= 0.00
# Epoch 600, loss= 0.00
# Epoch 650, loss= 0.00
# Epoch 700, loss= 0.00
# Epoch 750, loss= 0.00
# Epoch 800, loss= 0.00
# Epoch 850, loss= 0.00
# Epoch 900, loss= 0.00
# Epoch 950, loss= 0.00
# Epoch 1000, loss= 0.00
# [[1. 2. 3. 4.]
#  [2. 3. 4. 5.]
#  [3. 4. 5. 6.]
#  [4. 5. 6. 7.]]
# [[1.0676701 2.014852  2.96477   3.9848788]
#  [2.0148597 3.0723863 4.0078125 5.036436 ]
#  [2.9647856 4.0078125 4.9432383 5.986412 ]
#  [3.9848976 5.0364294 5.9864044 6.9977555]]
