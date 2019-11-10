# realestate_data_statistics.py

import data
import view
import analyze_statistics


def main():
    source_file = 'sac_realestate.csv'
    # Get a user request (expecting a list type, example: [ 'max', 'price' ])
    calc, field = view.menu()
    print(f"Selected Analysis: {calc}, {field}")

    # Get data set for analysis 
    result, list_index_of_records = analyze_statistics.analyze_data_from_source(source_file, calc, field)
    #list_index_of_records = analyze_statistics.get_index_from_value(dataset, result)

    records = []
    for i in list_index_of_records:
        records.append(data.get_record_from_index(source_file, i))
    print("Result: ",  result)
    print("Records: ", records)
 

if __name__ == "__main__":
    main()