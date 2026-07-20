class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        n = len(position)
        stack = list()

        for i in range(n):
            cars[position[i]] = speed[i]

        cars_sorted_rev = dict(sorted(cars.items(), key=lambda item: target-item[0]))

        for pos, sp in cars_sorted_rev.items():
            time = (target-pos)/sp
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
