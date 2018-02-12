import numpy # for standard deviation

hosts = ['github.com', 'yahoo.in', 'sublime.com', 'english.gov.cn', 'facebook.com', \
          'nationsonline.org', 'whitehouse.gov' ,  'hongkiat.com', 'ny.gov', 'test.com',   \
         'messenger.com', 'mit.edu', 'cmu.edu', 'ctrip.com',   'medium.com', 'yahoo.com', 'yahoo.ru', \
         'coindesk.com', 'soundcloud.com', 'britebart.com',  'sogou.com', 'pustakalaya.org', 'tmall.com',\
         'stackoverflow.com', 'naver.com', 'olenepal.com' , 'howard.edu'  , 'google.com', ]

	# get values from dictionary reverse and print the values in table
def print_result(mydic, avg_sd):
	keys = mydic.keys()
	keys.sort(reverse = True)
	print 'Ranking', "\t", 'Domain Name', "\t", avg_sd
	for i in range(1, 6):
		print i, "\t", mydic[keys[i -1]], "\t", keys[i -1]

    

# checks if the string in a line is a float delay
def is_float(string):
  try:
    return float(string) 
  except ValueError:  # String is not a number
    return False

# gets the average of the delays in a line
def get_average(lst):
    c = 0 #count
    total = 0
    for item in lst:
        if is_float(item) and is_float(item) > 0:
            total += float(item)
            c += 1
    return (total /c)



 # calculating the total average   
def calculate_total_avg_sd(file): # name in case of traceroute and ip in case of tcptraceroute when second argument has just ip
	myfile = open(file, 'r')
	total = 0
	count = 0
	my_lst = [] # list of the average of the packets
	for line in myfile:
		myline = line.split()
		if 'open' in line:     
			count += 1
			current_avg = get_average(myline)
			total += current_avg
			my_lst.append(current_avg)
	final_avg = total / count
	print "The final average is ", final_avg
	sd = numpy.std(my_lst)
	print "The standard deviation is", sd
	myfile.close()
	return (final_avg, sd)

calculate_total_avg_sd('olenepal.com.txt')


#driver of the program 
avg_dic = {}
avg_4sd_dic = {}
for host in hosts:
    print host
    filename = host + '.txt'
    avg, sd = calculate_total_avg_sd(filename)
    avg_4sd = avg + 4 * sd
    # storing the average and avg sd in a dictionary
    avg_dic[avg] = host
    avg_4sd_dic[avg_4sd] =  host
    
print avg_4sd_dic

print "The result for Average is: "
print_result(avg_dic, 'Average')
print_result(avg_4sd_dic, 'Average + 4 * Standard Deviation')
print_result

    












