import xml.etree.ElementTree as ET

tree = ET.parse('./Sprint_6968.xml')
root = tree.getroot()
for items in root.iter('item'):
    if "Sub-task" not in items.find('type').text:
        jira_id = items.find('key').text
        assigne = items.find('assignee').text
        epic = items.find('customfieldfields').find('customfieldvalue')
        print('{} * {} :: {}'.format(epic, jira_id, assigne))