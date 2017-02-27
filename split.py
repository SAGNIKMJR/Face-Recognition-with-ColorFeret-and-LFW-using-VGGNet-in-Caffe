import time

urlsfile = open('/home/abc-5/Downloads/train.txt', "rb", 0)
#filetrain2 = open("/home/sagnik/Downloads/train2.txt",'w')
fileval = open("/home/abc-5/Downloads/val1.txt",'w')
#filetrain2.write('jbjjbjbjb')
#filetrain2.close()
filetrain = open("/home/abc-5/Downloads/train1.txt",'w')
filetest = open("/home/abc-5/Downloads/test1.txt",'w')
#filetest = open("train1.txt",'w')
first_line='zzz'
counter1=0
for line1 in urlsfile:
	print 'h'
	if line1[-4:-1]==first_line:
		#print('cont')
		#time.sleep(1)
		continue	
	count=0
	print line1
 	first_line=line1[-4:-1]
	print ('first line'+first_line)
	urlsfile2 = open('/home/abc-5/Downloads/train.txt', "rb", 0)
	for line2 in urlsfile2:
		print line2
		print line1
		print(line2[-4:-1] == line1[-4:-1])
		#time.sleep(1)
		if line2[-4:-1] == line1[-4:-1] :
			print 'yo'
			count=count+1
			print count
			#time.sleep(1000)
		#else:
	print count
	#time.sleep(1)		
	count_train=int(count*0.7)
	#print count_train
	#time.sleep(2)
	print ('ctr'+str(count_train))
	count_val=int(0.15*count)
	if count_val==0:
		count_val=1
	#print count_val
	#time.sleep(2)
	count_test=count-(count_train+count_val)
	#print count_test
	#time.sleep(2)	
	counter=1
	print 'no'
	urlsfile3 = open('/home/abc-5/Downloads/train.txt', "rb", 0)
	for line3 in urlsfile3:
		print 'no'
		
		if (counter<=count_train and line3[-4:-1]==line1[-4:-1]):
			print 'no'
			#time.sleep(1)
			filetrain.write(line3)
			counter=counter+1
			print ('cntr'+str(counter))
		elif (counter>count_train and counter<=(count-count_test) and line3[-4:-1]==line1[-4:-1]):
			print 'yo'
			#time.sleep(1)
			fileval.write(line3)
			counter=counter+1
		elif (counter>(count-count_test) and counter<=count and line3[-4:-1]==line1[-4:-1]):
			print 'yo'
			#time.sleep(1)
			filetest.write(line3)
			counter=counter+1
		#else:
			#print 'break'
			#time.sleep(5)
			#break

		#if line2[-4:-1] is line1[-4:-1] :
		#	count=count+1
		#else:
		#	break
	#counter1=counter1+1
	#if counter1==3:
	#	break
filetrain.close()
fileval.close()
filetest.close()
