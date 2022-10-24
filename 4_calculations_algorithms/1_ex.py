from math import sqrt


class QuadraticEquation:

    def __init__(self, a: float, b: float, c: float):
        # arg_list = [a, b, c]
        # pass_ = 0
        # for arg in arg_list:
        #     pass_ = 0
        #     if isinstance(arg, float):
        #         pass_ += 1
        # if pass_ == 3:
            self.a = a
            self.b = b
            self.c = c

    def solve(self):
        delta = self.b ** 2 - 4 * (self.a * self.c)
        if delta > 0:
            x1, x2 = (-self.b - sqrt(delta)) / (2 * self.a), (-self.b + sqrt(delta)) / (2 * self.a)
            return f"x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x0 = (-self.b) / (2 * self.a)
            return f"x0 = {x0}"
        elif delta < 0:
            return "No real roots of this equation"


ex = QuadraticEquation(1, -10, -8)
ex2 = QuadraticEquation(2, 8, 1)
solution = ex.solve()
solution2 = ex2.solve()
print(solution, "\n",
      solution2)

