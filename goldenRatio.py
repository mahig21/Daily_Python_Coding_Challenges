#20-07-26
"""
 * Given two numbers, determines if their ratio approximates the golden ratio.
  - Target golden ratio: 1.618
  - Allowed tolerance: 0.01
"""
def is_golden_ratio(a, b):
    if a>b:
        ratio=a/b
    else:
        ratio=b/a
    diff=abs(ratio-1.618)
    if diff<=0.01:
        return True
    return False
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
ans=is_golden_ratio(a, b)
print(ans)