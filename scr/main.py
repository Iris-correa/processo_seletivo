import os
from generator.file_input_generetor import file_save
from generator.report_generetor import process_file, save_file_top_five


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path_input = f"{current_dir}/files/orders_code.txt"
    file_path_output = f"{current_dir}/files/report_top_5.txt"

    file_save(file_path_input, 50)

    top_five_order = process_file(file_path_input)
    save_file_top_five(top_five_order, file_path_output)

# execution process function
if __name__ == "__main__":
    main()
 