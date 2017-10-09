from __future__ import division

from config import *
from align import *
#from aligner import *
import numpy as np
from scipy import spatial
import nltk

# aligning strings (output indexes start at 1)

"""
sentence1 = "Four men died in an accident."
sentence2 = "4 people are dead from a collision."

alignments = align(sentence1, sentence2)
print alignments[0]
print alignments[1]
print
"""

# aligning sets of tokens (output indexes start at 1)

"""
sentence1 = ['Four', 'men', 'died', 'in', 'an', 'accident', '.']
sentence2 = ['4', 'people', 'are', 'dead', 'from', 'a', 'collision', '.']

alignments = align(sentence1, sentence2)

print alignments[0]
print alignments[1]

"""

"""

stop_words = ["i",  "me",  "my",  "myself",  "we",  "our",  "ours",  
              "ourselves",  "you",  "your",  "yours",  "yourself",  
              "yourselves",  "he",  "him",  "his",  "himself",  "she",  "her",
              "hers",  "herself",  "it",  "its",  "itself",  "they",  "them",
              "their",  "theirs",  "themselves",  "what",  "which",  "who",
              "whom",  "this",  "that",  "these",  "those",  "am",  "is",
              "are",  "was",  "were",  "be",  "been",  "being",  "have",
              "has",  "had",  "having",  "do",  "does",  "did",  "doing",
              "a",  "an",  "the",  "and",  "but",  "if",  "or",  "because",
              "as",  "until",  "while",  "of",  "at",  "by",  "for",  "with",
              "about",  "against",  "between",  "into",  "through",  "during",
              "before",  "after",  "above",  "below",  "to",  "from",  "up",
              "down",  "in",  "out",  "on",  "off",  "over",  "under",
              "again",  "further",  "then",  "once",  "here",  "there",
              "when",  "where",  "why",  "how",  "all",  "any",  "both",
              "each",  "few",  "more",  "most",  "other",  "some",  "such",
              "no",  "nor",  "not",  "only",  "own",  "same",  "so",  "than",
              "too",  "very",  "s",  "t",  "can",  "will",  "just",  "don",
              "should",  "now"]
stop_words += ["'s", "'ll", "'d", "'ve", "'re", "'m", "n't", "&", 
               "i.e.", "e.g."]

"""


"""
question = "How are infix expressions evaluated by computers?"
ref_answer = "First, they are converted into postfix form, " + \
             "followed by an evaluation of the postfix expression."
student_response = "computers usually convert infix expressions to postfix " +\
"expression and evaluate them using a stack."
"""

def sts_alignment(sentence1, sentence2,
                  parse_results=None,
                  sentence_for_demoting=None):
                      
    if parse_results == None:
        sentence1_parse_result = parseText(sentence1)
        sentence2_parse_result = parseText(sentence2)
        parse_results = []
        parse_results.append(sentence1_parse_result)
        parse_results.append(sentence2_parse_result)
    else:
        sentence1_parse_result = parse_results[0]
        sentence2_parse_result = parse_results[1]
        

    sentence1_lemmatized = lemmatize(sentence1_parse_result)
    sentence2_lemmatized = lemmatize(sentence2_parse_result)

    lemmas_to_be_demoted = []
    if sentence_for_demoting != None:
        if len(parse_results) == 2:
            sentence_for_demoting_parse_result = \
                                parseText(sentence_for_demoting)
            parse_results.append(sentence_for_demoting_parse_result)
        else:
            sentence_for_demoting_parse_result = parse_results[2]


        sentence_for_demoting_lemmatized = \
                            lemmatize(sentence_for_demoting_parse_result)
    
        sentence_for_demoting_lemmas = \
                        [item[3] for item in sentence_for_demoting_lemmatized]
    
        lemmas_to_be_demoted = \
    			[item.lower() for item in sentence_for_demoting_lemmas \
        					if item.lower() not in stop_words+punctuations]
    
    alignments = align(sentence1, sentence2, 
                       sentence1_parse_result, sentence2_parse_result)[0]
    
    sentence1_lemmas = [item[3] for item in sentence1_lemmatized]
    sentence2_lemmas = [item[3] for item in sentence2_lemmatized]

    sentence1_content_lemmas = \
            [item for item in sentence1_lemmas \
                      if item.lower() not in \
                            stop_words+punctuations+lemmas_to_be_demoted]

    sentence2_content_lemmas = \
            [item for item in sentence2_lemmas \
					if item.lower() not in \
                             stop_words+punctuations+lemmas_to_be_demoted]

    if sentence1_content_lemmas == [] or sentence2_content_lemmas == []:
        return (0, 0, parse_results)
    
    sentence1_aligned_content_word_indexes = \
		[item[0] for item in alignments if \
				sentence1_lemmas[item[0]-1].lower() not in \
                                stop_words+punctuations+lemmas_to_be_demoted]

    sentence2_aligned_content_word_indexes = \
		[item[1] for item in alignments if \
				sentence2_lemmas[item[1]-1].lower() not in \
                                stop_words+punctuations+lemmas_to_be_demoted]
    
    sim_score = (len(sentence1_aligned_content_word_indexes) + \
	             len(sentence2_aligned_content_word_indexes)) / \
                        				(len(sentence1_content_lemmas) + \
                        	              len(sentence2_content_lemmas))

    coverage = len(sentence1_aligned_content_word_indexes) / \
                                           len(sentence1_content_lemmas) 

    return (sim_score, coverage, parse_results)


