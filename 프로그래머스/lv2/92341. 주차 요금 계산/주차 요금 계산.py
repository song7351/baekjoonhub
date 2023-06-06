"""
기본시간, 기본요금, 단위시간, 단위요금
시간/ 번호/ IN/OUT
출차기록이 없으면 23시 59분에 출차함.
"""
def solution(fees, records):
    answer = []
    IN = {}
    time_ans = {}
    ans = []
    def calcul(in_time, out_time, number):
        time_in_h, time_in_m = list(map(int, in_time.split(":")))
        time_out_h, time_out_m = list(map(int, out_time.split(":")))
        tmp = (time_out_h - time_in_h)*60 + (time_out_m - time_in_m)
        if number in time_ans:
            time_ans[number] += tmp
        else:
            time_ans[number] = tmp
    
    for info in records:
        time, number, state = info.split()
        if state == "IN":
            IN[number] = time
        elif state == "OUT":
            calcul(IN[number], time, number)
            time_in_h, time_in_m = list(map(int, IN[number].split(":")))
            time_out_h, time_out_m = list(map(int, time.split(":")))
            del IN[number]
            
    for number, time in IN.items():
        calcul(IN[number], "23:59", number)
    
    for number, time in time_ans.items():
        pay = fees[1]
        setTime = time - fees[0]
        if setTime > 0:
            cnt = setTime // fees[2]
            if setTime % fees[2] != 0:
                cnt += 1
            pay += cnt*fees[3]
        ans.append([int(number), pay])
        
    ans.sort()
    
    for number, money in ans:
        answer.append(money)

    return answer