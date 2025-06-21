import csv

def read_csv(file_path):
    with open(file_path,mode='r') as file:
        return list(csv.DictReader(file))

def write_csv(file_path,data,fieldnames):
    with open(file_path,mode='w') as file:
       writer= csv.DictWriter(file,fieldnames=fieldnames)
       writer.writeheader()
       writer.writerow(data)
