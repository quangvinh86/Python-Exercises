'''
Question:
Write a program, which will find all such numbers
 between 1000 and 3000 (both included) such that
  each digit of the number is an even number.
The numbers obtained should be printed in a
 comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question,
 it should be assumed to be a console input.


Đề bài:
Viết một chương trình đầu vào:
- Các số từ 1000 đến 3000.
Yêu cầu:
- Tìm các số thỏa mãn điều kiện tất cả các con số
 trong số đều là số chẵn
- Thực hiện in ra cách nhau bởi dấu ,

Ví dụ:
> 2002, 2004, 2006

Gợi ý:
- Dùng vòng lặp for duyệt hàm range(1000, 3001) để lấy các số từ 1000-3000
- Chuyển số sang dạng chuỗi, sau đó lấy từng ký tự trong chuỗi
 để kiểm tra chia hết cho 2
- Hàm all(bool1, bool2, bool3,...) cho trả về:
 + True nếu tất cả các giá trị bên trong đều là True.
 + False nếu có ít nhất 1 giá trị là False
'''


BEGIN_NUMBER = 1000
END_NUMBER = 3000
OPERATOR_NUMBER = 2


def find_all_double_event(begin_number, end_number):
    '''Create a list that number in range BEGIN_NUMBER END_NUMBER
    '    and all digit of number is divisible for OPERATOR_NUMBER
    ' Params: Integer
    ' Rtype: List of string
    '''
    return [str(number) for number in range(begin_number, end_number + 1)
            if all([not int(i) % OPERATOR_NUMBER
                    for i in str(number)])]


def main():
    print(", ".join(find_all_double_event(BEGIN_NUMBER, END_NUMBER)))


if __name__ == "__main__":
    main()
