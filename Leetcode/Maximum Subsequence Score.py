import heapq


def maxScore(nums1: list[int], nums2: list[int], k: int) -> int:
    arr = [(nums2[i], nums1[i]) for i in range(len(nums2))]
    arr = list(sorted(arr, key=lambda x: x[0]))
    max_score = 0

    for i in range(len(arr) - k + 1):
        score = 0
        n = arr[i][0]
        m = heapq.nlargest(k - 1, arr[i + 1 :], lambda x: x[1])
        m.append(arr[i])
        for key, val in m:
            score += val
        score *= n
        max_score = max(score, max_score)
    return max_score


print(maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
