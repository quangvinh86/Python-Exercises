'''
Question:
Write a program that accepts a sequence of whitespace separated words
 as input and prints the words after removing all duplicate words and
  sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.



Câu hỏi:
Viết chương trình nhận đầu vào từ bàn phím:
 - Nhập vào một chuỗi các từ, cách nhau bởi dấu " "

In ra màn hình dữ liệu sau khi xử lý:
- Loại bỏ các từ trùng lặp
- Sắp xếp theo thứ tự alphanumerically

Ví dụ:

> hello world and practice makes perfect and hello world again


> again and hello makes perfect practice world


Gợi ý:
- Tách các từ thành 1 list.
- Dùng hàm set để loại bỏ các từ trùng lặp
Đầu ra sẽ là một set
- Dùng hàm sorted để sắp xếp.

Ghi chú: Trong Python, để sắp xếp 1 danh sách, có 2 cách sử dụng
Chúng khác nhau ở mục đích sử dụng và output
- temp_list.sort(): sắp xếp trực tiếp trong temp_list, thay đổi luôn
thứ tự các phần tử trong list
- sorted(temp_list): Sắp xếp và trả về 1 list mới, vị trí trong temp_list
không thay đổi.
'''


def remove_and_sort(input_text):
    input_list = input_text.split(" ")
    temp_list = sorted(set(input_list))
    return temp_list


def main():
    input_text = str(input("please input text (empty text to exit): \n"))
    print(remove_and_sort(input_text))


if __name__ == "__main__":
    main()
