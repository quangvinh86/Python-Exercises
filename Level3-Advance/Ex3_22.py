'''
Question:
Write a program to compute the frequency of the words from the input.
 The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? \
Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Đề bài:
Viết một chương trình nhận đầu vào là một chuỗi các từ.
Hãy tính số lần lặp lại của từng từ trong chuỗi.

Ví dụ:
New to Python or choosing between Python 2 and Python 3? \
Read Python 2 or Python 3.
Then, the output of the program should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Gợi ý:
- Sử dụng dictionary để lưu giữ các giá trị.
'''


def count_frequency(input_string):
    '''
    '   Params: string
    '   rtype: dictionary
    '''
    words_dict = {}
    for value in input_string.split(" "):
        if value in words_dict:
            words_dict[value] += 1
        else:
            words_dict[value] = 1
    return words_dict


def main():
    input_string = "New to Python or choosing between Python 2 and Python 3? "
    input_string += "Read Python 2 or Python 3."
    print(input_string)
    print(count_frequency(input_string))


if __name__ == "__main__":
    main()
