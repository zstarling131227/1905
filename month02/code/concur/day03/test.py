def count(x,y):
    c=0
    while c<7000000:
        x+=1
        y+=1
        c+=1
def io():
    write()
    read()

def write():
    f=open("test",'w')
    for i in range(1800):
        f.write("wangbadan\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()


