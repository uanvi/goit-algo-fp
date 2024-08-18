import numpy as np
import matplotlib.pyplot as plt

# Function to simulate dice rolls and calculate probabilities
def simulate_dice_rolls(num_rolls):

    dice1 = np.random.randint(1, 7, size=num_rolls)
    dice2 = np.random.randint(1, 7, size=num_rolls)
    
    sums = dice1 + dice2
    
    sum_counts = np.zeros(13)
    for roll_sum in sums:
        sum_counts[roll_sum] += 1
    
    probabilities = sum_counts / num_rolls
    
    return probabilities[2:]

# rolls count 
num_rolls = 100000

monte_carlo_probabilities = simulate_dice_rolls(num_rolls)

# Analytical probabilities 
analytical_probabilities = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36

# Comparation
sums = np.arange(2, 13)
comparison_table = np.vstack((sums, analytical_probabilities, monte_carlo_probabilities)).T

# Plot the results
plt.figure(figsize=(10, 6))
plt.bar(sums - 0.2, analytical_probabilities, width=0.4, label="Analytical", color='blue')
plt.bar(sums + 0.2, monte_carlo_probabilities, width=0.4, label="Monte Carlo", color='orange')
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability")
plt.title("Comparison of Analytical and Monte Carlo Probabilities")
plt.xticks(sums)
plt.legend()
plt.show()

comparison_table
