# Week 4 Lab
# Seamus de Cleir

# Import the ElementTree module
import xml.etree.ElementTree as ET

# Open file and parse it
tree = ET.parse('movies.xml')
# Get the root element and print it
root = tree.getroot()
print(root.tag)

# Print the child elements
for child in root:
    print(child.tag, child.attrib)

# Print the title of each movie
for movie in root.iter('movie'):
    print(movie.attrib['title'])

[print(elem.tag) for elem in root.iter()]
