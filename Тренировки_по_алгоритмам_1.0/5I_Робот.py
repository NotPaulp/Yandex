K=int(input())
operations=input()
pointer=0
count=0
while pointer+K<len(operations):
    matches = 0
    while operations[pointer]==operations[pointer+K]:
        matches+=1
        pointer+=1
        if pointer+K==len(operations):
            break
    pointer += 1
    if matches>0:
        count+=((1+matches)*matches)//2
print(count)
