def solution(prices):
    count = 0
    output = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        output.append(count)
        count = 0
    return output