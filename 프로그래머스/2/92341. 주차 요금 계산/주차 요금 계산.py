import math
from collections import defaultdict
def solution(fees, records):
    END = 23*60 + 59
    in_time = {}
    total_time = defaultdict(int)
    
    for record in records:
        time_str, car_num, status = record.split()
        h, m = time_str.split(":")
        time = int(h) * 60 + int(m)
        
        if status == "IN":
            in_time[car_num] = time
        else:
            total_time[car_num] += time - in_time.pop(car_num)
    
    for car_num, t in in_time.items():
        total_time[car_num] += END - t
    
    def calc_fee(t):
        if t <= fees[0]:
            return fees[1]
        return fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3]
  
    return [calc_fee(total_time[car]) for car in sorted(total_time)]