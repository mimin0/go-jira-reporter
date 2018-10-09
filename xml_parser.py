import xml.etree.ElementTree as ET
def parseExport(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    stpoints = 0

    for items in root.iter('item'):
        #if "Sub-task" not in items.find('type').text:
        jira_id = items.find('key').text
        assigne = items.find('assignee').text
        
        # print('{},{},{}'.format(status, jira_id, assigne))
        for k in items.find('customfields'):
            m = k.attrib["id"]
            if "customfield_10002" in m:
                stpoints += float(k[1][0].text)
    
    return stpoints

done = parseExport('./done.xml')
not_done = parseExport('./notdone.xml')
# removed = 

total = done + not_done
finished_scope = int(done * 100 / total)

print("done: {}\nnot done: {}\nfinished scope: {}%".format(done, not_done, finished_scope))