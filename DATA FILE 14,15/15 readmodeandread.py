#Open the file in read mode and read the data .
import csv
with open('records.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    print("Header:", header)
    print("\nData rows:")
    for row in csv_reader:
        print(row)


# Open a file named “records.csv” in write mode (“w”) and write data into it.       
import csv
header = ['Name', 'Age', 'City']
data = [
    ['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 35, 'Paris']
]
with open('records.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)