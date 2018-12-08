import tensorflow as tf

a = tf.constant([0.1, 0.2, 0.3, 0.4], shape=[1, 4, 1])
b = tf.nn.softmax(a, axis=1)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print("# b = {}".format(sess.run(b)))
