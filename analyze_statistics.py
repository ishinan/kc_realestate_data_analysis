"""
analyze_statistics.py

Functions
---------

analyze_data_from_source(source_file, calc, field)

analyze_data_from_dataset(stats_f="", data_set=[])

get_index_from_value(dataset=[], value="")
"""
import statistics
import data

def stats_max(data_set=[]):
    '''
    Return max number of data_set list
    It is same as max([ value, value, value,... ])
    '''
    return max(data_set)


def stats_min(data_set=[]):
    '''
    Return min number of data_set list
    It is same as min([ value, value, value,... ])
    '''
    return min(data_set)


def stats_mode(data_set=[]):
    '''
    Return mode of data_set list
    It is same as statistics.mode([ value, value, value,... ])
    '''
    return statistics.mode(data_set)


def stats_median(data_set=[]):
    '''
    Return median of data_set list
    It is same as statistics.median([ value, value, value,... ])
    '''
    #To find the median of a group of numbers:
    #    1. Arrange the numbers in order by size
    #    2. If there is an odd number of terms, the median is the center term.
    #    3. If there is an even number of terms, add the two middle terms and divide by 2.
    return statistics.median(data_set)


def stats_mean(data_set=[]):
    '''
    Return average of data_set list
    It is sum([ list_of_data ]) / len([ list_of_data ])
    It is same as statistics.mean([ value, value, value,... ])

    '''
    return sum(data_set) / len(data_set)

def analyze_data_from_source(source_file, calc, field):
    '''
    Retrieve user reqeust and data_sets, and calculate the results 
    parameters:
        source_file:
        calc: statistics calculation name such as max, min, mean, etc
        field: field to calculate
    return:
        Result [ reuslt, [ list_of_index_to_records ] ]
    '''
    stats_function_map = {
        'max': stats_max,
        'min': stats_min,
        'median': stats_median,
        'mean': stats_mean,
        'mode': stats_mode,
    }
    data_set = data.get_one_field_data(source_file, field)
    stats_func = stats_function_map[calc] 
    stats_result = stats_func(data_set)
    list_of_index = get_index_from_value(data_set, stats_result)

    return  [ stats_result, list_of_index ]


def analyze_data_from_dataset(stats_f="", data_set=[]):
    '''
    Retrieve user reqeust and data_sets, and calculate the results 
    parameters:
        stats_f: example 'max'
        data_sets: list[ ]
    return:
        Result [ 'calc_func(such as max)', 'fieldname', [ all_records_of_fields ] ]
    '''
    stats_function_map = {
        'max': stats_max,
        'min': stats_min,
        'median': stats_median,
        'mean': stats_mean,
        'mode': stats_mode,
    }
    stats_func = stats_function_map[stats_f] 
    stats_result = stats_func(data_set)

    return  stats_result 


def get_index_from_value(dataset=[], value=""):
    '''
    Get index of records from a value
    parameter:
        dataset
        value
    return:
        a list of indexes
            ex. [ 5, 10, ... ]
    '''
    return [ i for i, x in enumerate(dataset) if x == value ]


def main():
    # Static test
    calc = ['max', 'min', 'median' ]
    dataset = [ i for i in range(1, 1001) ]
    for c in calc:
        result = analyze_data_from_dataset(c, dataset)
        index = get_index_from_value(dataset, result)
        print(f"result: {result},  index of the record: {index}")


if __name__ == "__main__":
    main()