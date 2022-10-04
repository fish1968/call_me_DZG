from yabiao_test import obtain_mylist, translate_from_idx_to_val, obtain_minimum_choice, get_second_data, enemy_combination


source_file_name = r"data.xlsx"
source_sheet = "my-data"
enemy_sheet = "enemy-ruizexiaowei"

output_file_name = "output.xlsx"

has_enemy_full_info = False
enemy_info =  [322, 321, 311, 212, 226]
enemy_sum = 1061
enemy_sums  = [17864, 1351, 1061]
chance_to_win = 0.95
error_rate = 0.00

# 如果有 两个 sum 的数据，根据组合应该可以降低可能的组合，因为不是独立的

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
enemy_dict = dict()
enemy_count = dict()

# enemy_sums = []


def main():
    has_best_choice = False
    obtain_mylist(excel_name = source_file_name, sheetname = source_sheet, names = my_names, values = my_values, debug=False)
    get_second_data( values = my_values, sum_list= my_powers,  power_count = my_power_sum_counter, data_dict = my_dict, debug = False)
    if not has_enemy_full_info:
        # obtain enemy infos
        obtain_mylist(excel_name=source_file_name, sheetname=enemy_sheet, names = enemy_names, values = enemy_values, debug = True)
        # guess combination of enemy
        enemy_dict = enemy_combination(enemy_sum=enemy_sum, enemy_values=enemy_values, error_rate = error_rate)
        
        # print out all guess 
        if enemy_dict["has_found"] == True:
            print("Congrates! You have found at least one combination for the enemy!")
        else:
            print("No close combination has found, there may have some mistakes for the enemy?")
        for error in range(-int(abs(enemy_sum * error_rate)), int(abs(enemy_sum * error_rate))+1):
            if enemy_dict.get(error, -1) != -1:
                num_of_combination = enemy_dict.get(error)[0]
                combination = enemy_dict.get(error)[1:]
                print(f"**** {num_of_combination} combinations have been found for error at {error}")
                print(f"\tThey are: ")
                for i in range(num_of_combination): # iteratre through all possible enempy combinations at this error and provide solutions of our warriors
                    print(end = "\t")
                    print(translate_from_idx_to_val(combination[i], enemy_names), combination[i], translate_from_idx_to_val(combination[i], values=enemy_values))
                    my_ans = obtain_minimum_choice(my_values=my_values, my_names=my_names, \
                                                    power_count=my_powers, my_data=my_dict, enemy_values = translate_from_idx_to_val(combination[i], values=enemy_values), \
                                                    probability = chance_to_win)
                    if my_ans != False:
                        my_ans_names = translate_from_idx_to_val(my_ans, my_names)
                        has_best_choice = True
                    if has_best_choice == True:
                        print(f"\tYour best choice is {my_ans_names}") 
                        print(f"\tThe total power sum is {sum(translate_from_idx_to_val(my_ans, my_values))}")
                    else:
                        print("\tSorry :< No chance of winning for sure")
                    print()
                    has_best_choice = False
                    
    else: # has enemy's full info 
        # iteratre through all guess
        my_ans = obtain_minimum_choice(my_values=my_values, my_names=my_names, \
            power_count=my_powers, my_data=my_dict, enemy_values = enemy_info, \
                probability = chance_to_win)
        if my_ans != False:
            my_ans_names = translate_from_idx_to_val(my_ans, my_names)
            has_best_choice = True
        if has_best_choice == True:
            print(f"Your best choice is {my_ans_names}") 
            print(f"The total power sum is {sum(translate_from_idx_to_val(my_ans, my_values))}")
        else:
            print("Sorry :< No chance of winning for sure")
if __name__ == "__main__":
    main()