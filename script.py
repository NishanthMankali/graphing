import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Ask the user for the function, labels, and title
equation = input("Enter the equation (use 'x' as the variable): ")
x_label = input("Enter the x-axis label: ")
y_label = input("Enter the y-axis label: ")
title = input("Enter the graph title: ")

# Parse the user's equation
x = sp.symbols('x')
f = sp.lambdify(x, sp.sympify(equation), "numpy")

# Generate x values
x_vals = np.linspace(-10, 10, 400)  # Replace -10 and 10 with your range

# Generate y values
y_vals = f(x_vals)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y=' + equation)

# Set labels and title
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)

# Show legend
plt.legend()

# Display the plot
plt.show()
