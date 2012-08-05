import xml.etree.ElementTree as ET

def loadXMLFile(fileName):
  tree = ET.parse(fileName)
  root = tree.getroot()
  print root.tag
  return tree

def iterateTree(tree):
  iter = tree.iter()

  c = 0
  for elem in iter:
    print "elem: " + elem.tag
    c = c+1
    if c>10:
      if(elem.text):
        print "text: " + elem.text
      if(elem.keys()):
        print "has attribs: "
        print elem.keys() 
    if c>20:
      break

  return 0

def parseEntry(entryElem):
  
  return entry

tree = loadXMLFile("rtm-all-completed-tasks.xml")
iterateTree(tree)
