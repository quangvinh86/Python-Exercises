'''
Question
Write a program that accepts sequence of lines as input and prints the
 lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question,
 it should be assumed to be a console input.



Câu hỏi:
Viết chương trình nhận đầu vào từ bàn phím:
 - Nhập nhiều dòng
 - Kết thúc nhập nếu dòng trống.

In ra màn hình các dòng đã nhập được viết hoa

Ví dụ:

> Hello world
> Practice makes perfect

> HELLO WORLD
> PRACTICE MAKES PERFECT

Gợi ý:
- Sử dụng vòng lặp while để lặp đi lặp lại quá trình nhập dữ liệu.

Ghi chú: Trong Python, một chuỗi rỗng --> False
ví dụ:
empty_text = ""
bool(empty_text)  ---> False
'''


def while_loop_input():
    result = []
    input_text = str(input("please input text (empty text to exit): \n"))
    while input_text:
        result.append(input_text.upper())
        input_text = input("")
    return result


def main():
    print("\n".join(while_loop_input()))


if __name__ == "__main__":
    main()
