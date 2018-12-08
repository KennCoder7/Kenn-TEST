import tensorflow as tf

a = tf.constant([1, 2, 3, 1])
max = tf.argmax(a)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print(sess.run(max))