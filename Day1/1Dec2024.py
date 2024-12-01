import re

file = open('input1Dec2024.txt','r')
list1=[]
list2=[]

line = file.readline()
while line != '':
    values = [v for v in re.split(r'\s+|\n', line) if v] #List Comprehension
    list1.append(int(values[0]))
    list2.append(int(values[1]))

    line = file.readline()

list1.sort()
list2.sort()

def list_distance_count(list1, list2):
    temp_list1 = list1.copy()
    temp_list2 = list2.copy()

    total_distance = 0
    while temp_list1: #while the list is non-empty (both list have always the same number of elements)
            total_distance+= abs(temp_list1.pop(0) - temp_list2.pop(0)) #absolute value
    print('distance count =', total_distance)

def similarity_score(list1, list2):
    temp_list1 = list1.copy()
    temp_list2 = list2.copy()

    total_score = 0
    for n1 in temp_list1:
        counter = 0
        continue_flag = True
        for n2 in list2 :
            if continue_flag == True:
                if n2 == n1:
                    counter += 1
                elif n2 > n1:
                    continue_flag = False
                list2 = list2[list2.index(n2):]
        total_score += n1*counter
    
    print('similarity score =', total_score)

#alternative implementation (more efficient by using set's counter built-in function)
def similarity_score_2(list1,list2):
    temp_list1 = list1.copy()
    temp_list2 = list2.copy()

    total_score = 0
    for n1 in temp_list1:
        counter = temp_list2.count(n1)
        total_score += n1*counter

    print('similarity score =', total_score)


        


list_distance_count(list1, list2)
similarity_score(list1, list2)
similarity_score_2(list1,list2)





