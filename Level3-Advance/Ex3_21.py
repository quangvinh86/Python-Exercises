'''
Question:
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given
steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program
 to compute the distance from current position after a sequence of
  movement and original point. If the distance is a float, then
   just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Đề bài:
Một robot được lập trình di chuyển trên một hệ tọa độ (X,Y).
Bắt đầu từ vị trí (0,0), mỗi lần di chuyển, robot chỉ đi được một
hướng với một số bước.
Ví dụ:
UP 5 --> Di chuyển 5 bước về phía Y+ đến tọa độ (0, 5)
DOWN 3 --> Di chuyển 3 bước về phía Y- đến tọa độ (0, 2)
LEFT 3 --> Di chuyển 3 bước về X- đến tọa độ (-3, 2)
RIGHT 2 --> Di chuyển 2 bước về X+ đến tọa độ (-1, 2)

Yêu cầu: Viết một chương trình tính khoảng cách sau một số bước đi
 của robot đến vị trí ban đầu. (nếu khoảng cách là số thực, chuyển
 nó về số nguyên)
Giả sử các bước đi được nhập từ bàn phím hoặc nhập sẵn trong file.

Ví dụ:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Gợi ý:
- Sử dụng tuple, list để lưu vị trí của robot
- Khoảng cách chính là đường chéo trong tam giác vuông.
Có thể tính ra bằng công thức pitagos c^2 = a^2 + b^2
'''

import math


STEP_OF_ROBOT = "UP 5\nDOWN 3\nLEFT 3\nRIGHT 2"


def calculate_distance(input_string):
    '''
    '   Params: string
    '   rtype: int
    '''
    steps = [step.split(" ") for step in input_string.split("\n")]
    robo_pos = [0, 0]
    for step in steps:
        if step[0] == 'UP':
            robo_pos[1] += int(step[1])
        elif step[0] == 'DOWN':
            robo_pos[1] -= int(step[1])
        elif step[0] == 'LEFT':
            robo_pos[0] -= int(step[1])
        elif step[0] == 'RIGHT':
            robo_pos[0] += int(step[1])
        else:
            break
    return int(math.sqrt(robo_pos[0] * robo_pos[0] +
                         robo_pos[1] * robo_pos[1]))


def main():
    input_string = STEP_OF_ROBOT
    print(input_string.split("\n"))
    print(calculate_distance(input_string))


if __name__ == "__main__":
    main()
