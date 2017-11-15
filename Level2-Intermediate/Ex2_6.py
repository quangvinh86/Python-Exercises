'''
Question:
Write a program that calculates and prints the value according
 to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program
in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is
 given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off
 to its nearest value (for example, if the output received is 26.0,
  it should be printed as 26)
In case of input data being supplied to the question, it should be
 assumed to be a console input.


Câu hỏi:
Viết chương trình tính toán theo công thức:
Q = Square root of [(2 * C * D)/H]
Trong đó, giá trị mặc định ban đầu của C là 50, H là 30.

D là các giá trị được nhập vào các số nguyên cách nhau bởi dấu ,
In ra màn hình:
Các giá trị của Q.
Ghi chú: Trong trường hợp Q là một số thực (kiểu float), hãy lấy giá trị
 nguyên của số đó (không làm tròn)

Ví dụ:
Nhập vào:
100,150,180
Đầu ra
18,22,24

Gợi ý:
Phép toán "Square root" hay còn gọi là căn bậc 2.
Trong Python, phép toán này được xây dựng sẵn trong thưc hiện math.

Ghi chú:
Trong bài toán này có xây dựng một hàm để xử lý dữ liệu đầu vào.
Hạn chế việc nhập sai dữ liệu dẫn đến mất thời gian xử lý.
Có sử dụng đến hàm isditgit() đây là một "built-in method isdigit of str"
    Để kiểm tra xem một chuỗi có phải là một số nguyên không.
'''

import math

C = 50
D = 30


def calculate_value(numbers):
    ''' Calculate by formular: Q = Square root of [(2 * C * D)/H]
    ' params: list of integer
    ' rtype: list of integer
    '''
    Q = [int(math.sqrt((2 * C * D)/H)) for H in numbers]
    return Q


def recreate_input(input_str):
    '''function will remove some mistake of user input
    '  (eg: blank, string, not digit).
    '  And return correct list
    ' params: input string with comma-separated
    ' rtype: list of integer
    '''
    # remove all unused blank
    numbers = input_str.replace(",", " ").strip().split(" ")
    return [int(number) for number in numbers if number.isdigit()]


def main():
    try:
        input_str = input("Input a sequence of comma-separated numbers: ")
        numbers = recreate_input(input_str)
        print(calculate_value(numbers))
    except TypeError:
        print("Please input number only")


if __name__ == "__main__":
    main()
