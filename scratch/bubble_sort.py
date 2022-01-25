
def bubble_sort(list):
    for end in range(len(list) -1 , 0, -1):
        flag = 0
        for i in range(0, end):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                flag = 1
        if flag == 0:
            return

list = [3,5,1,9,7]
print(list)
bubble_sort(list)
print(list)
