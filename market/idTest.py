catalog = [{id:0,'product':'a','quantity':1000,'price':2},{id:1,'product':'b','quantity':250,'price':5}]

for here in catalog:
    if here['product'] == 'a':
        catalog.remove(here)
print(catalog)
