#import Element Tree XML API neeew
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import time
events = ET.iterparse("books.xml")
f = open("test.txt","w+")

def find_attribute(element, attribute):
  if attribute == "all":
    f.write("Element: " + element + "\n\nAttributes:\n")
    for event, elem in events:
      if elem.tag == element:
    # write() function only takes str not dict, so convert to string
        f.write(str(elem.attrib)+ "\n")
      elem.clear()
  elif element is not None and attribute is not None:
    f.write("Element: " + element + "\nAttribute Type: " + attribute + "\n\nAttributes:\n")
    for event, elem in events:
      if elem.tag == element:
        f.write(elem.attrib[attribute] + "\n")
      elem.attrib.clear()

def find_element_text(element):
  if element is not None:
    f.write("Element: " + element + "\n\nText:\n")
  for event, elem in events:
    if elem.tag == element:
      f.write(elem.text + "\n")
    elem.clear()

# def iterparse (file, element):
#   events = ET.iterparse(file)
#   for event, elem in events:
#     if elem.tag == element:
#       print(elem.text)
#   elem.clear()

def user_input():
    #get input and convert to lowercase for consistency
    answer = (input("Do you want to locate an attribute(y/n): ")).lower()
    if answer == 'y':
      element_attribute = input("Element: ")
      attribute = input("Attribute (or 'all'): ")
    else:
      element_attribute = None
      attribute = None
    
    answer = (input("Do you want to locate element text(y/n): ")).lower()
    if answer == 'y':
      element_text = input("Element: ")
    else:
      element_text = None
    return element_attribute, attribute, element_text

def main():
  element_attribute, attribute, element_text = user_input()
  start = time.time()
  find_attribute(element_attribute, attribute)
  f.write("------------------\n")
  find_element_text(element_text)
  end = time.time()
  print(end - start)
  f.close()

if __name__ == '__main__':
  main()
