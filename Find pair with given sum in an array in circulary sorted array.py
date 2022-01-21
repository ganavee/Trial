a = [9, 15, 2, 3, 7]
length = len(a)
high = a[0]
high_index = 0
low = a[0]
i = 1
sum = 20
while(i<length):
	if(high<a[i] ):
		high = a[i]
		high_index = i
		i+=1;
		#print("hello")
	else:
		#print(a[0])
		break
if(high_index == (length-1)):
	low = 0
else:
	low = a[high_index + 1]
	low_index = high_index +1 
while(low_index!=high_index):
	tmp_sum = a[high_index]+a[low_index]
	if( tmp_sum == sum):
		print("Pair found ( %d,%d)",a[high_index],a[low_index])
		if(high_index == 0):
			high_index = length-1
		else:
			high_index -= 1
		if(low_index == (length-1)):
			low_index = 0
		else:
			low_index += 1
		#print("if high = %d low %d",a[high_index],a[low_index])
	elif(tmp_sum < sum):
		if(low_index == (length-1)):
			low_index = 0
		else:
			low_index += 1
		#print("elsif high = %d low %d",a[high_index],a[low_index])
	else:
		if(high_index == 0):
			high_index = length-1
		else:
			high_index -= 1
		#print(" else high = %d low %d",a[high_index],a[low_index])
		



