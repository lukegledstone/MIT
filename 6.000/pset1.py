prime_number_count = 0
num = 2

while prime_number_count <= 1000:
    if num % 2 != 0:
        for division in range(2, num//2):
            if num % division == 0:
                break
            else:
                print(num)
                prime_number_count += 1
    num += 1
print(prime_number_count)