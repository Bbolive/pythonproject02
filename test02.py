#1. use ,
print("Hello...",456,'Hi...',True,10+20,"Hey...")
#2. use + มีข้อแม้ว่าต้องเอาทุกตัวที่เอามาต่อกันต้องเป็น string
print("Hello... "+str(456)+' Hi...'+str(True)+' '+str(10+20)+" Hey...")
#3. use .format
print("Hello... {} Hi... {} {} Hey...".format(456,True,10+20))
print("Hello... {0} Hi... {1} {2} Hey...".format(456,True,10+20))      #index number
#4. use f-string
print(f"Hello... {456} Hi... {True} {30} Hey...")
#5. use modulas operator (%) -> %d, %f, %c, %s, ....
print("Hello... %d Hi.... %s %d Hey..." %(456,True,10+20))
