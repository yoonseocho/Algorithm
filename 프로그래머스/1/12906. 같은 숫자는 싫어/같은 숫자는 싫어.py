def solution(arr):
    ans = []
    for i in range(len(arr)):
        if ans and arr[i] == ans[-1]:
            continue
        ans.append(arr[i])
    return ans