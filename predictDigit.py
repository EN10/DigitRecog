f = open('JSON.txt', 'r')
JSON = f.read()
f.close()

import json
digit = json.loads(JSON)

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

init = tf.initialize_all_variables()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess, "model.ckpt")
  
    prediction=tf.argmax(y,1)
    #first value in list
    print (prediction.eval(feed_dict={x: [digit]}, session=sess)[0])