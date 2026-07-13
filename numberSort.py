#15-06-26
#Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest.
def sort_numbers(s):
    num_list=[]
    nlist=s.split(",")
    for i in nlist:
        num_list+=[int(i)]
    num_list.sort()
    return num_list

string=input("Enter a string of numbers separated by commas: ")
num_list=sort_numbers(string) 
print(num_list)