last=None
current=None

# ASCENDING – 5
# WEAKLY ASCENDING – 4
# CONSTANT – 3
# DESCENDING – 2
# WEAKLY DESCENDING – 1
# RANDOM – 0
state=None
while current!=-2000000000:
    if last!=None and (state==None or state>0):
        if current>last:
            if state==None:
                state=5
            else:
                if state<3:
                    state=0
                elif state==3:
                    state=4
        elif current<last:
            if state==None:
                state=2
            else:
                if state>3:
                    state = 0
                elif state==3:
                    state=1
        else:
            if state==None:
                state=3
            else:
                if state==5:
                    state=4
                elif state==2:
                    state=1


    last=current
    current=int(input())
if state==5:
    print("ASCENDING")
elif state==4:
    print("WEAKLY ASCENDING")
elif state==3:
    print("CONSTANT")
elif state==2:
    print("DESCENDING")
elif state==1:
    print("WEAKLY DESCENDING")
elif state==0:
    print("RANDOM")
