#함수만들기
def final_sum(int_a):
    string_a = str(int_a)
    b = list(string_a)
    list_b = list(map(int, b))
    c = sum(list_b) + int_a
    return c

# 1 ~ 9999까지 리스트
ex_list = [ 0 for i in range(10000)]
for i in range(9998):
    ex_list[i] = i+1

# 리스트에서 함수값 제거?
for i in range(9998):
    test = final_sum(i)
    try:
        ex_list.remove(test)
    except ValueError:
        None

for i in range(9998):
    try:
        if ex_list[i] == 0:
            break
        print(ex_list[i])
    except IndexError:
        None