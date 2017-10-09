#import stopwords
import nltk
import string
import os
import math


from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stopset = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


fa=open('./Student_Answers.txt','r')
fb=open('./Reference_Answers.txt','r')
faa=fa.readlines()
fbb=fb.readlines()

xy =[[0 for i in range(5)] for j in range(4969)]
jcc = []
#print xy
count = 0
#stemmed = [[] for i in range(len(faa))]
#stemmed1 = [[] for i in range(len(fbb))]
#stemmed = []
#stemmed1 = []
cstmmd = []
stmmd = []
lmf = []; clmf = []; 
lemw = []
count = 0 
ct = 0
a = []
am = []
b = []


def remov_idf(word):
    import csv
    pp=0
    f=open('./idf_table.csv')
    csv_f=csv.reader(f)
    for row in csv_f:
        if word in row:
           pp=row[1]
           break
    return round((float(pp)),2)


def jc(st1, st2, count):
    t = list(set(st1) & set(st2))
    #t = (set(stemmed) & set(stemmed1))
    #print t
    t1 = len(t)

    #print stemmed
    #print set(stemmed)
    #print stemmed1
    #print set(stemmed1)

    u = list(set(st1) | set(st2)) 
    t2 = len(u)
    #jcc.append[count] = float(t1)/float(t2)
    jcc = float(t1)/float(t2)
    #print jc[
    return round(jcc, 2)
    

def swo(st1, st2, count):
    t = list(set(st1) & set(st2))
    t1 = len(t)
    #print t1
    u = list(set(st2))
     
    t2 = len(u)
    #print t2
    #swo.append[count] = float(t1)/float(t2)
    swow = float(t1)/float(t2)
    return round(swow, 2)

def idfo(st1, st2, count):
    idff = 0
    t = list(set(st1) & set(st2))
    #print t
    for i in t:
        idf = remov_idf(i)
        idff = idff + idf
    #print idff
    t1 = len(t)
    u = list(set(st2)) 
    t2 = len(u)
    idfof = (float(t1)/float(t2)) * idff
    return round(idfof, 2)


def novelty_idf(word):
    import csv
    pp=0
    f=open('./novelty_idf.csv')
    csv_f=csv.reader(f)
    for row in csv_f:
        if word in row:
           pp=row[1]
           break
    return round((float(pp)),2)



def tf_idf(st1, st2, count):
    t = list(set(st1) & set(st2))
    fmul = 0
    for term in t:
        ct1 = st1.count(term)
        ct2 = st2.count(term)
        ct3 = novelty_idf(term)
        fic = (math.log(ct1 + 1)) * (math.log(ct2 + 1)) * ct3
        fmul = fmul + fic
    return round((float(fmul)),2)

def phro(st1, st2, count):

    print st1
    print st2
    st11 = " ".join(st1)
    st22 = " ".join(st2)
    print st11
    print st22
    fk=open('./fcorpus.txt','w')
    fl=open('./fmodel.txt','w')
    fk.write(st11)
    fl.write(st22)
    fk.close()
    fl.close()
    os.system("perl txt_simi2.pl fcorpus.txt fmodel.txt fop.txt")
    f = open('./fop.txt', 'r')
    flesk = f.readlines()
    print flesk
    if flesk == []:
       flskk = 0.0
    else:
       flsk = flesk[0]
       flskk = round((float(flsk)),2)
    return (flskk) 
       
    #flsk = flesk[0]
    #flskk = round((float(flsk)),2)
    #return (flskk)      
        
           

#xc = [[] for i in range(len(faa))]
#xm = [[] for i in range(len(fbb))]

f1 = "./feat_trtst.csv"
outfile = open(f1, "a")
outfile.write('jcd, swo, idfo, tf_idf, phro')
outfile.write("\n")
for line in faa:          
     xx = nltk.word_tokenize(line)
     xxx=xx[0].split('.')
     xxx.remove(xxx[2])
     xxx.remove(xxx[2])
     xxxx='.'.join(xxx)  
          
     for j in fbb:         
         n = nltk.word_tokenize(j) 
         nn=n[0].split('-')
         nnn=nn[0].split('_')
         nnnn='.'.join(nnn) 
                  
         if xxxx== nnnn:

            y1 = line.replace('<STOP>', "")
            y = y1.replace('<STOP>\n',"")
            ynew = nltk.word_tokenize(y)
            yfinal = " ".join(ynew[1:])
            print yfinal
                      
            for c in string.punctuation:
                yfinal = yfinal.replace(c,"") 
    
            tokens=word_tokenize(str(yfinal.lower()))
            tokens = [w for w in tokens if not w in stopset]
           
            xc = []
            xm = []

            """
            for item in tokens:
                lemw = wordnet_lemmatizer.lemmatize(item)
                xc[count].append(lemw) 
            """

            for item in tokens:
                lemw = wordnet_lemmatizer.lemmatize(item)
                xc.append(lemw)            


      
        
            """
            for item in xc[count]:
                stemmed[count].append(stemmer.stem(item))
            st1 = stemmed[count]
            """
            stemmed = []
            stemmed1 = [] 
            for item in xc:
                stemmed.append(stemmer.stem(item))
            st1 = stemmed
   

            x1 = j.replace('<STOP>', "")
            x = x1.replace('<STOP>\n',"")
            xnew = nltk.word_tokenize(x)
            xfinal = " ".join(xnew[1:])
            print xfinal      
                        

            for c in string.punctuation:
                xfinal = xfinal.replace(c,"") 
    
            tokensm=word_tokenize(str(xfinal.lower()))
            tokensm = [w for w in tokensm if not w in stopset]
       
            """
            for item in tokensm:
                lemwm = wordnet_lemmatizer.lemmatize(item)
                xm[count].append(lemwm) 
            """ 
            
            for item in tokensm:
                lemwm = wordnet_lemmatizer.lemmatize(item)
                xm.append(lemwm) 


            """
            for item in xm[count]:
                stemmed1[count].append(stemmer.stem(item))
            st2 = stemmed1[count]
            """

            for item in xm:
                stemmed1.append(stemmer.stem(item))
            st2 = stemmed1
            #print st1
            #print st2

         
            break
                


     xy[count][0] = jc(st1, st2, count)
     xy[count][1] = swo(st1, st2, count)
     xy[count][2] = idfo(st1, st2, count)
     xy[count][3] = tf_idf(st1, st2, count)
     xy[count][4] = phro(st1, st2, count) 
     print xy[count]
     final_line = str(xy[count][0])+','+str(xy[count][1])+','+str(xy[count][2])+','+str(xy[count][3])+','+str(xy[count][4])+'\n'   

    
     outfile.write(final_line)      
      
    
     count = count + 1
     #print count
#print xy

