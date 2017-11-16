'''
Question:
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9


Đề bài:
Viết một chương trình đầu vào là một chuỗi các số cách nhau bởi dấu ,
Yêu cầu:
- In ra màn hình bình phương của các số lẻ trong chuỗi đầu vào
- Sử dụng list comprehension để hoàn thành bài


Ví dụ:
> 1,2,3,4,5,6,7,8,9

> 1,9,25,49,81

'''


def square_number_in_list(input_string):
    ''' Get a string that contains numbers separated by coma
    '   return a list of square odd number
    '   Params: String
    '   rtype: List
    '''
    return [int(number) * int(number) for number in
            input_string.strip().split(",") if int(number) % 2]


def main():
    input_string = "1,2,3,4,5,6,7,8,9"
    print(input_string)
    print(square_number_in_list(input_string))


if __name__ == "__main__":
    main()
