def sock_pairs(socks):
    count_pairs = 0

    A_socks = socks.count('A')
    B_socks = socks.count('B')
    C_socks = socks.count('C')

    exist_pair_A = A_socks > 1
    exist_pair_B = B_socks > 1
    exist_pair_C = C_socks > 1

    A_pairs = A_socks // 2
    B_pairs = B_socks // 2
    C_pairs = C_socks // 2


    if exist_pair_A:
        count_pairs += A_pairs

    if exist_pair_B:
        count_pairs += B_pairs
    
    if exist_pair_C:
        count_pairs += C_pairs            

    return count_pairs