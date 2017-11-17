'''
Question:
Define a class with a generator which can iterate the numbers,
 which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

Đề bài:
Viết một chương trình nhận đầu vào là một số, tạo ra một generator
chứa các số nhỏ hơn số vừa nhập và chia hết cho 7

Ví dụ:
>50
>
7
14
21
28
35
42
49

Gợi ý: Để tạo ra một generator, sử dụng từ khóa yield
'''


def create_generator(input_number):
    ''' create a generator of number
    '   Params: number
    '   rtype: nothing
    '''
    for number in range(1, input_number + 1):
        if not number % 7:
            yield number


def main():
    input_number = 50
    print(input_number)
    print()
    for number in create_generator(input_number):
        print(number)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
