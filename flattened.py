#01-03-26
#Given an array, determine if it is flat.
# -An array is flat if none of its elements are arrays.
def is_flat(arr):
    for i in arr:
        if isinstance(i, list): 
            return False
    return True

user_input = input("Enter an array (e.g., [1, 2, [3, 4]]): ")

try:

    arr = ast.literal_eval(user_input)
    if isinstance(arr, list):
        ans = is_flat(arr)
        print(ans)
    else:
        print("Error: Please enter a valid list format.")
        
except (ValueError, SyntaxError):
    print("Error: Invalid input. Make sure to use brackets and commas correctly.")