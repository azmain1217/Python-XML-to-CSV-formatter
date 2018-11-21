import xml.etree.ElementTree as ET
import csv

parse_file = input("Type in parse file name here.")
parse_name = parse_file + '.xml'
print("File to be parsed: " + parse_name + "\n")

tree = ET.parse(parse_name)
root = tree.getroot()

output_file = input("Type in output file name here.")
output_name = output_file + '.csv'
print("Output file name: " + output_name + "\n")

nyc_events = open(output_name, 'w')

csvwriter = csv.writer(nyc_events)

count = 0
nyc_head = []

for member in root.findall('event'):
 event = []
 if count == 0:
   name = member.find('name').tag
   nyc_head.append(name)
   description = member.find('description').tag
   nyc_head.append(description)
   date_created = member.find('date_created').tag
   nyc_head.append(date_created)
   csvwriter.writerow(nyc_head)
   count = count +1
  
 name = member.find('name').text
 event.append(name)
 description = member.find('description').text
 event.append(description)
 date_created = member.find('date_created').text
 event.append(date_created)
 csvwriter.writerow(event)

nyc_events.close()
print('Parsing completed!')
