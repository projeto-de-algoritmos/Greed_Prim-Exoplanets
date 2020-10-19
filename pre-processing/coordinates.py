import csv
import math

with open('pre-processing/planets_2020.10.18_11.32.38.csv') as csv_read, open('pre-processing/planets_xyz_values.csv', 'w+') as csv_write:
    csv_reader = csv.reader(csv_read, delimiter=',')
    csv_writer = csv.writer(csv_write, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            csv_writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
            line_count += 1
        else:
            if row:
                x = float(row[3]) * math.cos(math.radians(float(row[2]))) * math.sin(math.radians(float(row[1])))
                y = float(row[3]) * math.cos(math.radians(float(row[2]))) * math.cos(math.radians(float(row[1])))
                z = float(row[3]) * math.sin(math.radians(float(row[2])))
                csv_writer.writerow([row[0], row[1], row[2], row[3], x, y, z])
