import xml.etree.ElementTree as ET

def tryParse():
  root = ET.Element("html")

  head = ET.SubElement(root, "head")
  title = ET.SubElement(root, "title")
  title.text = "Page Title"

  tree = ET.ElementTree(root)
  return tree

tree = tryParse()
ET.dump(tree)

