#22-07-26
"""
Given an object representing a piggy bank, return the total value as a string
formatted as "$D.CC".

The object may contain any of the following:

| Coin      | Value |
|-----------|-------|
| pennies   | $0.01 |
| nickels   | $0.05 |
| dimes     | $0.10 |
| quarters  | $0.25 |
"""
coin_value= {
    "pennies": 0.01,
    "nickels": 0.05,
	"dimes": 0.10,
    "quarters": 0.25
}
def piggy_bank(coins):
    total=0
    for i in coins:
        total+=(coin_value[i]*coins[i])
    if total==0:
        return "$0.00"
    return "$"+str(round(total,2))
    
total=piggy_bank({})
print(total)