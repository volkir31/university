digits = [int(input()) for i in range(2)]
sequence = [str(i) for i in range(min(digits), max(digits) + 1)]
print(' '.join(sequence) if digits[0] < digits[1] else ' '.join(sequence[::-1]))
