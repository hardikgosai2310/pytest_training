import pandas


def get_csv_as_list(file_path):
    csv_file = pandas.read_csv(file_path)
    return csv_file.values.tolist()
