import string
import nltk
import numpy
import gensim
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities, utils, matutils
import math

stopset = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


f = open('./wikiArticles.txt', 'r')
txt = f.readlines()


#x = [[] for i in range(len(txt))]
#stemmed = [[] for i in range(len(txt))] 
stemmed = [[] for i in range(len(txt))] 
#lemw = []
count = 0 
ct = 0
#a = []
b = []



#string.punctuation = '!"#$%&\',.:;?@^_`~'
string.punctuation = '"#$%&\',.:;?@_`~'


for line in txt:
    for c in string.punctuation:
        line = line.replace(c,"") 
    
    tokens=word_tokenize(str(line.lower()))
    tokens = [w for w in tokens if not w in stopset]
    
    a = []
    for s in tokens:
        aa = filter(lambda x: x in string.printable, s)
        a. append(aa)
    
    
    x = []
    for item in a:
        lemw = wordnet_lemmatizer.lemmatize(item)
        x.append(lemw)  
      
        
    
    #stemmed = []
    for item in x:
        stemmed[count].append(stemmer.stem(item))
    count = count + 1


all_tokens = sum(stemmed, [])
    #print all_tokens
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
stemmed = [[word for word in stm if word not in tokens_once]
              for stm in stemmed]



dictionary = corpora.Dictionary(stemmed)
dictionary.save('./deerwester.dict') # store the dictionary, for future reference




corpus = [dictionary.doc2bow(stems) for stems in stemmed]
corpora.MmCorpus.serialize('./deerwester.mm', corpus) # store to disk, for later use



dictionary = corpora.Dictionary.load('./deerwester.dict')
corpus = corpora.MmCorpus('./deerwester.mm') # comes from the first tutorial, "From strings to vectors"



lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=5)





infile = open('./corpus_data.txt','r')
outfile = open('./corpus_data_n.txt', 'w')

infile1 = open('./model_ans.txt','r')
outfile1 = open('./model_ans_n.txt', 'w')


rp = {'-RRB-' : ')', '-LRB-' : '(', 'to the power of' : '^', 'minus' : '-', 'divided by' : '/', 'multiplied by' : '*', 'plus' : '+', 'theta' : 'O'}
for line in infile:
    for src, target in rp.iteritems():
        line = line.replace(src, target)
    outfile.write(line)
infile.close()
outfile.close()

rp = {'-RRB-' : ')', '-LRB-' : '(', 'to the power of' : '^', 'minus' : '-', 'divided by' : '/', 'multiplied by' : '*', 'plus' : '+', 'theta' : 'O'}
for line in infile1:
    for src, target in rp.iteritems():
        line = line.replace(src, target)
    outfile1.write(line)
infile1.close()
outfile1.close()


f = open('./sims.txt','a')
fa = open(r"./corpus_data_n.txt",'r')
fb = open(r"./model_ans_n.txt",'r')
faa = fa.readlines()
fbb = fb.readlines()

for line in faa:   
    
    
    for line1 in fbb:
        
        
        a1 = nltk.word_tokenize(line)

        a2 = nltk.word_tokenize(line1)

        b1=a1.split('.')
        b1.remove(b1[2])
        b1.remove(b1[2])
        c1='.'.join(b1)

        b2=a2.split('-')
        b22=b2[0].split('_')
        c2='.'.join(b22)
        
        if c1== c2:


           #print line
           a11 = line.split(c1)
           y1 = a11[1].replace('<STOP>', "")
           for c in string.punctuation:
               y1 = y1.replace(c,"")        
       

           clmf = []
           cstmmd = []
           ctkns=word_tokenize(str(y1.lower()))
           ctkns = [w for w in ctkns if not w in stopset]
           for item in ctkns:
               clmw = wordnet_lemmatizer.lemmatize(item)
               clmf.append(clmw)

           for item in clmf:
               cstmmd.append(stemmer.stem(item))
    
           c_vec = " ".join(cstmmd)
           cvec_bow = dictionary.doc2bow(c_vec.split())
           cvec_lsi = lsi[cvec_bow] 
           
        


           
           
           a22 = line1.split(c2)
           y2 = a22[1].replace('<STOP>', "")         
           for c in string.punctuation:
               y2 = y2.replace(c,"")        
       

              

           lmf = []
           stmmd = []
           tkns=word_tokenize(str(y2.lower()))
           tkns = [w for w in tkns if not w in stopset]

           for item in tkns:
               lmw = wordnet_lemmatizer.lemmatize(item)
               lmf.append(lmw)
   
      
           for item in lmf:
               stmmd.append(stemmer.stem(item))
    
           new_vec = " ".join(stmmd)
           vec_bow = dictionary.doc2bow(new_vec.split())
           vec_lsi = lsi[vec_bow]   
          
           sim = matutils.cossim(cvec_lsi, vec_lsi)
           
           print sim          
           
           

           
           
           f.write(str(sim))
           f.write("\n")
      
           
           ct = ct + 1
           print ct
           break

f.close()
fa.close()
fb.close()
        


     
           
           
           
           



