def water_jug(x,y,target):
    a,b=0,0
    while True:
        if a==target or b==target: break
        if a==0: a=x
        elif b==y: b=0
        else:
            t=min(a,y-b)
            a-=t; b+=t
        print(a,b)

water_jug(4,3,2)
