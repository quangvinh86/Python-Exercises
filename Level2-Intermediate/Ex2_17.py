'''
Question:
Question:
Write a program that computes the net amount of a bank account based
 a transaction log from console input. The transaction log format
  is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500


Đề bài:
Viết một chương trình đầu vào là chuỗi lấy từ
log các giao dịch tài khoản ngân hàng,
Có định dạng:

D 100
W 200

Với D là gửi vào, W là rút ra.
Yêu cầu:
- In ra màn hình số tiền còn lại trong tài khoản


Ví dụ:
>D 300
>D 300
>W 200
>D 100

> 500

'''


def computes_net_bank_account(input_string):
    ''' Get a string that contains transaction log from bank account
    '   return net amount of account
    '   Params: String
    '   rtype: Integer
    '''
    transactions = input_string.strip().split("\n")
    net_amount = 0
    for transaction in transactions:
        if transaction.split(" ")[0] == "D":
            net_amount += int(transaction.split(" ")[1])
        elif transaction.split(" ")[0] == "M":
            net_amount -= int(transaction.split(" ")[1])
        else:
            pass
    return net_amount


def main():
    input_string = "D 300\nD 200\nM 100\nD 300\nM 400"
    print(input_string)
    print(computes_net_bank_account(input_string))


if __name__ == "__main__":
    main()
