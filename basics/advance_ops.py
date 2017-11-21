import tensorflow as tf

x = tf.constant([[1, 1, 1], [1, 1, 1]])

print (x)
tf.reduce_sum(x)  # 6
tf.reduce_sum(x, 0)  # [2, 2, 2]
tf.reduce_sum(x, 1)  # [3, 3]
tf.reduce_sum(x, 1, keep_dims=True)  # [[3], [3]]
y=tf.reduce_sum(x, [0, 1])  # 6
print (y)
