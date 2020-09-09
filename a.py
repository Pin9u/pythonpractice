def comb(list, r): #list 요소에서 x개를 뽑는 조합 구하기 nCr
    result = []
    if r > len(list):
        return result

    if r == 1:
        for i in list:
            result.append([i])

    elif r > 1:
        for i in range(len(list) - r + 1):
            for j in comb(list[i + 1:], r - 1):
                result.append([list[i]] + j)
    return result

def comb_sum(arr):
    arr = list(set(arr)) #set을 이용하여 중복된 요소 제거
    blank = []
    for i in range(1, len(arr)+1):
        blank += comb(arr, i) #반복문을 활용하여 nC1 + nC2 + --- +nCn 경우를 확인
    print(blank)

if __name__ == "__main__":
    comb_sum([1,1,2,3,4,5])
