import random # Lib to return random numbers

# This script return input positional file (.txt) with 50 lines.
def positional_lines(i):
    order_number = str(123 + i).zfill(10)  # return a unique order number (10 positions) starting 123. 
    quantity = str(random.randint(1, 20)).zfill(5) # return a random number between 1 and 20 (5 positions - order quantity). 
    unit_value = str(random.randint(1, 20000)).zfill(10) # return a random number between 1000 and 20000 (10 positions - unit value). 
    return order_number, quantity, unit_value


#save positional file - order_number (10 positions) + quantity (5 positions) + unit_value (10 positions)
def file_save(file_path, num_lines):
    try:
        with open(file_path, 'w') as file:
            for i in range(num_lines):
                order_number, quantity, unit_value = positional_lines(i)
                line = order_number + quantity + unit_value
                file.write(line + '\n')
    except IOError as e:
        print("An error occurred while writing to the file: {e}")
    else:
        print('File written successfully.')
