def is_even(number):
    """
    주어진 숫자가 짝수인지 확인하는 함수.

    Parameters:
    - number (int): 확인할 숫자.

    Returns:
    - bool: 주어진 숫자가 짝수이면 True, 홀수이면 False를 반환.
    """
    return number % 2 == 0

number_to_check = 10
result = is_even(number_to_check)

if result:
    print(f"{number_to_check}는 짝수입니다.")
else:
    print(f"{number_to_check}는 홀수입니다.")
