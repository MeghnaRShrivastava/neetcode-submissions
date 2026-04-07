class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        #Zero condition for the gradient descent
        if iterations ==0:
            return init

        y_predicted = float(init)
        for i in range(iterations):
            g = 2 * y_predicted
            y_predicted = y_predicted - learning_rate * (g)

        return round(y_predicted, 5)

