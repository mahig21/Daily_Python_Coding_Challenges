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
ans=is_golden_ratio(15,20)
print(ans)