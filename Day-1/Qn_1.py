try:
    file=open("input.txt",'r')
    text=file.read()
except:
    print("File is not found")
else:
    text=text.lower()
    words=text.split(' ')
    words=[w.strip(",:;.{}()") for w in words]
    words=[w.replace("'s",'')for w in words]
    result=[]
    for w in words:
        if w not in result:
            result.append(w)
result=sorted(result,key=len)
try:
    file2=open("output.txt",'w')
except:
    print("File not found")
else:
    with file2 as f:
        for word in result:
            f.write("%s%d "%(word,len(word)))
content=open("output.txt",'r')
print(content.read())
