digits = [int(input()) for i in range(3)]
print( 3 if len(set(digits)) == 1 else 2 if len(set(digits)) == 2 else 0)