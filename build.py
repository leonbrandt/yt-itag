import pytablereader as ptr
import pytablewriter as ptw

data_path = "data.md"

reader = ptr.MarkdownTableFileLoader(data_path)
for table_data in reader.load(): res = table_data

csv_writer = ptw.CsvTableWriter()
csv_writer.headers = res.headers
csv_writer.value_matrix = res.rows

with open("data.csv", "w") as f:
	csv_writer.stream = f
	csv_writer.write_table()

for row in res.rows:
	for i, val in enumerate(row):
		if val == "": row[i] = None

json_writer = ptw.JsonTableWriter()
json_writer.headers = res.headers
json_writer.value_matrix = res.rows

with open("data.json", "w") as f:
	json_writer.stream = f
	json_writer.write_table()
