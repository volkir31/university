coords = [int(input()) for i in range(4)]
print('YES' if (coords[0] + coords[1]) % 2 == (coords[2] + coords[3]) % 2 else 'NO')