import math

def solution(fees, records):
    n = len(records)
    # records를 입차시간, 차량번호, 입/출 여부 로 나누기
    times = []
    car_nums = []
    in_or_out = []
    for record in records:
        split_record = record.split(" ")
        time = split_record[0].split(":")
        hour = int(time[0]) * 60
        minute = int(time[1])
        times.append(hour+minute)
        car_nums.append(split_record[1])
        in_or_out.append(split_record[2])
    
    # for time, car_num, in_out in zip(times, car_nums, in_or_out):
    #     print(time, car_num, in_out)
    
    # 누적 주차 시간 계산
    #car_fee = {5961:320, 0000:321}
    used_record = [False] * n
    car_fee = {}
    for car_num in car_nums:
        car_fee[car_num] = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if not used_record[i] and not used_record[j] and car_nums[i] == car_nums[j] and in_or_out[i] == "IN" and in_or_out[j] == "OUT":
                used_record[i] = True
                used_record[j] = True
                car_fee[car_nums[i]] += (times[j] - times[i])
                break
        else:
            if not used_record[i]:
                used_record[i] = True
                car_fee[car_nums[i]] += (60*23+59 - times[i]) #23:59
    
    # print(car_fee)
    
    # 주차 요금 계산
    final_car_fee = {}
    for car_num, time in car_fee.items():
        if time <= fees[0]:
            final_car_fee[car_num] = fees[1]
        else:
            over_time = time - fees[0]
            fee = fees[1] + math.ceil(over_time / fees[2]) * fees[3]
            final_car_fee[car_num] = fee
    # print(final_car_fee)
    
    # 차량번호가 작은 차부터 return
    answer = []
    for car_num in sorted(list(set(car_nums))):
        answer.append(final_car_fee[car_num])
    return answer