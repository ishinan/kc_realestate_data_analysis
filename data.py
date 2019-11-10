"""
data.py

Functions
---------

get_record_from_index(sourcefile, ind)

get_one_field_data(source_file, fieldname="")

get_all_data_from_source(source_file)
"""
import csv


def get_record_from_index(sourcefile, ind):
    '''
    parameters:
        sourcefile
        ind: index number
    return
        dict_of_one_record
    '''
    # Get all data
    # find index of the data
    fieldnames, all_records = get_all_data_from_source(sourcefile)
    record = {}
    for key, value_list in all_records.items():
        record[key] = value_list[ind] 
    return record
    

def get_one_field_data(source_file, fieldname=""):
    '''
    Return only one set of field data
    parameters:
        source_file
        fieldname
    return:
        list_of_dataset for one field
    '''
    data_list = []
    with open(source_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for record in csv_reader:
            data_list.append(record[fieldname])

    return [ int(i) for i in data_list ]


def get_all_data_from_source(source_file):
    '''
    get data from a csv file
    return a list of fields, and data 
        {
            'field01': [ value, value, value, ... ]
            'field02': [ value, value, value, ... ]
            'field03': [ value, value, value, ... ]
            ...
        }
    '''
    records = {}

    with open(source_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # This is a list of field names
        fieldnames = csv_reader.fieldnames
        for fieldname in fieldnames:
            records[fieldname] = []

        # Populating a dictionary for each field
        for record in csv_reader:
            for field in fieldnames:
                records[field].append(record[field])

    return [ fieldnames, records ]


def main():
    source_file = 'sac_realestate.csv'
    fieldname = "price"

    fieldnames, all_records = get_all_data_from_source(source_file )
    print(fieldnames, type(all_records))
    print(all_records[fieldname][0:5])

    record_set = get_one_field_data(source_file, fieldname)
    print(len(record_set))
    print(record_set[0:5])

    index = 0
    one_record = get_record_from_index(source_file, index)
    print(one_record)

if __name__ == "__main__":
    main()