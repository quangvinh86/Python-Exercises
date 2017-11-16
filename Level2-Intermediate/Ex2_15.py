'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa
 with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question,
 it should be assumed to be a console input.



Đề bài:
Viết một chương trình đầu vào là một số bất kỳ từ 1-9.
Yêu cầu:
- Tính kết quả của phép toán: a+aa+aaa+aaaa
Với a là số vừa nhập vào


Ví dụ:
> 9

> 11106


Gợi ý:
- Dùng format string để xử lý bài toán này
'''


def caculate_by_formula(number):
    ''' Get a single number (1-9) and caculate by formula:
    '   "a + aa + aaa+ aaaa"
    '   Params: Integer_single number
    '   rtype: Integer
    '''
    return sum([number, int("{}{}".format(number, number)),
                int("{}{}{}".format(number, number, number)),
                int("{}{}{}{}".format(number, number, number, number))])


def main():
    input_number = 9
    print(input_number)
    print(caculate_by_formula(input_number))


if __name__ == "__main__":
    main()
