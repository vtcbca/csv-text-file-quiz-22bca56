import csv
data = [
    ["2", "om", "4000"],
    ["5", "sai", "4200"]
]

header = ["eid", "ename", "esalary"]
with open("salary.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("CSV file 'salary.csv' has been created with the following content:")
with open("salary.csv", mode="r") as file:
    for line in file:
        print(line.strip())



        
