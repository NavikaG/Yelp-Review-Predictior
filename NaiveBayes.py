import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords') 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import random
import csv




import sys

# print ("arg1" + (sys.argv[0]))
# print ("arg2" + (sys.argv[1]))
# print ("arg3" + (sys.argv[2]))



#do we need to be able to accept any input files? (specific names or input)
with open (sys.argv[1]) as json_file: #open ('data_test_wo_label_template.json') as json2_file :
	
	#load the data from the file into data0
	data0 = json.load(json_file)
	#print(data0[0])

with open (sys.argv[2]) as json_file2:	

	# IMPORTANT READS THE TEST FILE
	data2 = json.load(json_file2)

	
	
	# IMPORTANT READS THE TEST FILE
	# data2 = json.load(json2_file)
	
	#create a 'data' to train the data set and a 'data2' to test the data. For testing purposes we split the train data
	data1 = data0[10000:24576]
	# data2 = data0[1000:1010]
	# data= datas[0:10000]
	#first=data[1]

#print((data[0]['text']))


#create an int to keep track of test length
totalTest=0
#counts number of elements in test data
for e in (data2):
	totalTest = totalTest + 1

#create ints for all the below variables then traverse the data to update the values
total=0
one = 0
rate1 = []
two = 0
rate2 = []
three = 0
rate3 = []
four = 0
rate4 = []
five = 0
rate5 = []
#calculate the total number of entries, then calculate the number of entries with rating 1, 2, 3, 4, or 5.
for l in ((data1)):
	total = (total + 1)
	if (l['stars'] == 1 ):
		one = (one + 1)
		rate1.append(l)
	if (l['stars'] == 2 ):
		two = (two + 1)
		rate2.append(l)
	if (l['stars'] == 3 ):
		three = (three + 1)
		rate3.append(l)
	if (l['stars'] == 4 ):
		four = (four + 1)
		rate4.append(l)
	if (l['stars'] == 5 ):
		five = (five + 1)
		rate5.append(l)

# print(total)    
# print ("one: " + str(one))
# print ("two: " + str(two))
# print ("three: " + str(three))
# print ("four: " + str(four))
# print ("five: " + str(five))


data = data1
maximum = max(one, two, three, four, five)

def balance(maximum, rankNum, rateList):
	while rankNum < maximum:
		randomNum = random.randint(0, len(rateList) - 1)
		#print("rand " + str(randomNum))
		data.append(rateList[randomNum])
		rankNum = rankNum + 1
		#sample a new data with rank. How can we get the correct review??

balance(maximum, one, rate1)
balance(maximum, two, rate2)
balance(maximum, three, rate3)
balance(maximum, four, rate4)
balance(maximum, five, rate5)
#print(data)

one2 = 0
two2 = 0
three2 = 0
four2 = 0
five2 = 0

for d in ((data)):
	if (d['stars'] == 1 ):
		one2 = (one2 + 1)
	if (d['stars'] == 2 ):
		two2 = (two2 + 1)
	if (d['stars'] == 3 ):
		three2 = (three2 + 1)
	if (d['stars'] == 4 ):
		four2 = (four2 + 1)
	if (d['stars'] == 5 ):
		five2 = (five2 + 1)


# print ("one2: " + str(one2))
# print ("two2: " + str(two2))
# print ("three2: " + str(three2))
# print ("four2: " + str(four2))
# print ("five2: " + str(five2))

one = maximum
two = maximum
three = maximum
four = maximum
five = maximum

# print ("one: " + str(one))
# print ("two: " + str(two))
# print ("three: " + str(three))
# print ("four: " + str(four))
# print ("five: " + str(five))

total = one + two + three + four + five

# print(total)
# print(len(data))













#preprocessing

#create a string with all possible punctuations
punctuations = "~`!@#$%^&*()_-+={}[]|\\:;<>,.?/\"\'"
numbers = "0123456789"
#print(type(punctuations))

#traverse through the data
for x in (data):


	#make each text lower case
	x['text'] = x['text'].lower()
	#print(x['text'])


	#traverse through the characters in each text
	for y in x['text']:
		#remove punctuation
		if y in punctuations:
			 #relpace the puncutation with an empty string
			 x['text'] = x['text'].replace(y, "")
		if y in numbers:
			 #relpace the numbers with an empty string
			 x['text'] = x['text'].replace(y, "")


	stemmer = PorterStemmer()
	#create a list of all the stopwords
	words = stopwords.words('english')
	#tokenizes the text
	tokens = word_tokenize(x['text'])
	#traverse through the stopwords
	for z in tokens:

		#remove stopwords from text
		#replace the stopword in the text with a space to "remove" it
		if z in words:
			x['text'] = x['text'].replace(" " + z + " ", " ")

		x['text'] = x['text'].replace(" " + z + " ", " " + stemmer.stem(z) + " ")
		#print(z + " : " + stemmer.stem(z))


