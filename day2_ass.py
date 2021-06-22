import sys
import re
def palin(w):
    return w==w[::-1]
def splitfn(text):
    text = text.replace(' ', '')
    answer = re.split('a|e|i|o|u', text)
    while ('' in answer):
        answer.remove('')
    for ans in answer:
        file.write("%s " % ans)
def capitalizethird(text):
    for w in text:
        if (len(w) > 2):
            w = w[0:2] + w[2].upper() + w[3:]
        file.write("%s " % w)
def capitalizefifth(words):
    count = 0
    for w in words:
        count += 1
        if (count % 5 == 0):
            file.write("%s "%w.upper())
            continue
        else:
            file.write("%s " % w)
def replacespace (text) :
    t = text.replace(' ', '-')
    file.write("%s" % t)
try:
    filename=sys.argv[1]
    f=open(filename,'r')
    text=f.read()
    text=text.replace('.',' ')
    text=text.replace("'s",'')
    words=re.split(' ',text)
    #Prefix "To"
    count_prefix=0
    for w in words:
        if(w.startswith("To") and len(w)>2):
            count_prefix+=1
    print('Prefix count:',count_prefix)
    #suffix "ing"
    count_suffix = 0
    for w in words:
        if(w.endswith("ing")):
            count_suffix+=1
    print('suffix count:',count_suffix)
    #most repeated word
    max_count=0
    answer=""
    for i in range(len(words)):
        count=0
        for j in range(i+1,len(words)):
            if(words[i]==words[j]):
                count+=1
        if(count>max_count):
            max_count=count
            answer = words[i]
    print('Most repeated words:',answer, " ", max_count)
    #palindrome
    print("Palindromic words")
    for w in words:
        if(palin(w)):
            print(w)
    #Unique word
    result=[]
    for w in words:
        w=w.lower()
        if w not in result:
            result.append(w)
    print('Unique Words')
    print(result, end=" ")
    #creating dictionary
    dict={}
    for w in enumerate(words):
        dict.update({w})
    print(dict)
    ran = 'fileoutput'
    for i in range(4):
        file = open(ran + str(i+1) + '.txt', 'w')
        if i == 0:
            splitfn(text)
        elif i == 1:
            capitalizethird(words)
        elif i == 2:
            capitalizefifth(words)
        elif i==3:
            replacespace(text)
        file.close()
    f.close()
except:
    print("File not found")












