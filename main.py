import openpyxl
from functions import judge, cankill_montecarlo, debug
from test import obtain_mylist, translate_from_idx_to_val, obtain_minimum_choice, get_second_data
source_file_name = "test.xlsx"
source_sheet = "Sheet2"
output_file_name = "output.xlsx"

has_enemy_full_info = True


# place to hold Our and enemy's name & value pairs
my_names = []
my_values = []
my_powers = []
my_dict = dict()
my_power_sum_counter = dict()
my_ans = []
my_ans_names = []

enemy_names = []
enemy_values = []
enemy_sums = []
enemy_dict = dict()
enemey_count = dict()
enemy_info = [ 1000, 326, 284, 323, 295]


def main():
    has_best_choice = False
    obtain_mylist(excel_name = source_file_name, sheetname = source_sheet, names = my_names, values = my_values, debug=True)
    get_second_data( values = my_values, sum_list= my_powers,  power_count = my_power_sum_counter, data_dict = my_dict, debug = False)
    if has_enemy_full_info:
        my_ans = obtain_minimum_choice(my_values=my_values, my_names=my_names, \
            power_count=my_powers, my_data=my_dict, enemy_values = enemy_info)
        if my_ans != False:
            my_ans_names = translate_from_idx_to_val(my_ans, my_names)
            has_best_choice = True
    else:
        pass
    if has_best_choice == True:
        print(f"Your best choice is {my_ans_names}") 
        print(f"The total power sum is {sum(translate_from_idx_to_val(my_ans, my_values))}")
    else:
        print("Sorry :< No chance of winning for sure")

main()