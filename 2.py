g=raw_input()
y=g.split(',')
j=""
for i in y:
    m=1
    for k in range(int(i)+1)[1:]:
        m*=10

    p=m-1
    #print p
    while 1:
        #print p%int(i)
        if p%int(i)==0:
            j+=str(p)+','
            break
        else:
            #print m
            print p
            p-=1
print j[:-1]