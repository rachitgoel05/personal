import random
#sum1=0
#avg=0
#file=open('review.txt','a')
#for i in range(0,74):
#    v=round(random.uniform(1,10),1)
#    sum1+=v
#    file.write(str(v))
#    file.write("\n")
#    
#print('finished')    
#avg=sum1/74
#file.close()

index=1
rp=[]
irp=[]
file=open('review.txt','r')
fil1=open('revelant_pages.txt','a')
fil2=open('irrevelant_pages.txt','a')
for i in file:
    if(float(i)<avg):
        irp.append(index)
    else:
        rp.append(index)
    index+=1
print(rp)
print(irp)
print('finished')
file.close()    
for i in rp:
    fil1.write(str(i))
    fil1.write("\n")
fil1.close()
for i in irp:
    fil2.write(str(i))
    fil2.write("\n")
fil2.close()
print("FINISHED")    