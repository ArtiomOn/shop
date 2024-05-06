def upload_file(numbers):
    with open('numbers.txt', 'w') as f:
        for number in numbers:
            f.write(f'{number}\n')


upload_file([1, 2, 3, 4, 5])