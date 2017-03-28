import csv
import json

def generate_file(art_dict):
	content = '''"""This file is auto generated"""

class Record(obj_no):

	obj_dict = ''' + json.dumps(art_dict) + '''

	@staticmethod
	def get_obj_ID(obj_no):
		return Record.obj_dict[obj_no]
'''
	return content

if __name__ == '__main__':
	input_file = "ccma_artists/ccma_artists.json"
	output_file = "ccma_actor_id.py"

	art_dict = {}

	with open(input_file, "rU") as f:
		records = json.load(f)
		for record in records['artists']:
			art_dict[record[u'Display_Name']] = art_dict.get(record[u'Display_Name'],record[u'_Artist_ID'])

	with open(output_file, 'w') as f:
		f.write(generate_file(art_dict))