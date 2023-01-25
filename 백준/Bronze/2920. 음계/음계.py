c_maj_num = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']

cmn_len = len(c_maj_num)

c_maj_dct = {i+1 : c_maj_num[i] for i in range(cmn_len)}

usr_p_key = list(map(int, input().split()))
if usr_p_key == list(c_maj_dct.keys()):
    play_type = 'ascending'
elif usr_p_key[::-1] == list(c_maj_dct.keys()):
    play_type = 'descending'
else:
    play_type = 'mixed'

print(play_type)
