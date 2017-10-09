f = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/Only_Student_Answers.txt', 'r')
g = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/cc.txt', 'a')
q = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/Questions.txt', 'r')



#a = [40,40,38,40,40,105,40,40,40,110,39,41,40,40,40]   # no. of student answers for each question
#a=[97,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,100,100,100,99,100,100,100,99,100,101,100,100,100,100,100,100,100,100,102,100,100,65,100,100]

a=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#A = ['EM.13','MX.11b','II.12b','EM.33b','LF.13b','PS.24a','VB.5c','LP.16c','FN.26b','PS.2b','ME.36','ME.74b','MS.50b','SE.44','SE.27b']
#A=['EV.22a','WA.20b','HB.42a','HB.35','WA.12a','EV.12b','HB.6a','WA.12b','WA.32b','HB.53b','WA.52a','HB.43','HB.46','WA.31','EV.8c','WA.17b','HB.24b1','HB.24b2','WA.18','WA.15a','HB.60','WA.7b','WA.24b','WA.29','HB.53a2','WA.15b','EV.35a','WA.51','WA.22','HB.42b','WA.33b','EV.25','WA.30b','HB.34','HB.59b','WA.12c','EV.21','HB.22a','WA.50b','HB.59a','WA.20a','WA.16b','WA.21','EV.11','WA.52b','HB.54a2']
A=[]
q1=q.readlines()
for line in q1:
    a=line.split("  ")
    b=a[0]
    c=b.split("_")
    d=".".join(c)
    A.append(d)
print len(A)   

for i in A:
    #for j in range(a[A.index(i)]):
    for j in range(4):         
        #for k in range(j):  # 29 times, 
        g.write(str(i) + '.' + str(j + 1))
        g.write('\n')
        #    if i11 != 

f.close()
g.close()



from itertools import izip
with open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/corpus_final.txt', 'w') as res, open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/cc.txt') as f1, open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/Only_Student_Answers.txt') as f2:
    
    for line1, line2 in zip(f1, f2):
        res.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))


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

stopset = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

"""
infile = open('./corpus_final.txt','r')
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
"""
lsi = gensim.models.lsimodel.LsiModel.load('/home/saransh/Saransh_21.7.17/relevance_fb/lsi.txt')
#id2word = gensim.corpora.Dictionary.load_from_text('/home/saransh/Saransh_21.7.17/relevance_fb/wiki_en_wordids.txt')
dictionary = gensim.corpora.Dictionary.load_from_text('/home/saransh/Saransh_21.7.17/relevance_fb/wiki_en_wordids.txt')
mm = gensim.corpora.MmCorpus('/home/saransh/Saransh_21.7.17/relevance_fb/wiki_en_tfidf.mm')


#cstmmd = []
#stmmd = []
#lmf = []; clmf = []; 
#lemw = []
ct = 0
xy = [[0 for i in range(4)] for j in range(135)]
#xy =[[0 for i in range()] for j in range(1862)]
sims = []
#f_sim = open('./sims.txt','a')
f = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/corpus_final.txt', 'r')
g = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/Reference_Answers.txt', 'r')

f1 = f.readlines()
g1 = g.readlines()

for line in f1:
    for line1 in g1:
         a1 = nltk.word_tokenize(line)

         a2 = nltk.word_tokenize(line1)

         x1 = a1[0].split(".")
         x2 = ".".join(x1[0:-1]) 
         x3 = x1[-1]
         z1=a2[0].split('-')
         z2=z1[0].split('_')
         z3='.'.join(z2)
         z4=''.join((z3,'p'))
         z5=z4.split('_')
         z6='.'.join(z5)
        
         if x2 == z3:
    

           #print line
            a11 = line.split(a1[0])
            
            y1 = a11[1].replace('<STOP>', "")

          
            ctkns=word_tokenize(str(y1.lower()))
            ctkns = [w for w in ctkns if not w in stopset]

            clmf = []
            for item in ctkns:
                clmw = wordnet_lemmatizer.lemmatize(item)
                clmf.append(clmw)

            cstmmd = []
            for item in clmf:
                cstmmd.append(stemmer.stem(item))
    
            c_vec = " ".join(cstmmd)
            cvec_bow = dictionary.doc2bow(c_vec.split())
            cvec_lsi = lsi[cvec_bow] 


            a22 = line1.split(a2[0])
            y2 = a22[1].replace('<STOP>', "") 

            tkns=word_tokenize(str(y2.lower()))
            tkns = [w for w in tkns if not w in stopset]

            lmf = []
            for item in tkns:
                lmw = wordnet_lemmatizer.lemmatize(item)
                lmf.append(lmw)
   
            stmmd = []
            for item in lmf:
                stmmd.append(stemmer.stem(item))
    
            new_vec = " ".join(stmmd)
            vec_bow = dictionary.doc2bow(new_vec.split())
            vec_lsi = lsi[vec_bow]  

            sim = matutils.cossim(cvec_lsi, vec_lsi)

            #print sim

            #print x2

            if str(x2) in A:
               xind = A.index(str(x2))

               #print int(xind)
               #print int(x3) - 1
               
               
               xy[int(xind)][int(x3) - 1] = sim    # question-wise placing scores of answers

            
            #sims.append(str(sim))
              
            #f.write(str(a1[0]) + '-' + str(a2[0]) + " " + ':' + " " + str(sim))
            #f_sim.write(str(a1[0]) + ':' + " " + str(sim))
            #f_sim.write(str(sim))
            #f_sim.write("\n")
       #    print sims_opt[:10]
            #print ct
            ct = ct + 1
            break
            #sort()
