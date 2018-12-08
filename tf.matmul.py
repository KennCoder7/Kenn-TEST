import tensorflow as tf

# a_2d = tf.constant([1]*6, shape=[2, 3])
# b_2d = tf.constant([2]*12, shape=[3, 4])
# c_2d = tf.matmul(a_2d, b_2d)
# a_3d = tf.constant([1]*12, shape=[2, 2, 3])
# b_3d = tf.constant([2]*24, shape=[2, 3, 4])
# c_3d = tf.matmul(a_3d, b_3d)
# a_4d = tf.constant([1]*24, shape=[2, 2, 2, 3])
# b_4d = tf.constant([2]*48, shape=[2, 2, 3, 4])
# c_4d = tf.matmul(a_4d, b_4d)
#
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     print("# {}*{}={} \n{}".
#           format(a_2d.eval().shape, b_2d.eval().shape, c_2d.eval().shape, c_2d.eval()))
#     print("# {}*{}={} \n{}".
#           format(a_3d.eval().shape, b_3d.eval().shape, c_3d.eval().shape, c_3d.eval()))
#     print("# {}*{}={} \n{}".
#           format(a_4d.eval().shape, b_4d.eval().shape, c_4d.eval().shape, c_4d.eval()))

# a_2d = tf.constant([1]*6, shape=[2, 3])
# b_2d = tf.constant([2]*6, shape=[2, 3])
# c_2d = tf.multiply(a_2d, b_2d)
# a_3d = tf.constant([1]*12, shape=[2, 2, 3])
# b_3d = tf.constant([2]*12, shape=[2, 2, 3])
# c_3d = tf.multiply(a_3d, b_3d)
# a_4d = tf.constant([1]*24, shape=[2, 2, 2, 3])
# b_4d = tf.constant([2]*24, shape=[2, 2, 2, 3])
# c_4d = tf.multiply(a_4d, b_4d)
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     print("# {}*{}={} \n{}".
#           format(a_2d.eval().shape, b_2d.eval().shape, c_2d.eval().shape, c_2d.eval()))
#     print("# {}*{}={} \n{}".
#           format(a_3d.eval().shape, b_3d.eval().shape, c_3d.eval().shape, c_3d.eval()))
#     print("# {}*{}={} \n{}".
#           format(a_4d.eval().shape, b_4d.eval().shape, c_4d.eval().shape, c_4d.eval()))


a_2d = tf.constant([1]*6, shape=[2, 3])
k = tf.constant(2)
l = tf.constant([2, 3, 4])
b_2d_1 = tf.multiply(k, a_2d)  # tf.multiply(a_2d, k) is also ok
b_2d_2 = tf.multiply(l, a_2d)  # tf.multiply(a_2d, l) is also ok
a_3d = tf.constant([1]*12, shape=[2, 2, 3])
b_3d_1 = tf.multiply(k, a_3d)  # tf.multiply(a_3d, k) is also ok
b_3d_2 = tf.multiply(l, a_3d)  # tf.multiply(a_3d, l) is also ok
a_4d = tf.constant([1]*24, shape=[2, 2, 2, 3])
b_4d_1 = tf.multiply(k, a_4d)  # tf.multiply(a_4d, k) is also ok
b_4d_2 = tf.multiply(l, a_4d)  # tf.multiply(a_4d, l) is also ok
#
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    print("# {}*{}={} \n{}".
          format(k.eval().shape, a_2d.eval().shape, b_2d_1.eval().shape, b_2d_1.eval()))
    print("# {}*{}={} \n{}".
          format(l.eval().shape, a_2d.eval().shape, b_2d_2.eval().shape, b_2d_2.eval()))
    print("# {}*{}={} \n{}".
          format(k.eval().shape, a_3d.eval().shape, b_3d_1.eval().shape, b_3d_1.eval()))
    print("# {}*{}={} \n{}".
          format(l.eval().shape, a_3d.eval().shape, b_3d_2.eval().shape, b_3d_2.eval()))
    print("# {}*{}={} \n{}".
          format(k.eval().shape, a_4d.eval().shape, b_4d_1.eval().shape, b_4d_1.eval()))
    print("# {}*{}={} \n{}".
          format(l.eval().shape, a_4d.eval().shape, b_4d_2.eval().shape, b_4d_2.eval()))
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     print("# c_2d_1 shape:{} \n{}".format(c_2d_1.eval().shape, c_2d_1.eval()))
#     print("# c_2d_2 shape:{} \n{}".format(c_2d_2.eval().shape, c_2d_2.eval()))
#     print("# c_3d_1 shape:{} \n{}".format(c_3d_1.eval().shape, c_3d_1.eval()))
#     print("# c_3d_2 shape:{} \n{}".format(c_3d_2.eval().shape, c_3d_2.eval()))
#     print("# c_4d_1 shape:{} \n{}".format(c_4d_1.eval().shape, c_4d_1.eval()))
#     print("# c_4d_2 shape:{} \n{}".format(c_4d_2.eval().shape, c_4d_2.eval()))


# a_2d = tf.constant([1]*6, shape=[2, 3])
# d_2d_1 = tf.reduce_sum(a_2d, axis=0)
# d_2d_2 = tf.reduce_sum(a_2d, axis=1)
# a_3d = tf.constant([1]*12, shape=[2, 2, 3])
# d_3d_1 = tf.reduce_sum(a_3d, axis=1)
# d_3d_2 = tf.reduce_sum(a_3d, axis=2)
# a_4d = tf.constant([1]*24, shape=[2, 2, 2, 3])
# d_4d_1 = tf.reduce_sum(a_4d, axis=2)
# d_4d_2 = tf.reduce_sum(a_4d, axis=3)
#
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     print("# a_2d 行累加得到shape:{}\n{}".format(d_2d_1.eval().shape, d_2d_1.eval()))
#     print("# a_2d 列累加得到shape:{}\n{}".format(d_2d_2.eval().shape, d_2d_2.eval()))
#     print("# a_3d 行累加得到shape:{}\n{}".format(d_3d_1.eval().shape, d_3d_1.eval()))
#     print("# a_3d 列累加得到shape:{}\n{}".format(d_3d_2.eval().shape, d_3d_2.eval()))
#     print("# a_4d 行累加得到shape:{}\n{}".format(d_4d_1.eval().shape, d_4d_1.eval()))
#     print("# a_4d 列累加得到shape:{}\n{}".format(d_4d_2.eval().shape, d_4d_2.eval()))