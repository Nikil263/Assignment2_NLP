def n(f1):
    r11=[]
    r15=[]
    r110=[]
    c=0
    for a in f1:
        c=c+1
        if(c==1):
            r11.append(a)
        if(c<=5):
            r15.append(a)
        if(c<=10):
            r110.append(a)
    return r11,r15,r110


def n3(x,y,f3):
    r11=[]
    r15=[]
    r110=[]
    co=0
    for a, b, c in f3:
    
        if(a == x and b == y and c!= None):
            co=co+1
            if(co==1):
                r11.append(c)
            if(co<=5):
                r15.append(c)
            if(co<=10):
                r110.append(c)
    return r11,r15,r110

def n15(z,q,f5):
    r51=[]
    r55=[]
    r510=[]
    co=0
    for a, b, c, d, e in f5:
    
        if(c == z and d == q and e!= None):
            co=co+1
            if(co==1):
                r51.append(e)
            if(co<=5):
                r55.append(e)
            if(co<=10):
                r510.append(e)
    return r51,r55,r510

def n10(z,q,f10):
    r51=[]
    r55=[]
    r510=[]
    co=0
    for a, b, c, d, e, f, g, h, i, j in f10:
    
        if(h == z and i == q and j!= None):
            co=co+1
            if(co==1):
                r51.append(e)
            if(co<=5):
                r55.append(e)
            if(co<=10):
                r510.append(e)
    return r51,r55,r510

def n1(x,f2):
    r11=[]
    r15=[]
    r110=[]
    c=0
    for a, b in f2:
    
        if(a == x and b!= None):
            c=c+1
            if(c==1):
                r11.append(b)
            if(c<=5):
                r15.append(b)
            if(c<=10):
                r110.append(b)
    return r11,r15,r110
