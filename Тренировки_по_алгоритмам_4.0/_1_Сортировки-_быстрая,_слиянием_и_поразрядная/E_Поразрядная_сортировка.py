def radix_sort(list1):
    phase = 0
    n=len(list1)
    k=len(list1[0])
    for digit in range(k-1,-1,-1):
        phase += 1
        new_list = [''] * n
        buckets = {}
        positions = {}
        keys=[chr(i) for i in range(ord('0'),ord('9')+1)]
        for key in keys:
            buckets[key] = list()
            positions[key] = 0
        for element in list1:
            buckets[element[digit]].append(element)
        for key_index,key in enumerate(keys):
            if key_index == 0:
                positions[key] = 0
            else:
                positions[key] = positions[keys[key_index-1]] + len(buckets[keys[key_index-1]])
        for element in list1:
            position=positions[element[digit]]
            new_list[position]=element
            positions[element[digit]]=positions[element[digit]]+1
        list1=new_list
        print("**********")
        print(f"Phase {phase}")
        for key in keys:
            bucket=buckets[key]
            bucket = ', '.join(bucket)
            if bucket=='': bucket='empty'
            print(f"Bucket {key}: {bucket}")
    print("**********")
    print("Sorted array:")
    print(', '.join(list1))
n=int(input())
list1=['']*n
for i in range(n):
    list1[i]=input()
print("Initial array:")
print(*list1,sep=", ")
radix_sort(list1)
