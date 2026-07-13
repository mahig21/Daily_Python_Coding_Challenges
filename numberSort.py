#15-06-26
#Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest.
def sort_numbers(s):
    num_list=[]
    nlist=s.split(",")
    for i in nlist:
        num_list+=[int(i)]
    num_list.sort()
    return num_list

num_list=sort_numbers("5,3,8,1,9,2") 
print(num_list)