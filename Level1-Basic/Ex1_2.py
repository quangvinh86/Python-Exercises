'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to
be a console input.


Câu hỏi:
Viết một chương trình tính giai thừa của các số nhập vào từ bàn phím.
Hiển thị theo cách dễ hiểu nhất có thể.

Gợi ý:
Đây là bài toán kép:
- Xử lý các dữ liệu nhập từ bàn phím
- Viết 1 hàm tính giai thừa theo công thức:
    fact(x) = x * (x-1)
- In ra bằng cách đẹp nhất là dùng dict với hiển thị 1:1
Ghi chú: Bài toán đơn giản, bỏ qua phần kiểm tra dữ liệu nhập vào
'''


def fact(number):
    '''function can compute the factorial of a given number
    ' params: int
    ' rtype: int
    '''
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)


def fact_numbers(numbers):
    '''function can compute the factorial of a given numbers
    ' params: list
    ' rtype: dictionary with struct of a element {number: factorial of number}
    '''
    dict_result = {}
    for number in numbers:
        dict_result[int(number)] = fact(int(number))
    return dict_result


def main():
    try:
        numbers_str = input("Input a sequence of space-separated numbers: ")
        numbers = numbers_str.split(" ")
        print(fact_numbers(numbers))
    except TypeError as ex:
        print("Type error, please input number only")


if __name__ == "__main__":
    main()
