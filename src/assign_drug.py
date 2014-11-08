def assign_drug(filename):
    num = int(filename[-5])
    if num % 2 == 1:
        return "tylenol"
    else: 
        return "placebo"


assert assign_drug("inflammation_1.dat") == "tylenol" 
assert assign_drug("inflammation_10.dat") == "placebo"
assert assign_drug("inflammation_3.dat") == "tylenol"   