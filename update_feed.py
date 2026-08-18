from xml.etree import ElementTree as ET

feed = ET.parse('feed.xml')

root = feed.getroot()

channel = root[0]

new_item = ET.Element('item')

new_item_title = ET.SubElement(new_item, 'title')
new_item_title.text = 'Teste 16'

new_item_link = ET.SubElement(new_item, 'link')
new_item_link.text = 'https://www.example.com/teste-16'

new_item_description = ET.SubElement(new_item, 'description')
new_item_description.text = 'Apenas o teste 16'

channel.insert(3, new_item)

channel.remove(channel[-1])

ET.indent(feed, '  ')

feed.write('new_feed.xml', encoding='utf-8', xml_declaration=True)
