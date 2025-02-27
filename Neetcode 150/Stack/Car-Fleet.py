class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda a: a[0])

        time = [(target - pos) / vel for pos, vel in pos_speed]
        n = len(position)
        car_fleets = 0 if n == 0 else 1
        max_time = time[-1]
        for i in range(n - 2, -1, -1):
            if time[i] > max_time:
                car_fleets += 1
                max_time = time[i]
        return car_fleets
