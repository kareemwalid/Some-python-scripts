f=open("list.txt","w")
for i in range(0,10):
    x=str(i)
    part_1=x*8
    #print(part_1)
    c=x*4
    for z in range(0,10):
        s=str(z)
        momo=s*4
        ff=momo+c
        #print ff
        f.write(ff+"\n")
f.close()        
        
