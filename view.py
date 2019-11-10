"""
view.py

Functions
---------

menu(fields_list=[], calc_choices=[])
"""
import data
import analyze_statistics


def menu(fields_list=[], calc_choices=[]):
    '''
    1. Print menu
        1) largest room size
        2) average room size
        3) higest sales
    2. parse a user input
    3. return a list: example, [ "max", "sales" ] 
    '''
    # This is not used. In future, we can pick one from this list.   
    # This list could be passed as a parameter
    calc_choices =  [ 'max', 'min', 'mean', 'mode', 'median' ]

    menu = f"""
    1) Record of the largest size house
    2) Record of the smallest size house
    3) Rocord of the highest cost house
    4) Rocord of the lowest cost house
    -------------------------------
    """

    while True: 
       print(menu)
       user_input = input("Select number: ")
       if user_input == '1':
           return ['max', 'sq__ft', 'sqft'] 
       elif user_input == '2':
           return ['min', 'sq__ft', 'sqft'] 
       elif user_input == '3':
           return [ 'max', 'price', 'US$'] 
       elif user_input == '4':
           return [ 'min', 'price', 'US$'] 
       else:
           print("Cound't understand your input")


def main_test():
    reply = menu()
    print(f"Response: {reply}" )


def main_debug():
    source_file = 'sac_realestate.csv'
    # Get a user request (expecting a list type, example: [ 'max', 'price' ])
    calc, field, unit = menu()
    print(f"Selected Analysis: {calc}, {field}")

    # Get data set for analysis 
    result, list_index_of_records = analyze_statistics.analyze_data_from_source(source_file, calc, field)
    #list_index_of_records = analyze_statistics.get_index_from_value(dataset, result)

    records = []
    for i in list_index_of_records:
        records.append(data.get_record_from_index(source_file, i))
    print("Result: ",  result, unit)
    print("Records: ", records)


def main():
    source_file = 'sac_realestate.csv'
    # Get a user request (expecting a list type, example: [ 'max', 'price' ])
    calc, field, unit = menu()
    # Get data set for analysis 
    result, list_index_of_records = analyze_statistics.analyze_data_from_source(source_file, calc, field)
    #list_index_of_records = analyze_statistics.get_index_from_value(dataset, result)
    records = []
    for i in list_index_of_records:
        records.append(data.get_record_from_index(source_file, i))
    print("Result: ",  result, unit)


if __name__ == "__main__":
    main_debug()
    #main()