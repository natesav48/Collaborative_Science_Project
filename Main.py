fruits = []
start_weights = []
end_weights = []

def get_data():
    while True:
        data_input_name = input("Enter the name of the fruit: ")
        data_input_start = float(input(f"Enter the starting weight of",data_input_name))
        data_input_end = float(input(f"Enter the ending weight of", data_input_name))

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

get_data()
calculate_weight_loss()

