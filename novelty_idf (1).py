import re

import math
line=''
s=set()
i = 0

w11 = []
f1 = open(r'./Student_Answers.txt',"r")
lines=f1.readlines()




lines = [line.lower() for line in lines]
with open('listTogether1.txt', 'w') as out:
     out.writelines(lines)

out.close()













filename = './Student_Answers.txt'

word_list = re.split('\s+', file(filename).read().lower())
print 'Words in text:', len(word_list)
#punctuation = re.compile(r'[-.?!,":;]')
punctuation = re.compile(r'[][.?!,":;()|0-9]')
#w1=[]

word_list = [punctuation.sub("", word) for word in word_list] 




s = set(word_list)
s = sorted(s)


ff1 = open('listTogether1.txt', 'r')
f = ff1.readlines()


  

i=0
ct=0
tf_line=''          
doc_counts=[]       
for term in s: #takes each term in the set 
    doc_counts.append(0)
   
    for at in f: # counts the no of times "term" is encountered in each doc
        
        
        ct=at.count(str(term)) #counts the no. of times "term" is present in the file
        #print ct
         
        if (ct>0):              #counts no of docs in which 
           doc_counts[i]+=1    #this "term" is found
    i+=1
    
print doc_counts

idf=[]  #inverse document frequency      

total_docs=len(f)
print total_docs



i=0

for doc_count in doc_counts:    #takes the 1st doc count
    #if doc_count==0:
    #   idf.append(0)
    #else:
    idf.append(math.log((total_docs + 1)/(doc_count+0.5))) #calculates idf for each "term"
    
    i+=1
#print idf




fdoc="./novelty_idf.csv"
outfile=open(fdoc,"a")

i=0
for term in s:
    final_line=term+','+str(round(idf[i],2))+','+'\n'
    
   
    outfile.write(final_line)
   
    i+=1


print "DONE"
























