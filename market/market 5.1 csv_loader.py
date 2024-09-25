
import csv
itemsname = 'market 0.5raw.csv'
categoriesname = 'market 0.5raw1.csv'

categoriesfields = ('id', 'name', 'longname', 'desc')
categoriesinfo = (
    ('TESC', 'monty', 'monty', ''),
)

itemfields = ('id', 'name', 'longname', 'category', 'cost', 'description')
iteminfo = (
    ('BE00', 'bean', 'beans', 'TESC', '1', 'beance'),
    ('EGG1', 'egg', 'fried egg', 'TESC', '2.1', 'uncooked fried egg'),
    ('20AD', 'toast', 'charred bread', 'TESC', '1.11', ''),
    ('PAM3', 'spam', 'canned spam', 'TESC', '20', 'insert ham copypasta here')
)

with open(itemsname, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(itemfields)
    csvwriter.writerows(iteminfo)

with open(categoriesname, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(categoriesfields)
    csvwriter.writerows(categoriesinfo)

with open(itemsname, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        print(row)

