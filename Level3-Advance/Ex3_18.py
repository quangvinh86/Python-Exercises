'''
Question:
A website requires the users to input username and password to register.
 Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
 check them according to the above criteria. Passwords that match the criteria
  are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1


Đề bài:
Một hệ thống cho phép password hợp lệ như sau:
1. Ít nhất có 1 ký tự [a-z]
2. Ít nhất có 1 số [0-9]
1. Ít nhất có 1 ký tự [A-Z]
3. Ít nhất có 1 ký tự đặc biệt [@#$%^&]
4. Độ dài ngắn nhất của password: 6
5. Độ dài dài nhất của password: 12
Hãy viết một chương trình cho phép kiểm tra password có hợp lệ hay không.

- Đầu vào:
Danh sách các password, cách nhau bởi dấu ,
- Đầu ra:
Danh sách các password hợp lệ, cách nhau bởi dấu ,

Ví du:
> ABd1234@1,a F1#,2w3E*,2We3345

> ABd1234@1
'''

import string


def check_valid_string_rule(password, rule_string):
    ''' Check every charaters of password at least in rule_string
    '   params: string, string
    '   rtype: bool
    '''
    return any([bool(single_char in rule_string) for single_char in password])


def check_valid_password(input_string):
    ''' Get a string that contains some password, separates by comma
    '   check valid password by 5 rules
    '   Params: String
    '   rtype: List of string
    '''
    passwords = input_string.strip().split(",")
    valid_password = []
    for password in passwords:
        if len(password) > 12 or len(password) < 6:
            continue
        else:
            if all([check_valid_string_rule(password, string.ascii_lowercase),
                    check_valid_string_rule(password, string.ascii_uppercase),
                    check_valid_string_rule(password, string.digits),
                    check_valid_string_rule(password, string.punctuation)]):
                valid_password.append(password)
    return valid_password


def main():
    input_string = "ABd1234@1,a F1#,2w3E*,2We3345,1q2w3e4rA@"
    print(input_string)
    print(','.join(check_valid_password(input_string)))


if __name__ == "__main__":
    main()
