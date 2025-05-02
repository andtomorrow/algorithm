CROATIAN = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inpt_str = input()
inpt_str_copied = inpt_str

"""
CROATIAN의 요소가 inpt_str에 있는지 확인 후, 해당 내용을 상관없는 임의의 한 글자로 처리
"""

for croatian_char in CROATIAN:
    if croatian_char in inpt_str:
        inpt_str_copied = inpt_str_copied.replace(croatian_char, "*")

print(len(inpt_str_copied))
