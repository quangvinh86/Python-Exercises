'''
Question:
Write a program which takes 2 digits, X,Y as input and generates
 a 2-dimensional array. The element value in the i-th row and j-th
  column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,..,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question,
 it should be assumed to be a console input
  in a comma-separated form.



Câu hỏi:
Viết chương trình nhận đầu vào là 2 số X,Y.
Tạo một mảng hai chiều:
- với X hàng và Y cột
- Giá trị tại vị trí [i,j] được tính bằng i*j

Ví dụ:
Input a sequence of comma-separated numbers:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Gợi ý:
Trong Python không có khái niệm mảng như các ngôn ngữ lập trình khác.
Việc sử dụng List cũng giống như mảng.

'''


def create_array(x_dimensional, y_dimensional):
    '''Create array with 2-dimensional
    ' params: x_dimensional, y_dimensional
    ' rtype: List with 2 dimensional
    '''
    xy_array = [[x * y for y in range(y_dimensional)]
                for x in range(x_dimensional)]
    return xy_array


def recreate_input(input_str):
    '''function will remove some mistake of user input
    '  (eg: blank, string, not digit).
    '  And return correct list
    ' params: input string with comma-separated
    ' rtype: list of integer
    '''
    # remove all unused blank
    numbers = input_str.replace(",", " ").strip().split(" ")
    return [int(number) for number in numbers if number.isdigit()]


def main():
    try:
        input_str = input("Input a sequence of comma-separated numbers: ")
        numbers = recreate_input(input_str)
        if not len(numbers) == 2:
            print("Please input 2 number")
        else:
            print(create_array(numbers[0], numbers[1]))
    except TypeError:
        print("Please input number only")


if __name__ == "__main__":
    main()
