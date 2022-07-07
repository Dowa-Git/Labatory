def KMPSearch(src, search):
    n = len(src)
    m = len(search)
    
    ret = []
    pi = GetPartialMatch(search)

    begin = 0
    matched = 0
    while begin <= n - m:
        if matched < m and src[begin+matched] == search[matched]:
            matched+=1

            if matched == m:
                ret.append(begin)
        else:
            if matched == 0:
                begin+=1
            else:
                begin+=matched - pi[matched-1]
                matched = pi[matched-1]
    return ret


def GetPartialMatch(search):
    m = len(search)
    pi = [0 for i in range(0, m)]
    
    begin = 1
    matched = 0

    while begin + matched < m:
        if search[begin + matched] == search[matched]:
            matched+=1
            pi[begin+matched-1] = matched

        else:
            if matched==0:
                begin+=1
            else:
                begin+= matched - pi[matched - 1]
                matched = pi[matched - 1]
    print(pi)
    return pi


print(KMPSearch('QWEQWRTQAABAABACAASDF', 'AABAABAC'))
