import math


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = []
        closestPrimes = []
        distance = right - left + 1
        for num in range(left, right + 1):
            sqrt_num = int(math.sqrt(num))
            isPrime = num != 1
            for divisor in range(2, sqrt_num + 1):
                if num % divisor == 0:
                    isPrime = False
                    break

            if isPrime:
                primes.append(num)
                if len(primes) >= 2 and primes[-1] - primes[-2] < distance:
                    distance = primes[-1] - primes[-2]
                    closestPrimes = [primes[-2], primes[-1]]
                if distance <= 2:
                    return closestPrimes
        if len(primes) < 2:
            return [-1, -1]
        return closestPrimes
