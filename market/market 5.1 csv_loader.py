
import csv
filename = 'market 0.5raw.csv'

fields = ('id', 'name', 'longname', 'cost', 'description')
info = (
    ('BE00', 'bean', 'beans', 1, 'beans'),
    ('EGG1', 'egg', 'fried egg', 2.1, 'uncooked fried egg'),
    ('20AD', 'toast', 'charred bread', 1.11, ''),
    ('PAM3', 'spam', 'canned spam', 20, 'insert ham copypasta here')
        )

with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    csvwriter.writerows(info)

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        print(row)

