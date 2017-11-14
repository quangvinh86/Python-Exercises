#!/usr/bin/env python3
'''
Question:
Write a program which will find all such numbers which are
divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence
on a single line.

Hints:
Consider use range(#begin, #end) method

Câu hỏi:
Viết một chương trình tìm tất cả các số chia hết cho 7 nhưng không chia
 hết cho 5 nằm trong khoảng từ 2000 đến 3200.
Các số tìm được phải được in ra trên một dòng, cách nhau bởi một dấu ,

Gợi ý:
- Đầu bài đưa ra 2000 - 3200, 2 con số này được gọi là MAGIC_NUMBER
--> khai báo nó là GLOBAL VARIABLE (Biến toàn cục)
- Để lấy ra các số trong 1 khoảng, Python sử dụng hàm range(begin, end)
- Để in ra các số trên cùng 1 dòng --> đưa vào List và sử dụng hàm join
để in ra như 1 chuỗi.
'''

BEGIN_NUMBER = 2000
END_NUMBER = 3200


def find_all_number(begin_number, end_number):
    # Create list with list comprehension
    numbers = [str(number) for number in range(begin_number, end_number)
               if number % 7 == 0 and number % 5 != 0]
    print(', '.join(numbers))


def main():
    find_all_number(BEGIN_NUMBER, END_NUMBER)


if __name__ == "__main__":
    main()
