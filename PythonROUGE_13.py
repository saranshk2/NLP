import string
import nltk
import numpy
import gensim
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

stopset = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()



          
    
import os
import re

def PythonROUGE(ct,guess_summ_list,ref_summ_list,ngram_order=2):
    """ Wrapper function to use ROUGE from Python easily. """

    # even though we ask that the first argument is a list,
    # if it is a single string we can handle it
    if type(guess_summ_list) == str:
        temp = list()
        temp.append(ref_summ_list)
        guess_summ_list = temp
        del temp
   
   
    
    # this is the path to your ROUGE distribution
    ROUGE_path = '/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/ROUGE-1.5.5.pl'
    data_path = '/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/data'
      
    
    # these are the options used to call ROUGE
    # feel free to edit this is you want to call ROUGE with different options
    #options = '-a -m -n -s' + str(ngram_order)
    options = '-a -m -n ' + str(ngram_order)
    
    # this is a temporary XML file which will contain information
    # in the format ROUGE uses
    xml_path = 'temp.xml'
    xml_file = open(xml_path,'w')
    xml_file.write('<ROUGE-EVAL version="1.0">\n')
    for guess_summ_index,guess_summ_file in enumerate(guess_summ_list):
        xml_file.write('<EVAL ID="' + str(guess_summ_index+1) + '">\n')
        create_xml(xml_file,guess_summ_file,ref_summ_list[guess_summ_index])
        xml_file.write('</EVAL>\n')
    xml_file.write('</ROUGE-EVAL>\n')
    xml_file.close()
    
    
    # this is the file where the output of ROUGE will be stored
    ROUGE_output_path = 'ROUGE_result.txt'
    
    # this is where we run ROUGE itself
    #exec_command = ROUGE_path + ' -e ' + data_path + ' ' + options + ' -x ' + xml_path + ' > ' + ROUGE_output_path
    #exec_command = ROUGE_path + ' -e ' + data_path + ' ' + options + xml_path + ' > ' + ROUGE_output_path

    #exec_command = ROUGE_path + ' -e ' + data_path + ' ' + options + ' -s ' + ' -2 ' + ' -1 ' + ' -U ' + ' -x ' +  xml_path + ' > ' + ROUGE_output_path  # ROUGE-L is not calculated
    exec_command = ROUGE_path + ' -e ' + data_path + ' ' + options + ' -s ' + ' -2 ' + ' -1 ' + ' -U ' + ' -w 1.2 ' + xml_path + ' > ' + ROUGE_output_path  # ROUGE-L is calculated

    os.system(exec_command)
    
    # here, we read the file with the ROUGE output and
    # look for the recall, precision, and F-measure scores
    recall_list = list()
    precision_list = list()
    F_measure_list = list()
    #print "Hello"
    ROUGE_output_file = open(ROUGE_output_path,'r')
    f1 = ROUGE_output_file.readlines()
    #print f1

    

    
    ROUGE_output_file.seek(0)
    for line in ROUGE_output_file:
        for n in xrange(ngram_order):
            match = re.findall('X ROUGE-' + str(n+1) + ' Average_R: ([0-9.]+)',line)
            if match != []:
                recall_list.append(float(match[0]))
                xyn[ct][0][0] = float(match[0])
            match = re.findall('X ROUGE-' + str(n+1) + ' Average_P: ([0-9.]+)',line)
            if match != []:
                precision_list.append(float(match[0]))
                xyn[ct][0][1] = float(match[0])
            match = re.findall('X ROUGE-' + str(n+1) + ' Average_F: ([0-9.]+)',line)
            if match != []:
                F_measure_list.append(float(match[0]))
                xyn[ct][0][2] = float(match[0])


        match = re.findall('X ROUGE-L' + ' Average_R: ([0-9.]+)',line) 
        if match != []:
            recall_list.append(float(match[0]))
            xyn[ct][2][0] = float(match[0])
        match = re.findall('X ROUGE-L' + ' Average_P: ([0-9.]+)',line) 
        if match != []:
            precision_list.append(float(match[0]))
            xyn[ct][2][1] = float(match[0])
        match = re.findall('X ROUGE-L' + ' Average_F: ([0-9.]+)',line) 
        if match != []:
            F_measure_list.append(float(match[0]))
            xyn[ct][2][2] = float(match[0])

        
        match = re.findall('X ROUGE-W-1.2' + ' Average_R: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][3][0] = float(match[0])
        match = re.findall('X ROUGE-W-1.2' + ' Average_P: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][3][1] = float(match[0])
        match = re.findall('X ROUGE-W-1.2' + ' Average_F: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][3][2] = float(match[0])


        match = re.findall('X ROUGE-S' + ' Average_R: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][4][0] = float(match[0])
        match = re.findall('X ROUGE-S' + ' Average_P: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][4][1] = float(match[0])
        match = re.findall('X ROUGE-S' + ' Average_F: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][4][2] = float(match[0])

      
        match = re.findall('X ROUGE-SU*' + ' Average_R: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][5][0] = float(match[0])
        match = re.findall('X ROUGE-SU*' + ' Average_P: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][5][1] = float(match[0])
        match = re.findall('X ROUGE-SU*' + ' Average_F: ([0-9.]+)',line) 
        if match != []:
            #F_measure_list.append(float(match[0]))
            xyn[ct][5][2] = float(match[0])

       
    ROUGE_output_file.close()
    print xyn[ct]

    #f1 = "./feat.csv"
    #outfile = open(f1, "a")
    final_line = str(xyn[ct][0][0]) +','+str(xyn[ct][0][1])+','+str(xyn[ct][0][2])+','+str(xyn[ct][1][0])+','+str(xyn[ct][1][1])+','+str(xyn[ct][1][2])+','+str(xyn[ct][2][0])+','+str(xyn[ct][2][1])+','+str(xyn[ct][2][2])+','+str(xyn[ct][3][0])+','+str(xyn[ct][3][1])+','+str(xyn[ct][3][2])+','+str(xyn[ct][4][0])+','+str(xyn[ct][4][1])+','+str(xyn[ct][4][2])+','+str(xyn[ct][5][0])+','+str(xyn[ct][5][1])+','+str(xyn[ct][5][2])+'\n'

   

    
    outfile.write(final_line)
    #outfile.write("\n")
    #return (xy[count]);  
   
    
        
    # remove temporary files which were created
    os.remove(xml_path)
    os.remove(ROUGE_output_path)


    return (recall_list,precision_list,F_measure_list)


def mainf(ct):
#if __name__ == '__main__':
    #guess_summary_list = ['Example/Guess_Summ_1.txt','Example/Guess_Summ_2.txt']
    
    guess_summary_list = ['/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/datanew/data1.txt']
    #ref_summ_list = [['Example/Ref_Summ_1_1.txt','Example/Ref_Summ_1_2.txt'] , ['Example/Ref_Summ_2_1.txt','Example/Ref_Summ_2_2.txt','Example/Ref_Summ_2_3.txt']]
   
    #ref_summ_list =  [['/home/saransh/PythonROUGE-master/RELEASE-1.5.5/datanew/data2.txt'], ['/home/saransh/PythonROUGE-master/RELEASE-1.5.5/datanew/data2.txt']]

    ref_summ_list =  [['/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/datanew/data2.txt']]
    recall_list,precision_list,F_measure_list = PythonROUGE(ct,guess_summary_list,ref_summ_list,ngram_order=2)
    #print 'recall = ' + str(recall_list)
    #print 'precision = ' + str(precision_list)
    #print 'F = ' + str(F_measure_list)
    return;








   
   
    
# This is an auxiliary function
# It creates an XML file which ROUGE can read
# Don't ask me how ROUGE works, because I don't know!
def create_xml(xml_file,guess_summ_file,ref_summ_list):
    xml_file.write('<PEER-ROOT>\n')
    guess_summ_dir = os.path.dirname(guess_summ_file)
    xml_file.write(guess_summ_dir + '\n')
    xml_file.write('</PEER-ROOT>\n')
    xml_file.write('<MODEL-ROOT>\n')
    ref_summ_dir = os.path.dirname(ref_summ_list[0] + '\n')
    xml_file.write(ref_summ_dir + '\n')
    xml_file.write('</MODEL-ROOT>\n')
    xml_file.write('<INPUT-FORMAT TYPE="SPL">\n')      
        
                
    xml_file.write('</INPUT-FORMAT>\n')
    xml_file.write('<PEERS>\n')
    guess_summ_basename = os.path.basename(guess_summ_file)
    xml_file.write('<P ID="X">' + guess_summ_basename + '</P>\n')
    xml_file.write('</PEERS>\n')
    xml_file.write('<MODELS>')
    letter_list = ['A','B','C','D','E','F','G','H','I','J']
    for ref_summ_index,ref_summ_file in enumerate(ref_summ_list):
        ref_summ_basename = os.path.basename(ref_summ_file)
        xml_file.write('<M ID="' + letter_list[ref_summ_index] + '">' + ref_summ_basename + '</M>\n')
    
    xml_file.write('</MODELS>\n')
    return(xml_file)



ct = 0
#xyn = [[[0 for i in range(3)]for j in range(6)]for k in range(2442)]

#f1 = "./feat_train3.csv"
f1 = "./feat_train5.csv"
outfile = open(f1, "a")
outfile.write('ROUGE-1_R, ROUGE-1_P, ROUGE-1_F, ROUGE-2_R, ROUGE-2_P, ROUGE-2_F, ROUGE-L_R, ROUGE-L_P, ROUGE-L_F, ROUGE-W_R, ROUGE-W_P, ROUGE-W_F, ROUGE-S_R, ROUGE-S_P, ROUGE-S_F, ROUGE-SU_R, ROUGE-SU_P, ROUGE-SU_F')
outfile.write("\n")

fa = open(r"/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/Student_Answers.txt",'r')
fb = open(r"/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/Reference_Answers.txt",'r')
faa = fa.readlines()
le = len(faa)

xyn = [[[0 for i in range(3)]for j in range(6)]for k in range(le)]

fbb = fb.readlines()

for line in faa:   
    
    
    for line1 in fbb:
        
        
        a1 = nltk.word_tokenize(line)

        a2 = nltk.word_tokenize(line1)

        
        b1=a1[0].split('.')
        b1.remove(b1[2])
        b1.remove(b1[2])
        c1='.'.join(b1)

        b2=a2[0].split('-')
        b22=b2[0].split('_')
        c2='.'.join(b22)
        
        if c1==c2:

           """
           #print line
           a11 = line.split(a1[0])
           y1 = a11[1]
           for c in string.punctuation:
               y1 = y1.replace(c,"") 
           ynew = y1.lower()
           print ynew
          
           
           
           #print line1
           a22 = line1.split(a2[0])
           y2 = a22[1]         
           for c in string.punctuation:
               y2 = y2.replace(c,"")        
           yneww = y2.lower()
           print yneww"""

           a11 = line.split(a1[0])
           y1 = a11[1]
           ynew=y1.lower()

           a22 = line1.split(a2[0])
           y2 = a22[1]
           yneww=y2.lower()
      
 
           
    
           ff1 = open('/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/datanew/data1.txt', 'w')
           ff1.write(ynew)
           ff2 = open('/home/saransh/ROUGE/train/PythonROUGE-master/RELEASE-1.5.5/datanew/data2.txt', 'w')
           ff2.write(yneww)

           ff1.close()
           ff2.close()
           mainf(ct)
           ct=ct+1
    """
           print ct
           ct = ct + 1
           break
           """




















 


