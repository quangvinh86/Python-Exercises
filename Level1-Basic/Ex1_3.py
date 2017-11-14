'''
Question:
With a given integral number n, write a program to generate 
a dictionary that contains (i, i*i) such that is an integral number
between 1 and n
(both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed
to be a console input.
Consider use dict()


Câu hỏi:
Viết một chương trình nhập vào một số nguyên N, In ra màn hình
một dictionary định dạng (i, i*i) trong đó i là các số từ 1 đến N.
Ví dụ: 
8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


Gợi ý:
Đây là bài toán kép:
- Xử lý các dữ liệu nhập từ bàn phím
- Tạo vòng lặp lần lượt append các giá trị của dict lại.
Ghi chú: Bài toán sử dụng nhập dữ liệu đầu vào bằng thư viện argparse
Để chạy được bài toán, sử dụng lệnh sau:
python Ex1_3.py [number]
ví dụ: 
python Ex1_3.py 10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
'''


def get_dictionary(number):
    dics = {}
    for value in range(1, number + 1):
        dics[value] = value * value
    return dics


def main():
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("number", help="display a square of a given number", type=int)
        number = parser.parse_args().number
        print(get_dictionary(number))
    except TypeError as ex:
        print("Type error, please input number only")


if __name__ == "__main__":
    main()
