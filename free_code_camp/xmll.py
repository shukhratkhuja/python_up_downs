import xml.etree.ElementTree as ET

data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
        +99891 777 49 64
        </phone>
        <email hide="yes"/>
    </person>
'''

tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))