'''
Question:
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple


Câu hỏi:
Viết một chương trình nhập vào các số nguyên cách nhau bởi dấu ,
In ra màn hình:
- List chứa các số vừa nhập
- Tuple chứa các số vừa nhập

Ví dụ: 
Nhập vào:
34,67,55,33,12,98
Đầu ra
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Gợi ý:
Đây là bài toán sử dụng các hàm có sẵn của một chuỗi và tạo tuple
- Hàm str.split(express) --> trả về một LIST
- Tuple(list) --> trả về một tuple
'''


def main():
    input_str = input("Input a sequence of comma-separated numbers: ")
    numbers = input_str.split(",")
    print(numbers)
    print(tuple(numbers))


if __name__ == "__main__":
    main()
