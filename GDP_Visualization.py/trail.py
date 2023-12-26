# We are working on this code which seperates the state which is better in the compared parameter more is to be done.
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'path/to/your/data.xlsx' with the actual path to your Excel file
excel_path = 'C:/Users/astey/Desktop/GDP_dataset.xlsx'

# Load data from Excel
df = pd.read_excel(excel_path)

# Display available parameters with numbers
parameter_dict = {index + 1: column for index, column in enumerate(df.columns)}

print("Available parameters:")
for number, parameter in parameter_dict.items():
    print(f"{number}. {parameter}")

# Ask the user for the numbers corresponding to the parameters they want to compare
chosen_numbers = input("Enter the numbers of the parameters you want to compare (comma-separated): ")
chosen_numbers = [int(number) for number in chosen_numbers.split(',')]

# Check if the chosen numbers are valid
invalid_numbers = [num for num in chosen_numbers if num not in parameter_dict]
if invalid_numbers:
    print(f"Error: Invalid numbers {invalid_numbers}. Please enter valid numbers.")
elif not (1 <= len(chosen_numbers) <= 3):
    print("Error: Please enter 1, 2, or 3 parameter numbers for comparison.")
else:
    chosen_parameters = [parameter_dict[number] for number in chosen_numbers]

    # Plot Grouped Bar Chart for chosen parameters
    plt.figure(figsize=(14, 8))
    num_chosen = len(chosen_parameters)
    bar_width = 0.6 / num_chosen  # Adjust this value based on your preference

    positions = range(len(df['State']))
    max_values = {}

    for i, chosen_parameter in enumerate(chosen_parameters):
        # Identify the state with the maximum value for the chosen parameter
        max_value_state = df[chosen_parameter].idxmax()
        max_values[chosen_parameter] = max_value_state

        # Create a list of colors for each bar
        colors = [f'C{i}' if idx != max_value_state else f'C{i}7' for idx in range(len(df))]

        # Plot bars with different colors
        plt.bar([pos + i * bar_width for pos in positions], df[chosen_parameter], label=chosen_parameter, color=colors, width=bar_width)

    # Display max values in the legend with different colors
    for parameter, max_value_state in max_values.items():
        plt.plot([], label=f'Max {parameter}', color=f'C{chosen_parameters.index(parameter)}7', linewidth=5)

    plt.xlabel('State')
    plt.ylabel('Values')
    plt.title(f'Comparison of Parameters by State ({", ".join(chosen_parameters)})')
    plt.xticks([pos + (num_chosen - 1) * bar_width / 2 for pos in positions], list(map(str, df['State'])), rotation=45, ha='right', fontsize=8)
    plt.legend()
    plt.tight_layout()
    plt.show()