print ct

#f_sim.close()
f.close()
g.close()


#print xy




c = zip(A, xy)                 # zipping question-id and scores of answers to the corresponding question-id

d = []
for i in range(len(c)):
    #print c[i]
    j = list(c[i])
    #print j
    #i1 = list(j[0])
    empty = []
    i1 = list(str(j[0]))
    i2 = "".join(i1[:])
    empty.append(i2)
    #print j[1]
    e = []
    e.append(empty)
    e.append(j[1])
    d.append(e)

#print d



import nltk
from nltk import word_tokenize

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

stopset = set(stopwords.words('english'))

wordnet_lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

#stemmed = [[] for i in range(len(txt))] 
#cstmmd = []
#stmmd = []
#lmf = []; clmf = []; 
#lemw = []
ct1 = 0


arr = []
f = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/corpus_final.txt', 'r')
f1 = f.readlines()
for line in f1:
    line = line.split(" ")
    arr_old = []
    id1 = line[0]
    ans = " ".join(line[1:])
    arr_old.append(id1)
    arr_old.append(ans)
    arr.append(arr_old)

#print arr                                      # displaying both id and text
f.close()

arr_m = []
g = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/Reference_Answers.txt', 'r')
g1 = g.readlines()
for line in g1:
    line = line.split("  ")
    arr_old1 = []
    y1=line[0].split('-')
    y2=y1[0].split('_')
    y3='.'.join(y2)
    ans = line[1]
    arr_old1.append(y3)
    arr_old1.append(ans)
    arr_m.append(arr_old1)

#print "arr_m" 
#print arr_m                                 # displaying both id and text
g.close()






top_max_scores = []
modifier = []
model_new = []
for i in range(len(d)):
    xy1 = d[i][1]
    #print xy1
    if not all(xy1[x]==0 for x in range(len(xy1))):
       xy1[:] = [item for item in xy1 if item != 0]
       ques_n = xy1[:]
    else:
       xxy = d[i][0][0]
       xxy1 = xxy.split(".")
       xxy2 = int(A.index(xxy)) - 1
       #print xxy2
       #new_q = a[xxy2]
       new_q=4
       #print new_q
       ques_n = xy1[0:new_q]
       print ques_n
       
    
    #print ques_n
    #S1 = sorted(ques_n) 
    S1 = sorted(ques_n, reverse=True) 
    print len(S1)
    #print S1
    #S11 = sorted(range(len(ques_n)), key=lambda k: ques_n[k])   # ascending order of indices
    S11 = sorted(range(len(ques_n)), key=lambda k: ques_n[k],reverse=True)   # descending order of indices
 

    #print S11
    S12 = S11[0:1]                                             # picking up top 6 answer scores (indices) having maximum scores (one-fifth of number of student answers corresponding to each question)
    #print S12
    xx_top = []
    for xx in S12:
        xx1 = str(d[i][0][0]) + "." + str(xx + 1)
        xx2 = ques_n[xx]
        xx3 = []
        xx3.append(xx1)
        xx3.append(xx2)
        xx_top.append(xx3)
         
    #print xx_top
    top_max_scores.append(xx_top)             # question-wise top 6 scores are stored 

    xy2 = d[i][0][0]              # 1.1 selected in xy, 2.4 selected

    #print xy2
    md = []
    md.append(xy2)
    #md.append(str(S11[1]))
    md1 = S12[0]
    #print md1
    N_sco = ques_n[md1]
    #print N_sco
    md.append(N_sco)
    modifier.append(md)                  # question-wise replacement score
    
    #y1 = arr[xy2][1]                   # 1.1.
    #f_sel = open('./asc_sel.txt', 'a')
    f_sel = []
    for x in S12:
        xy3 = str(xy2) + "." + str(x)
        for aa in arr:
            if aa[0] == xy3:
               xy4 = aa[1]
               f_sel.append(xy4)
               break

    #print f_sel

    f_selarr = []
    for i1 in f_sel:
        i2 = nltk.word_tokenize(i1)
        f_selarr.append(i2)

    #print f_selarr                         # selected top 6 answers having maximum scores
        

    
    
    m_sel = []                                # old model answer
    for b in arr_m:
        if str(b[0]) == str(xy2):
           xy5 = b[1]
           xy6 = nltk.word_tokenize(xy5)
           m_sel.append(xy6)
           #break                             

    #print m_sel
    m_seltk = m_sel[0]                         # tokenized model answer

    


    for ab in f_selarr:   # f_selarr is list of lists....each list repr tokens for an answer
        xnew = [x.lower() for x in ab]
        for ii in xnew:
            if ii not in m_seltk:
               m_seltk.append(ii)                          # new model answer 

    a1 = []
    a1.append(str(d[i][0][0]))
    a1.append(m_seltk)
    model_new.append(a1)
    #model_new.append(m_seltk)


