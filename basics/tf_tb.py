import tensorflow as tf
 
# Build a graph
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

# Create the session object
sess = tf.Session()
 
#Run the graph within a session and store the output to a variable
output_c = sess.run(c)


File_writer = tf.summary.FileWriter('/home/ml/tensor_flow/basics/graphs',sess.graph)

#Print the output of node c
print(output_c)


 
#Close the session to free up some resources
sess.close()
