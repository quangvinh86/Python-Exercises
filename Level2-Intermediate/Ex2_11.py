'''
Question:
Write a program which accepts a sequence of comma separated 4 digit
 binary numbers as its input and then check whether they are
  divisible by 5 or not. The numbers that are divisible by 5
   are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
0100,1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Chú ý: Từ bài này sẽ không sử dụng việc nhập vào từ bàn phím nữa.
Thay vào đó là mặc định một số giá trị sẵn.
Câu hỏi:
Viết một chương trình đầu vào:
- Các số có 4 chữ số được tạo bơi 0 & 1.
- Cách nhau bởi dấu ,
Xử lý: 
- Kiểm tra các số, in ra màn hình nếu chia hết cho 5.
- Nếu có nhiều số, thực hiện in ra cách nhau bởi dấu ,

Ví dụ: 
> 0100,0011,1010,1001

> 0100,1010

Gợi ý:
- Sử dụng hàm split để cắt dữ liệu.
- Nếu chuỗi sau khi đưa về dạng int, cần in lại dạng đủ 4 ký tự,
ta dùng hàm zfill.
'''


OPERATOR_NUMBER = 5

def create_divisible_list(input_str):
    '''Create a divisible list that all number in divisible list
    '   are divisible with OPERATOR_NUMBER
    ' Params: String
    ' Rtype: List of string
    '''
    divisible_list = []
    input_list = input_str.split(",")
    divisible_list = [number for number in input_list
                      if not int(number) % OPERATOR_NUMBER]
    return divisible_list


def main():
    input_str = '0100,0011,1010,1001,0010'
    print(input_str)
    print(",".join(create_divisible_list(input_str)))


if __name__ == "__main__":
    main()
