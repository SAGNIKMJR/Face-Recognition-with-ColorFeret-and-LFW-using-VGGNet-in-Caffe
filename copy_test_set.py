import time
import os

urlsfile = open('/home/abc-5/Downloads/test1.txt', "rb", 0)
#filetrain2 = open("/home/sagnik/Downloads/train2.txt",'w')
#fileval = open("/home/sagnik/Downloads/val1.txt",'w')
#filetrain2.write('jbjjbjbjb')
#filetrain2.close()
#filetrain = open("/home/sagnik/Downloads/train1.txt",'w')
#filetest = open("train1.txt",'w')
first_line='zzzz'
os.makedirs('/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir')
counter1=0
for line1 in urlsfile:
	
	
	print 'h'
	if line1[-4:]==first_line:
		#print('cont')
		#time.sleep(1)
		continue
	else:
		counter2=0
		'''for i in line1:
			if i=='/':
				counter2=counter2+1
			if counter2==5:'''
		os.makedirs('/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir/'+line1[34:39])	
	count=0
	print line1
 	first_line=line1[-4:]
	print ('first line'+first_line)
	urlsfile2 = open('/home/abc-5/Downloads/test1.txt', "rb", 0)
	for line2 in urlsfile2:
		print line2
		print line1
		print(line2[-4:] == line1[-4:])
		#time.sleep(1)
		if line2[-4:] == line1[-4:] :
			counter3=0
			for j in line2:
				if j==' ':
					break
				else:	
					counter3=counter3+1
			os.system('cp '+line2[0:counter3]+' '+'/home/abc-5/Desktop/DOP17_SK_SM/Run2_22_2/testdir/'+line1[34:39])
			print 'yo'
			count=count+1
			print count
			#time.sleep(1000)
		#else:
	print count
	#time.sleep(1)		
	'''count_train=int(count*0.7)
	print ('ctr'+str(count_train))
	count_val=count-count_train
	counter=1
	print 'no'
	urlsfile3 = open('/home/sagnik/Downloads/train.txt', "rb", 0)
	for line3 in urlsfile3:
		print 'no'
		
		if (counter<=count_train and line3[-4:-1]==line1[-4:-1]):
			print 'no'
			#time.sleep(1)
			filetrain.write(line3)
			counter=counter+1
			print ('cntr'+str(counter))
		elif (counter>count_train and counter<=count and line3[-4:-1]==line1[-4:-1]):
			print 'yo'
			#time.sleep(1)
			fileval.write(line3)
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
	#	break'''
#filetrain.close()
#fileval.close()

