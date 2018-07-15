import PyPDF2
import string
from nltk.corpus import stopwords
import nltk
import pandas as pd
import re
obj=open('JavaBasics-notes.pdf','rb')
PDFreader=PyPDF2.PdfFileReader(obj)
n=PDFreader.numPages
content=''
for i in range(n):
    content=content+PDFreader.getPage(i).extractText()
no_punch=[]
for i in content:
    if i not in string.punctuation:
        no_punch.append(i)
final_clean=''.join(no_punch)
clean_content=[]
for word in final_clean.split():
    if word.lower() not in stopwords.words('english'):
        clean_content.append(word.lower())
nlp_words=nltk.FreqDist(clean_content)
word=[]
#word=list(word)
for j in clean_content:
    if j not in word:
        word.append(j)
freq=[]
for i in word:
    freq.append(nlp_words.get(i))
df=pd.DataFrame({'freq':freq},index=word)
df.to_excel('with_numerics.xlsx',sheet_name='sheet 1',index=True)

"""if the above data is to be represented without numerics """


tok=re.sub('[^a-zA-Z,]',' ',final_clean)
tok=tok.lower()
clean_content2=[]

for word2 in tok.split():
    if word2 not in stopwords.words('english'):
        clean_content2.append(word2)
        
        
nlp_words2=nltk.FreqDist(clean_content2)
word2=[]
#word=list(word)
for j2 in clean_content2:
    if j2 not in word2:
        word2.append(j2)
freq2=[]
for i2 in word2:
    freq2.append(nlp_words2.get(i2))
df2=pd.DataFrame({'freq':freq2},index=word2)
df2.to_excel('without_numerics.xlsx',sheet_name='sheet 1',index=True)





