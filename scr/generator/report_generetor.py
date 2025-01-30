import os # Lib to access operating system commands

# return order number to identify each order and its total value
def process_line(line):
    try:
        order_number = line[0:10].strip()  
        order_quantity = int(line[10:15].strip())  
        unit_value = float(line[15:25].strip()) / 100 

        total_value = order_quantity * unit_value
        return order_number, total_value 
    except IOError as e:
        return print("An error occurred while opening to the file: {e}")

# read the file,  sort each tuple with total value (descending) and return top 5 highest values
def process_file(file_path):
    orders = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                order_number, total_value = process_line(line)
                orders.append((order_number, total_value))
        order_sorted = sorted(orders, key=lambda x: x[1], reverse=True)
        five_orders = order_sorted[:5]
        return five_orders
    except IOError as e:
        return print("An error occurred while opening to the file: {e}")


# save report in file output    
def save_file_top_five(top_five, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(f"Report: 5 Orders with the Highest Total Value:" + '\n')
            for order, total_value in top_five:
                file.write(f"{order:<15} R$ {total_value:,.2f}" + '\n')
    except IOError as e:
        print("An error occurred while writing to the file: {e}")
    else:
        print('File written successfully.')