#fa=open('/home/saransh/Saransh_21.7.17/ScientsBank/train/Student_Answers_1_4.txt','r')
fa=open('/home/saransh/Saransh_21.7.17/short-answer-grader-master/data.txt','r')
fb=open('/home/saransh/Saransh_21.7.17/ScientsBank/train/Reference_Answers.txt','r')
fc=open('/home/saransh/Saransh_21.7.17/ScientsBank/train/Questions.txt','r')
faa=fa.readlines()
fbb=fb.readlines()
fcc=fc.readlines()
f1 = "./train/res.csv"
outfile = open(f1, "a")

f2 = "./train/res1.csv"
outfile1 = open(f2, "a")

f3 = "./train/res2.csv"
outfile2 = open(f3, "a")

f4 = "./train/res3.csv"
outfile3 = open(f4, "a")


for student_response in faa:
    xx = nltk.word_tokenize(student_response)
    xxx=xx[0].split('.')
    xxx.remove(xxx[2])
    xxx.remove(xxx[2])
    xxxx='.'.join(xxx)  
    
    for ref_answer1 in fbb:
        yy = nltk.word_tokenize(ref_answer1)
        nn=yy[0].split('-')
        nnn=nn[0].split('_')
        nnnn='.'.join(nnn) 
        st = " ".join(xx[1:])
        ref = " ".join(yy[1:])
        print xxxx
        print nnnn
        if xxxx==nnnn:
            ref_answer=ref_answer1.replace('<STOP>', "")
            sim_alignment, cov_alignment, parse_results = sts_alignment(ref,st)
            outfile.write(str(cov_alignment))
            outfile.write('\n')
            outfile1.write(str(sim_alignment))
            outfile1.write("\n")

            """print sim_alignment     # similarity alignment score
            print cov_alignment"""     # coverage alignment score
            #print parse_results
            for question1 in fcc:
                zz=nltk.word_tokenize(question1)
                zzz=zz[0].split('_')
                zzzz='.'.join(zzz)
                ques=" ".join(zz[1:])
                if xxxx==zzzz:
                    question=question1.replace('<STOP>',"")

                    q_demoted_sim_alignment, q_demoted_cov_alignment, _ = sts_alignment(ref, st, parse_results, ques)
                    outfile2.write(str(q_demoted_sim_alignment))
                    outfile2.write('\n')
                    outfile3.write(str(q_demoted_cov_alignment))
                    outfile3.write("\n")
            """print q_demoted_sim_alignment
            print q_demoted_cov_alignment"""

outfile.close()
outfile1.close()
outfile2.close()
outfile3.close()
fa.close()
fb.close()
fc.close()

