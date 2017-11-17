'''
Question:
You are required to write a program to sort the (name, age, height) tuples
 by ascending order where name is string, age and height are numbers.
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
 ('Json', '21', '85'), ('Tom', '19', '80')]


Đề bài:
Viết một chương trình nhận đầu vào là các tuple gồm các thành phần:
name, age, score
Yêu cầu: Thực hiện sắp xếp các tuple theo thứ tự name > age > score

Ví dụ:
>Tom,19,80
>John,20,90
>Jony,17,91
>Jony,17,93
>Json,21,85

> [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
 ('Json', '21', '85'), ('Tom', '19', '80')]
'''


def unpack_score(input_string):
    items = input_string.split(",")
    return (items[0], int(items[1]), int(items[2]))


def sort_tuple(input_string):
    ''' sort list of tuple
    '   Params: String
    '   rtype: List of tuple affter sort
    '''
    scores = input_string.strip().split("\n")
    temp = [unpack_score(score) for score in scores]
    result = sorted(temp, key=lambda x: (x[0], x[1], x[2]))
    return result


def main():
    input_string = "Tom,19,80\n"
    input_string += "John,20,90\n"
    input_string += "Jony,17,91\n"
    input_string += "Jony,17,93\n"
    input_string += "Json,21,85"
    print(input_string)
    print(sort_tuple(input_string))


if __name__ == "__main__":
    main()
