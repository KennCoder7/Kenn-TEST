import tensorflow as tf
import numpy as np
import pandas as pd
import math

labels = np.array(['Cat', 'Dog', 'Fish'])
print(pd.get_dummies(labels))
labels_onehot = np.asarray(pd.get_dummies(labels))
print(labels_onehot)

logits = np.array(([[0.7, 0.3, 0.1], [0.3, 0.9, 0.1], [0.1, 0.1, 0.8]]))
print(logits)

cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=labels_onehot)
loss = tf.reduce_sum(cross_entropy)

softmax_logits = tf.nn.softmax(logits)


def softmax_cross_entropy(labels, logits):
    cross_entropy_all = np.array([])
    for m in range(len(labels)):
        cross_entropy = 0
        for n in range(len(labels[0])):
            cross_entropy += math.log(logits[m][n]) * float(labels[m][n])
        cross_entropy_all = np.append(cross_entropy_all, -cross_entropy)
    return cross_entropy_all


with tf.Session() as sess:
    print("tf.nn.softmax_cross_entropy_with_logits_v2", sess.run(cross_entropy))
    # print("loss = ", sess.run(loss))
    real_softmax_logits = sess.run(softmax_logits)
    print("softmax_cross_entropy", softmax_cross_entropy(labels_onehot, real_softmax_logits))


