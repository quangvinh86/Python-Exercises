'''
Question:
Write a program that accepts a sentence and calculate
 the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question,
 it should be assumed to be a console input.


Đề bài:
Viết một chương trình đầu vào là một chuỗi ký tự bất kỳ.
Yêu cầu:
- Đưa ra kết quả số lượng chữ cái viết hoa, viết thường

Ví dụ:
> Hello world!

> UPPER 1
> LOWER 9

Gợi ý:
- Built-in method của str có sẵn hàm isupper, islower
- Dùng cách khởi tạo dictionary
'''


def count_case_in_string(input_string):
    '''Count all upper case, lower case in string
    ' Params: String
    ' Rtype: Dictionary
    '''
    count_char = {'UPPER': 0, 'LOWER': 0}
    for single_char in input_string:
        if single_char.isupper():
            count_char['UPPER'] += 1
        elif single_char.islower():
            count_char['LOWER'] += 1
    return count_char


def main():
    input_string = "Hello word! I'm a robot with ID 1001#$1002"
    print(input_string)
    print(count_case_in_string(input_string))


if __name__ == "__main__":
    main()
