def is_palindrome(my_str):
    if len(my_str) <= 1:
        return True
    if my_str[0] != my_str[-1]:
        return False
    else:
        return is_palindrome(my_str[1:-1])


# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))
