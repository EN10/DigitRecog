from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])
N = 100
w2 = tf.Variable(tf.truncated_normal([784, N], stddev=0.1))
b2 = tf.Variable(tf.zeros([N]))
y2 = tf.nn.relu(tf.matmul(x, w2) + b2)
w = tf.Variable(tf.truncated_normal([N, 10], stddev=0.1))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(y2, w) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    save_path = saver.save(sess, "2LModel.ckpt")