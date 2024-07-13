def asteroidCollision(asteroids: list[int]) -> list[int]:
    arr = [asteroids[0]]
    win = False
    for i in asteroids[1:]:
        while True:
            try:
                last = arr.pop()
            except:
                arr.append(i)
                break
            if i < 0 and last > 0:
                if abs(i) > last:
                    win = True
                elif abs(i) < last:
                    arr.append(last)
                    break
                else:
                    break
            else:
                arr.append(last)
                arr.append(i)
                if win:
                    win = False
                break
    return arr


print(asteroidCollision([8, -8]))
