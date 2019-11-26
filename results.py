man=open("./result.html")
pr=open("./pr.txt")
wpr=open("./wpr.txt")
power=open("./power.txt")
rp=open("./revelant_pages.txt")
irp=open("./irrevelant_pages.txt")
#count=1
#main_content_2=['            <tr>\n',
#'                    <td id="t1_'+'><a href=".php"></td>\n',
#'                    <td id="t2_'+'><a href=".php"></td>\n',
#'                    <td id="t3_'+'><a href=".php"></td>\n',
#'                    <td id="t4_'+'><a href=".php"></td>\n',
#'                    <td id="t5_'+'><a href=".php"></td>\n',  
#'            </tr>\n',]
#for i in range(0,74):
#    main_content=main_content_2
#    main_content=['            <tr>\n',
#'                    <td id="t1_'+(str(count))+'"'+'><a href=".php"></td>\n',
#'                    <td id="t2_'+(str(count))+'"'+'><a href=".php"></td>\n',
#'                    <td id="t3_'+(str(count))+'"'+'><a href=".php"></td>\n',
#'                    <td id="t4_'+(str(count))+'"'+'><a href=".php"></td>\n',
#'                    <td id="t5_'+(str(count))+'"'+'><a href=".php"></td>\n',  
#'            </tr>\n',]
#    for j in main_content:
#        man.write(j)
#    count+=1
#print("fini")    
#man.close()
man_read=open("./result.html",'a')
first='<tr>'
last='</tr>'
main_content=[]
for iter in range(1,75):
        main_content.append('<tr>\n')
        coun=1
        for i in pr:
            number=int(i)
            for li in man:
                if('<td id="t1_'+(str(coun))+'"'+'>' in li):
                    my_line=li
                    my_line=list(my_line)
                    for j in range(0,len(my_line)-4):
                        if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
                            part_2=my_line[j+4:]
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
        #                    print(my_line)
        #                    man_read.write(my_line)
                            break
                    for j in range(0,len(my_line)-4):
                        my_line=list(my_line)
                        if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
                            part_2=my_line[j+4:]
        #                    print(part_2)
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
                            print(my_line)
        #                    man_read.write(my_line)
                            break                
                    break     
            coun+=1
        coun=1
        for i in wpr:
            number=int(i)
            for li in man:
                if('<td id="t2_'+(str(coun))+'"'+'>' in li):
                    my_line=li
                    my_line=list(my_line)
                    for j in range(0,len(my_line)-4):
                        if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
                            part_2=my_line[j+4:]
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
        #                    print(my_line)
        #                    man_read.write(my_line)
                            break
                    for j in range(0,len(my_line)-4):
                        my_line=list(my_line)
                        if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
                            part_2=my_line[j+4:]
        #                    print(part_2)
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
                            print(my_line)
        #                    man_read.write(my_line)
                            break                
                    break     
            coun+=1
        coun=1
        for i in power:
            number=int(i)
            for li in man:
                if('<td id="t3_'+(str(coun))+'"'+'>' in li):
                    my_line=li
                    my_line=list(my_line)
                    for j in range(0,len(my_line)-4):
                        if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
                            part_2=my_line[j+4:]
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
        #                    print(my_line)
        #                    man_read.write(my_line)
                            break
                    for j in range(0,len(my_line)-4):
                        my_line=list(my_line)
                        if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
                            part_2=my_line[j+4:]
        #                    print(part_2)
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
                            print(my_line)
        #                    man_read.write(my_line)
                            break                
                    break     
            coun+=1
        count=1    
        for i in rp:
            number=int(i)
            for li in man:
                if('<td id="t4_'+(str(count))+'"'+'>' in li):
                    my_line=li
                    my_line=list(my_line)
                    for j in range(0,len(my_line)-4):
                        if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
                            part_2=my_line[j+4:]
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
        #                    print(my_line)
        #                    man_read.write(my_line)
                            break
                    for j in range(0,len(my_line)-4):
                        my_line=list(my_line)
                        if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
                            part_2=my_line[j+4:]
        #                    print(part_2)
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
                            print(my_line)
        #                    man_read.write(my_line)
                            break                
                    break     
            count+=1            
        for i in irp:
            number=int(i)
            for li in man:
                if('<td id="t4_'+(str(count))+'"'+'>' in li):
                    my_line=li
                    my_line=list(my_line)
                    for j in range(0,len(my_line)-4):
                        if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
                            part_2=my_line[j+4:]
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
        #                    print(my_line)
        #                    man_read.write(my_line)
                            break
                    for j in range(0,len(my_line)-4):
                        my_line=list(my_line)
                        if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
                            part_2=my_line[j+4:]
        #                    print(part_2)
                            my_line[j+4:]=('%i' % number)
                            part_2=('').join(part_2)
                            my_line.append(part_2)
                            my_line=('').join(my_line)
                            print(my_line)
        #                    man_read.write(my_line)
                            break                
                    break     
            count+=1                          
                    
print("finished")





#
#count=1
#for i in rp:
#    number=int(i)
#    for li in man:
#        if('<td id="t5_'+(str(count))+'"'+'>' in li):
#            my_line=li
#            my_line=list(my_line)
#            for j in range(0,len(my_line)-4):
#                if(my_line[j] == 'e' and my_line[j+1] == 'f' and my_line[j+2] == '=' and my_line[j+3] == "\""):
#                    part_2=my_line[j+4:]
#                    my_line[j+4:]=('%i' % number)
#                    part_2=('').join(part_2)
#                    my_line.append(part_2)
#                    my_line=('').join(my_line)
##                    print(my_line)
##                    man_read.write(my_line)
#                    break
#            for j in range(0,len(my_line)-4):
#                my_line=list(my_line)
#                if(my_line[j] == 'h' and my_line[j+1] == 'p' and my_line[j+2] == '\"' and my_line[j+3] == ">"):
#                    part_2=my_line[j+4:]
##                    print(part_2)
#                    my_line[j+4:]=('%i' % number)
#                    part_2=('').join(part_2)
#                    my_line.append(part_2)
#                    my_line=('').join(my_line)
#                    print(my_line)
##                    man_read.write(my_line)
#                    break                
#            break    
#            #print("hello5")    
#    count+=1        
    
    
    
    
    

#        if('<td id="t1_'+(str(count))+'"'+'><a href=".php"></td>\n' in li):
#            print("hello1")
#            
#        if('<td id="t2_'+(str(count))+'"'+'><a href=".php"></td>\n' in li):
#            print("hello2")
#            
#        if('<td id="t3_'+(str(count))+'"'+'><a href=".php"></td>\n' in li):
#            print("hello3")
# 
#        if('<td id="t4_'+(str(count))+'"'+'><a href=".php"></td>\n' in li):
#            print("hello4")
#             