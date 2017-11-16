'''
Question:
Write a program that accepts a sentence and calculate
 the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question,
 it should be assumed to be a console input.


Đề bài:
Viết một chương trình đầu vào là một chuỗi ký tự bất kỳ.
Yêu cầu:
- Đưa ra kết quả số lượng chữ cái, chữ số,
 ký tự đặc biệt trong chuỗi đó

Ví dụ:
> hello world! 123

> LETTERS 10
> DIGITS 3
> PUNCTUATIONS 1

Gợi ý:
- Built-in method của str có sẵn hàm isdigit, isisalpha
 nhưng không có hàm tìm ký tự đặc biệt.
- Trong thư viện string có cho phép hiển thị ký tự đặc biệt
string.punctuation
'''

import string


def count_char_in_string(input_string):
    '''Count all letter, number, punctuation in string
    ' Params: String
    ' Rtype: Dictionary
    '''
    count_char = {}
    count_char['DIGITS'] = 0
    count_char['LETTERS'] = 0
    count_char['PUNCTUATIONS'] = 0
    for single_char in input_string:
        if single_char.isdigit():
            count_char['DIGITS'] += 1
        elif single_char.isalpha():
            count_char['LETTERS'] += 1
        elif single_char in string.punctuation:
            count_char['PUNCTUATIONS'] += 1
    return count_char


def main():
    input_string = "Hello word! I'm a robot with ID 1001#$1002"
    print(input_string)
    print(count_char_in_string(input_string))


if __name__ == "__main__":
    main()