#print top_min_scores              # index with score

#print modifier


#print model_new

#for x in model_new:
#    xm = " ".join(x[1][:])

new_model = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/new_model.txt', 'a')
for iter1 in model_new:
    iter2 = " ".join(iter1[1][:])
    #iter2 = " ".join(iter1[:])
    new_model.write(iter1[0] + " " + str(iter2))
    new_model.write('\n')
new_model.close()


"""
infile = open('./corpus_final.txt','r')
outfile = open('./corpus_final_n.txt', 'w')

infile1 = open('./new_model.txt','r')
outfile1 = open('./new_model_n.txt', 'w')


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
"""
print "really done part2"

#xy = [[0 for i in range(35)] for j in range(87)]

#sims = []


#id2word_wiki = gensim.corpora.Dictionary.load('./data/wiki.dictionary')
#lda_model = gensim.models.LdaModel.load('./data/lda_wiki.model')

#dictionary = corpora.Dictionary.load('./deerwester.dict')
#lsi = models.LsiModel.load('lsi_model.model')
f_sim = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/sims2.txt','a')
f = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/corpus_final.txt', 'r')
g = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/new_model.txt', 'r')
f_sim_1 = open('/home/saransh/Saransh_21.7.17/ScientsBank/unseen_answers/sims2_new.txt', 'a')


f1 = f.readlines()
g1 = g.readlines()

for line in f1:
    for line1 in g1:
         a1 = nltk.word_tokenize(line)

         a2 = nltk.word_tokenize(line1)
        
         x1 = a1[0].split(".")
         x2 = ".".join(x1[0:-1]) 
         z1=a2[0].split('-')
         z2=z1[0].split('_')
         z3='.'.join(z2)  
         z4=''.join((z3,'p'))
         z5=z4.split('_')
         z6='.'.join(z5)      
         if x2 == z3:

           #print line
            a11 = line.split(a1[0])
            
            y1 = a11[1].replace('<STOP>', "")

          
            ctkns=word_tokenize(str(y1.lower()))
            ctkns = [w for w in ctkns if not w in stopset]

            clmf = []
            for item in ctkns:
                clmw = wordnet_lemmatizer.lemmatize(item)
                clmf.append(clmw)

            cstmmd = []
            for item in clmf:
                cstmmd.append(stemmer.stem(item))
    
            c_vec = " ".join(cstmmd)
            cvec_bow = dictionary.doc2bow(c_vec.split())
            cvec_lsi = lsi[cvec_bow] 


            a22 = line1.split(a2[0])
            y2 = a22[1].replace('<STOP>', "") 
            y2 = y2.replace('< STOP >', "") 
            tkns=word_tokenize(str(y2.lower()))
            tkns = [w for w in tkns if not w in stopset]

            lmf = []

            for item in tkns:
                lmw = wordnet_lemmatizer.lemmatize(item)
                lmf.append(lmw)
   
            stmmd = []
            for item in lmf:
                stmmd.append(stemmer.stem(item))
    
            new_vec = " ".join(stmmd)
            vec_bow = dictionary.doc2bow(new_vec.split())
            vec_lsi = lsi[vec_bow]  

            sim = matutils.cossim(cvec_lsi, vec_lsi)

            #any((x > 0 for x in list))
            #if any(top_min_scores[i][0] == a1[0] for i in range(len(top_min_scores))) == True:

            #if any(top_min_scores[i][0] for i in range(len(top_min_scores))]

            #results = [t[1] for t in mylist if t[0] == 10]

            #print sim

            #print a1[0]
            #print type(a1[0])
            #print any(str(top_min_scores[i][j][0]) == str(a1[0]) for i in range(len(top_min_scores)) for j in range(len(top_min_scores[i])) )
            if any(str(top_max_scores[i][j][0]) == str(a1[0]) for i in range(len(top_max_scores)) for j in range(len(top_max_scores[i])) ) == True:
               rs = [top_max_scores[i][j][1] for i in range(len(top_max_scores)) for j in range(len(top_max_scores[i])) if top_max_scores[i][j][0] == a1[0]]
               #print rs
               sim1 = rs[0]

               #print sim1
            else:

               #print modifier
               for m in range(len(modifier)):
                   if str(modifier[m][0]) == str(x2):
                      #print float(sim)
                      #print modifier[m][1]
                      sim1 = float(sim) * float(modifier[m][1])
                      #print sim1

                   #break


            
            #print sim1
            f_sim_1.write(str(a1[0]))
            f_sim_1.write(' ')
            f_sim_1.write(str(sim1))
 
            f_sim.write(str(sim1))
            f_sim.write('\n')

            
            
            
            ct1 = ct1 + 1
            print ct1
            break
            #sort()
         

f_sim.close()
f.close()
g.close()


#print xy
    

  

  


    
        

    

    
    


 
        










