# list
def select_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                 min =j
        if i != min:
            list[i],list[min] = list[min],list[i]

list = [3,5,1,9,7]
print(list)
select_sort(list)
print(list)

