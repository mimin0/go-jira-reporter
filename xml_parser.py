import xml.etree.ElementTree as ET
def parseExport(filename, status):
    tree = ET.parse(filename)
    root = tree.getroot()
    for items in root.iter('item'):
        #if "Sub-task" not in items.find('type').text:
        jira_id = items.find('key').text
        assigne = items.find('assignee').text
        # epic2 = items.find('customfields')
        epic = items.find('customfields')[5][1][0].text
        if "OCFD" not in epic:
            epic = items.find('customfields')[6][1][0].text
            print('{},{},{},{}'.format(status, epic, jira_id, assigne))
        else:
            print('{},{},{},{}'.format(status, epic, jira_id, assigne))

for i in ['./done.xml']:
    parseExport(i, "done")

for n in ['./notdone.xml']:
    parseExport(n, "not done")