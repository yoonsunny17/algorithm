while True:
    codes = input()
    reverse_codes = codes[::-1]
    if codes == '0':
        break
    else:
        if codes == reverse_codes:
            print('yes')
        else:
            print('no')