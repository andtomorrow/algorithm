N = int(input())

m = 0
while True:
    m += 1
    m_str = str(m)
    sum_each = sum([int(m_str[i]) for i in range(len(m_str))])
    result_num = m + sum_each
    
    if result_num == N:
        print(m)
        break
    
    if m > N:
        print(0)
        break