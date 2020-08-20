name = input("Enter file:")
if len(name) < 1 : name = "romeo.txt"
handle = open(name)

lst=list()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        line=line.rstrip()
        line=line.split()
        lst.append(line[1])
        
bword = None
bcount= None
dic=dict()

for word in lst:
    dic[word]=dic.get(word,0) +1
    
for word,count in dic.items():
    if bcount==None or count > bcount:
        bcount=count
        bword=word
                                                       
print(bword,bcount)