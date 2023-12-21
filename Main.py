import matplotlib.pyplot as plt
fruits = []
start_weights = []
end_weights = []
final_weight = []


def get_data():
    while True:
        data_input_name = input("Enter the name of the fruit: ")
        data_input_start = float(input("Enter the starting weight of "+data_input_name))
        data_input_end = float(input("Enter the ending weight of "+ data_input_name))

        fruits.append(data_input_name)
        start_weights.append(data_input_start)
        end_weights.append(data_input_end)

        more = input("Do you want to enter data for another fruit? (Y/N): ")
        if more.upper() != "Y":
            break

def calculate_weight_loss():
    print("Weight Loss:")
    for i in range(len(fruits)):
        weight_loss = start_weights[i] - end_weights[i]
        print("The",fruits[i], "lost", weight_loss, "grams of weight.")
        final_weight.append(weight_loss)


get_data()
calculate_weight_loss()


plt.figure(figsize=(10, 6))  # Adjust figure size if needed
plt.bar(fruits, final_weight, color='skyblue')
plt.xlabel('Fruits')
plt.ylabel('Weight Loss (grams)')
plt.title('Weight Loss of Fruits')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if necessary
plt.grid(axis='y')  # Add gridlines along the y-axis
plt.show()


