n = 3426
def print_digit(n):
    while(n>0):
        print(" ",n%10)
        n=n//10
print_digit(n)

def print_table(n):
    for i in range(n):
        print(n)