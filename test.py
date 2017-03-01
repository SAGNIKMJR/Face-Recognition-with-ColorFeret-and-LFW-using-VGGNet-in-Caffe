import numpy as np
import matplotlib.pyplot as plt
import csv
import caffe
import os
import sys
from os import walk
from PIL import Image
import PIL
from scipy import misc
from collections import Counter

plt.rcParams['figure.figsize'] = (5, 5)       #(10,10) 
plt.rcParams['image.interpolation'] = 'nearest' 
plt.rcParams['image.cmap'] = 'gray'  


caffe_root = '../'  
sys.path.insert(0, caffe_root + 'python')

test_dir='/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir'

def vis_square(data,i):
    
    

    data = (data - data.min()) / (data.max() - data.min())
    

    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 
               + ((0, 0),) * (data.ndim - 3))  

    data = np.pad(data, padding, mode='constant', constant_values=1)
    
    
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    plt.figure(i)
    plt.imshow(data)
    plt.axis('off')
    plt.hold(True)
    plt.show(block=True)

def VggNetClassific():
	if os.path.isfile('/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/run_27_2_snapshots/train_VGG19_iter_28000.caffemodel'):
    		print 'VGGNet found.'
	caffe.set_mode_cpu()

	model_def = '/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/VGG_ILSVRC_19_layers_deploy.prototxt'
	model_weights = '/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/run_27_2_snapshots/train_VGG19_iter_28000.caffemodel'

	net = caffe.Net(model_def,model_weights,caffe.TEST)  

	mu = np.load('/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/colfer_mean_npy.npy')
	mu = mu.mean(1).mean(1)  

	print 'mean-subtracted values:', zip('BGR', mu)

	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

	transformer.set_transpose('data', (2,0,1)) 
	transformer.set_mean('data', mu)            
	transformer.set_raw_scale('data', 255)     
	transformer.set_channel_swap('data', (2,1,0))  


	net.blobs['data'].reshape(50,3,224, 224)  
	testFiles=[]
    	for (dirpath, dirnames, filenames) in walk('/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir'):
		#testFiles.append('/home/sagnik/Desktop/ML Project/test_folder/')
		print dirnames
		break

	for i in dirnames:
		path='/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir/'+i
		for (dirpath, dirnames, filenames) in walk(path):
			pass
		for f in filenames:
				
				image = caffe.io.load_image(path+'/'+f)
				transformed_image = transformer.preprocess('data', image)
				plt.imshow(image)
				plt.axis('off')
				plt.show()

	
				net.blobs['data'].data[...] = transformed_image

	
				output = net.forward()

				output_prob = output['prob'][0] 
				print 'predicted class is:', output_prob.argmax()

				top_inds = output_prob.argsort()[::-1][:5]
				
				print 'probabilities and labels:'
				print(zip(output_prob[top_inds], top_inds))

				for layer_name, blob in net.blobs.iteritems():
	   				print layer_name + '\t' + str(blob.data.shape)

				for layer_name, param in net.params.iteritems():
	    				print layer_name + '\t' + str(param[0].data.shape), str(param[1].data.shape)


    
    				filters = net.params['conv1_1'][0].data
				vis_square(filters.transpose(0, 2, 3, 1),1)

				feat = net.blobs['conv1_1'].data[0, :36]
				vis_square(feat,2)

				feat = net.blobs['pool5'].data[0]
				vis_square(feat,3)

				feat = net.blobs['fc7'].data[0]
				plt.subplot(2, 1, 1)
				plt.plot(feat.flat)
				plt.subplot(2, 1, 2)
				_ = plt.hist(feat.flat[feat.flat > 0], bins=100)
				plt.show()

				feat = net.blobs['prob'].data[0]
				plt.figure(figsize=(15, 3))
				plt.plot(feat.flat)
				plt.show()

VggNetClassific()

