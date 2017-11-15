'''
Question:
Write a program that accepts a comma separated sequence of words as
 input and prints the words in a comma-separated sequence after sorting
  them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be
 assumed to be a console input.


Câu hỏi:
Viết chương trình nhận đầu vào từ bàn phím là các từ cách nhau bởi dấu ,
Sắp xếp các từ theo thứ tự alphabe và in ra màn hình

Ví dụ:

> without,hello,bag,world
> bag,hello,without,world

Gợi ý:
Trong List của python có method bult-in sort sẽ tự động
sắp xếp các phần từ trong List.
'''


def main():
    input_str = input("Input a sequence of comma-separated string: ")
    list_str = input_str.strip().split(",")
    list_str.sort()
    print(list_str)


if __name__ == "__main__":
    main()
