#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:06:22 2017

@author: saransh
"""

import tensorflow as tf
#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)
import numpy as np
def extraction_csv(b):
    import csv
    x=[]
    file=open(b)
    csv_file=csv.reader(file)
    for row in csv_file:
        x.append(row)
    return np.array(x)

 

def extraction_txt(a):
    file=open(a,'r')
    y=[]
    file1=file.readlines()
    for line in file1:
        line1=line.split('\n')
        y.append(list(line1[0]))
    return np.array(y)

train_x=extraction_csv('/home/saransh/sciENTsbank/Word_Overlap/train/feat_trtst.csv')
train_y=extraction_txt('/home/saransh/sciENTsbank/Word_Overlap/train/Accuracy_label.txt')
test_x=extraction_csv('/home/saransh/sciENTsbank/Word_Overlap/unseen_Questions/feat_trtst.csv')
test_y=extraction_txt('/home/saransh/sciENTsbank/Word_Overlap/unseen_Questions/Accuracy_label.txt')

n_nodes_hl1 = 5
n_nodes_hl2 = 5
n_nodes_hl3 = 5
display_step = 1
n_classes = 1
batch_size = 500

x = tf.placeholder('float', [None, 5])
y = tf.placeholder('float')

def neural_network_model(data):
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([5, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes])),}


    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']

    return output

def train_neural_network(x):
    
    prediction = neural_network_model(x)
    # OLD VERSION:
    #cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )
    # NEW:
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    
    hm_epochs = 30
    with tf.Session() as sess:
        
        # OLD:
        #sess.run(tf.initialize_all_variables())
        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            
            avg_cost = 0
            total_batch = int(len(train_x/batch_size))
            while i < len(train_x):
                
		       start = i
		       end = i+batch_size
		       batch_x = np.array(train_x[start:end])
		       batch_y = np.array(train_y[start:end])

		       _, c,p = sess.run([optimizer, cost,prediction], feed_dict={x: batch_x,
				                                              y: batch_y})
		       avg_cost += c / total_batch
                i+=batch_size
        # sample prediction
        label_value = batch_y
        estimate = p
        err = label_value-estimate
        print ("num batch:", total_batch)

        # Display logs per epoch step
        if epoch % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(avg_cost))
            print ("   ")
            for i in xrange(4):
                print ("label value:", label_value[i], \
                    "estimated value:", estimate[i])
            print ("   ")

    print ("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("Accuracy:", accuracy.eval({x: X_test, y: Y_test}))               
	            

        
	    
train_neural_network(x)

#data extraction



        
    
    
    
