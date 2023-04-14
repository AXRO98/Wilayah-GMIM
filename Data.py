# © 2022 GMIM. Bidang Data Informatika & Litbang.
# Sumber Data Website https://dashboard.gmim.info/
# Update 11/04/2023 14:00:39

# import
import json
from prettytable import PrettyTable

# mengambil data 
file = open("data.json")
data = json.loads(file.read())

# membuat table
table = PrettyTable()
table.field_names = data[0].keys()
for row in data:
    table.add_row(row.values())

# mencetak
print("© 2022 GMIM. Bidang Data Informatika & Litbang.")
print(table)