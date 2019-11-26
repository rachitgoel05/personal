import pprint
f=open("meaningful_words.txt",'r')
l={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    ch=""
    for j in s:
        if((j>='a' and j<='z') or (j>='A' and j<='Z')):
            ch+=j
    l[ch]=1
    
f.close()

def distinctList(l):
    nl=[]+l
    nl.sort()
    i=0
    sl=[]
    while(1):
        if(i>=len(nl)):
            break
        c=nl.count(nl[i])
        sl.append(nl[i])
        i=i+c
    return sl

f=open("quotes.txt",'r')
word_count={}
quote_for_word={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    words=s.split()
    for i in words:
        ch=""
        for j in i:
            if((j>='a' and j<='z') or (j>='A' and j<='Z')):
                ch+=j
        try:
            if(l[ch]==1):
                try:
                    if(s not in quote_for_word[ch]):
                        quote_for_word[ch].append(s)
                except KeyError:
                    quote_for_word[ch]=[s]
                try:
                    word_count[s]+=1
                except KeyError:
                    word_count[s]=1
        except KeyError:
            continue
f.close()
f=open("quotes.txt",'r')
similarMap={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    cluster=[]
    words=s.split()
    for i in words:
        ch=""
        for j in i:
            if((j>='a' and j<='z') or (j>='A' and j<='Z')):
                ch+=j
        try:
            if(l[ch]==1):
                cluster+=quote_for_word[ch]
        except KeyError:
            continue
    if(len(cluster)==0):
        print (cluster)
    cluster=distinctList(cluster)
    clusterMap=[]
    for i in cluster:
        clusterMap.append({"quote":i,"count":word_count[i]})
    clusterMap.sort(key=lambda x: x["count"])
    ast=[i["quote"] for i in  clusterMap]
    #print clusterMap,"\n",ast,"\n*******\n"
    similarMap[s]=ast
#for i in similarMap.keys():
#    print len(similarMap[i])
#    if(len(similarMap[i])==0):
#        print i
ptoq={}
qtop={}
for i in range(1,len(similarMap.keys())+1):
    qtop[similarMap.keys()[i-1]]=i
    ptoq[i]=similarMap.keys()[i-1]
numberMap={}
for i in similarMap.keys():
    numberMap[qtop[i]]=[]
    for j in similarMap[i]:
        if(qtop[i]==qtop[j]):
            continue
        numberMap[qtop[i]].append(qtop[j])
pprint.pprint(numberMap)
#adj=[[0 for i in range(len(similarMap.keys()))] for j in range(len(similarMap.keys()))]
#for i in similarMap.keys():
#    out=similarMap[i]
#    for j in out:
#        adj[qtop[i]-1][qtop[j]-1]=1
#    print adj[qtop[i]-1]
