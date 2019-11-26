#import math
#from math import pow
#import random
#from pprint import pprint
#no_of_pages=75
#"----------------------RANDOM GRAPH-------------"
#p={}
#q={}
#j=0
#for i in range(1,no_of_pages):
#    p[i]=[]
#    q[i]=[]
#for i in range(1,no_of_pages): #why not the last page
#    random_no=random.randint(1,10)
#    while j<random_no:
#        b=random.randint(1,no_of_pages-1)
#        if (i!=j and (b not in p[i]) ):
#            p[i].append(b)
#            q[b].append(i)
#        j+=1
#    j=0
#pprint(p)
p={1: [72, 18, 46, 25],
 2: [22, 19],
 3: [22, 33, 62, 48, 20],
 4: [29, 73],
 5: [74],
 6: [11, 13, 29, 58, 15, 36],
 7: [55, 16, 61, 41, 11, 29],
 8: [59, 72, 67, 55, 23, 7],
 9: [3, 22, 12],
 10: [17, 23, 40, 70, 3, 51, 27, 33],
 11: [19, 15],
 12: [33, 4, 72, 56, 69],
 13: [66, 48, 33, 34, 35, 64, 65, 62, 39, 14],
 14: [29, 52, 14, 49, 70, 35, 16],
 15: [70, 11, 64, 46, 19, 5, 71],
 16: [2, 24, 53, 41, 45, 68],
 17: [69, 2, 36],
 18: [66, 70, 47, 14, 65, 23, 10],
 19: [60, 30, 71, 35, 54, 24, 62, 41, 10, 69],
 20: [26, 61, 67, 71, 49, 63],
 21: [34, 33, 72, 19, 22, 23, 63],
 22: [14, 34, 52, 2, 70, 56, 22],
 23: [40, 48, 33],
 24: [30, 41, 64, 18, 40, 60, 70, 17, 69],
 25: [13, 55, 14, 51],
 26: [71, 48, 69, 34, 1, 20, 22],
 27: [67, 68, 2, 33, 72],
 28: [19, 38, 44],
 29: [72, 2, 15, 74, 13, 28, 21, 62, 31, 73],
 30: [74, 72, 24, 18, 56, 17, 42, 8, 26],
 31: [21, 49],
 32: [61, 55, 33, 42, 64, 7, 1, 73, 22],
 33: [46, 28, 15],
 34: [57, 12, 55, 4, 49, 64],
 35: [23, 37, 3, 74, 39, 72, 9, 8],
 36: [22],
 37: [56, 66, 9, 44, 29],
 38: [56, 16, 34, 57],
 39: [62, 20, 37, 66],
 40: [14],
 41: [71, 12, 31, 49, 64, 43, 13, 36, 70, 60],
 42: [1, 32],
 43: [12, 64, 4, 54, 30, 16, 58, 51, 36],
 44: [56],
 45: [22],
 46: [70, 37, 27, 36, 3, 14, 13, 24],
 47: [34, 33, 67, 42, 8, 9, 48, 54],
 48: [38, 68, 74, 47, 53],
 49: [64, 62, 5, 66],
 50: [28, 61, 20, 34],
 51: [37, 45, 51, 57, 7, 43, 35, 59, 32, 21],
 52: [22],
 53: [36, 70, 66, 69, 53, 26, 58],
 54: [49, 28, 40, 2, 14, 42],
 55: [11, 33, 51, 64],
 56: [17, 69, 68, 67, 16, 11, 61, 59, 48],
 57: [29, 5, 62, 71, 55, 34, 67, 69],
 58: [29, 5, 23, 1, 13],
 59: [1, 7, 52, 69],
 60: [5, 9, 1],
 61: [56, 8, 22, 25, 38, 23, 46, 32, 5, 18],
 62: [59, 6, 72],
 63: [63, 9, 58],
 64: [46, 66, 20, 65, 70],
 65: [9, 23],
 66: [7, 43, 52, 56, 46, 12, 60, 38, 44, 70],
 67: [48, 15, 32, 27, 49, 25],
 68: [45, 35, 46, 51, 48],
 69: [1, 61, 45],
 70: [1, 25, 61, 52, 48, 36, 32],
 71: [23],
 72: [45, 8, 55, 62, 65],
 73: [16, 31, 55, 52, 48, 68, 59, 64, 66, 13],
 74: [28, 37, 4, 56, 53, 9, 3, 45]}
"-----------------------------------web html--------------------"
html=open('01.php')
text=open('quotes.txt')
page_no=1
xi=text.readline()
wrt=open('%i.php' % page_no,'a')
html=open('01.php')
for li in html:
    line=li
    if('class="p4"' in line):
        main_line=list(line)
        for i in range(0,len(main_line)-4):
            if(main_line[i] == 'p' and main_line[i+1] == '4' and main_line[i+2] == '"' and main_line[i+3] == '>'):
                break
        for j in range(0,len(main_line)-4):
            if(main_line[j] == '/' and main_line[j+1] == 'h' and main_line[j+2] == '3' and main_line[j+3] == '>'):
                break
        main_line[i+4:j-1]=xi
        line=('').join(main_line)
        wrt.write(line)
    elif('<button id="p2' in line):
        print(line)
        no_pages=len(p[page_no])
        for i in range(0,no_pages):
            main_line_2=list(line)
            for j in range(0,len(main_line_2)-4):
                if(main_line_2[j] == 'e' and main_line_2[j+1] == 'f' and main_line_2[j+2] == '=' and main_line_2[j+3] == "'"):
                    print(main_line_2)
                    part_2=main_line_2[j+4:]
                    main_line_2[j+4:]=('%i.php' % p[page_no][i])
                    part_2=('').join(part_2)
                    main_line_2.append(part_2)
                    main_line_2=('').join(main_line_2)
#                        print(main_line_2)
                    wrt.write(main_line_2)
                    break            
    else:
        wrt.write(line)
page_no+=1        
wrt.close()
print("finished")    

    