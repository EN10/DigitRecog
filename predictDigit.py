f = open('JSON.txt', 'r')
JSON = f.read()
f.close()

import json
digit = json.loads(JSON)

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

init = tf.initialize_all_variables()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess, "2LModel.ckpt")
  
    prediction=tf.argmax(y,1)
    #first value in list
    print (prediction.eval(feed_dict={x: [digit]}, session=sess)[0])