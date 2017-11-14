'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Câu hỏi:
Định nghĩa 1 lớp chứa ít nhất 2 phương thức:
- get_string: nhận dữ liệu string từ màn hình nhập
- print_string: in ra giá trị string ở dạng viết hoa
Viết chương trình test cho lớp vừa tạo

Gợi ý:
Trong hàm __init__ có thể khởi tạo một chuỗi với giá trị rỗng
Qua bài này, chúng ta có thể nắm được các khai báo một class trong Python
'''

class AutoUpperString():

    def __init__(self):
        self.value = ""

    def get_string(self):
        self.value = input("Please input everything: ")

    def print_string(self):
        print(self.value.upper())


def main():
    obj = AutoUpperString()
    obj.get_string()
    obj.print_string()


if __name__ == "__main__":
    main()
