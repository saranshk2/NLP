# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:23:06 2017

@author: saranshk2
"""

from xml.dom import minidom
import os
path="/home/saranshk2/semeval2013-Task7-5way/sciEntsBank/train/Core"
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    doc=minidom.parse(fullname)
    f1=open('Questions.txt','a')
    quess = doc.getElementsByTagName("question")[0]
    ques = doc.getElementsByTagName("questionText")[0]
    f1.write(quess.getAttribute('id'))
    f1.write('  ')
    f1.write(ques.firstChild.data)
    f1.write('\n')
    refAns=doc.getElementsByTagName("referenceAnswer")[0]
    f2=open('Reference_Answers.txt','a')
    f2.write(refAns.getAttribute('id'))
    f2.write('  ')
    f2.write(refAns.firstChild.data)
    f2.write('\n')
    stuAnss=doc.getElementsByTagName('studentAnswer')
    for stuAns in stuAnss:
        st_id=stuAns.getAttribute('id')
        Ans=stuAns.firstChild.data
        Acc=stuAns.getAttribute('accuracy')
        f3=open('Student_Answers.txt','a')
        f3.write(st_id)
        f3.write('  ')
        f3.write(Ans)
        f3.write('\n')
        f4=open('Accuracy.txt','a')
        f4.write(st_id)
        f4.write('  ')
        f4.write(Acc)
        f4.write('\n')