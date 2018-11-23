import tensorflow as tf

train_X = 1.0
train_Y = 2.0

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
k = tf.Variable(0.0, name="x")
loss = tf.abs(k * X - Y)
train_op = tf.train.GradientDescentOptimizer(learning_rate=0.3).minimize(loss)
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for epoch in range(20):
        _, _k, _loss = sess.run([train_op, k, loss], feed_dict={X: train_X, Y: train_Y})
        print("Epoch: %d | k = %f | loss = %f" % (epoch+1, _k, _loss))