#print (data[0]['text'])


#print out the total and the total number of 1's, 2's, 3's, 4's, and 5's
# print(total)    
# print ("one: " + str(one))
# print ("two: " + str(two))
# print ("three: " + str(three))
# print ("four: " + str(four))
# print ("five: " + str(five))


# prob1 = ((one/total))
# prob2 = ((two/total))
# prob3 = ((three/total))
# prob4 = ((four/total))
# prob5 = ((five/total))

#calculate the probability of each rate in the entire train set
def probStar(rate):
  if (rate == 1):
    return (one/total)
  if (rate == 2):
    return (two/total)
  if (rate == 3):
    return (three/total)
  if (rate == 4):
    return (four/total)
  if (rate == 5):
    return (five/total)


# print ("one: " + str(one)+"/"+str(total) + "=" + str(probStar(1)))
# print ("two: " + str(two)+"/"+str(total)+ "=" + str(probStar(2)))
# print ("three: " + str(three)+"/"+str(total) + "=" + str(probStar(3)))
# print ("four: " + str(four)+"/"+str(total)+ "=" + str(probStar(4)))
# print ("five: " + str(five)+"/"+str(total)+ "=" + str(probStar(5)))


#pick target words and create a vocabulary
voca = []
vocabulary = []
for t in data:
	token = word_tokenize(t['text'])
	voca.extend(token)

voca = nltk.FreqDist(voca)
voca = voca.most_common(1000)
#print(type(voca))
for h in voca:
	a, b = h
	vocabulary.append(a)

# print(vocabulary)

# print(vocabulary)
# vocabulary = ["horrible", "love", "good", "bad"]
# "perfect", "awful", "slow", "avoid", "great" , "not worth", "incredible", "well", "superb", " professional", "best", "well", "genuine", "fun", "terrific", "fancy", "downhill", "flawless"]

# def heckProb(voc):
#   count=0
#   # if(storeP)
#   for i in data:

#   	#if it is in the review and the rating is the one passed in
#     if((voc in i['text'])):
#       count=count+1



#   return(count)


# horrible=heckProb(vocabulary[0])
# print(horrible)





#"fan", extremely, tremendous

#print(data[0]["text"])

#stores Probabilty of thing 
#storeP = [-1]*5[-1]*(length(vocablulary))

#print(storeP) 


#voc is word in vocablulary
# rate is the rating given
#finds probability of ratings if the text contains specific words
def Prob(voc, rate):
  count=0
  # if(storeP)
  for i in data:

  	#if it is in the review and the rating is the one passed in
    if((voc in i['text']) and  (i['stars']==rate)):
      count=count+1



  return(count/total)

#print(Prob("horrible", 4))
#print(data[0]['text'])
# print (vocabulary[0] in data[0]['text'])
# print (data[0]['stars'])
#print (probablity(vocabulary[0],1.0))



  

def P(rev): 

  #sum=probStar(rev['stars'])
  r=[0,0,0,0,0]
  #print("here")
  
  #for loop calulates probability of getting each rating given review
  for j in range(5):
  #
  	#sum=1

  	sum=probStar(j+1)

  	#loop calcultes the probabilty of getting each ratiting given the text
  	for i in vocabulary:
  		if (i in rev['text']):
  			sum=Prob(i, j+1)*sum
  	r[j]=sum

  # print(r)

  #find the highest probability
  final=max(r)
  
  # print(final)

  # print("here1")
  
  #figure out what rateing produced the highest probaibilty
  for k in range(5):
   # print("here2")

   #If the rating is the one with the highest probabilty
   if (r[k]==final):
   	# print("here3")


   	# print("our: " + str(k+1))
   	# print("actual: " + str(rev['stars']))
    
    #Our prediction of the review based on the highest probaility
   	return k+1


# print("our: " + str(P(data[1])))
# print("actual: " + str(data[1]['stars']))
    

# print(P(data[9]))

# test accuracy
# COME BACKKKKK
# acc=0
# for z in range(totalTest):

# 	if((P(data2[z])) == data2[z]['stars']):
# 		acc=acc+1

# print (str((acc/totalTest)*100)+"%")

  
# final=sort(P(1), P(2), P(3), P(4), P(5))
# print(final[4])


#Write to the CSV File
import csv
with open('predictions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Predictions"])
    
    
    for h in range(totalTest):
    	writer.writerow({float(P(data2[h]))})





