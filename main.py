# import Element Tree XML API
import xml.etree.ElementTree as ET
tree = ET.parse('H4_CONSOLIDATED_M4_REPORT.xml')
root = tree.getroot()
f = open("test.txt","w+")

def user_input():
  # get input and convert to lowercase for consistency
  answer = (input("Do you want to locate an attribute(y/n): ")).lower()
  if answer == 'y':
    # store user input in variables
    element_attribute = input("Element: ")
    attribute = input("Attribute (or 'all'): ")
  else:
    # if user does not want to search for attribute:
    element_attribute = None
    attribute = None

  #get input for next question
  answer = (input("Do you want to locate element text(y/n): ")).lower()
  if answer == 'y':
    # store element input in variable
    element_text = input("Element: ")
  else:
    element_text = None
  
  # return variables in a tuple
  return element_attribute, attribute, element_text

def find_attribute(element, attribute):
  # find all attributes of an element
  if attribute == "all":
    f.write("Element: " + element + "\n\nAttributes:\n")
    for child in root.iter(element):
    # write() function only takes str not dict, so convert to string
      f.write(str(child.attrib)+ "\n")
  # only find specified attribute for given element
  elif element is not None and attribute is not None:
    f.write("Element: " + element + "\nAttribute Type: " + attribute + "\n\nAttributes:\n")
    # iterate through elemens to find attribute
    for child in root.iter(element):
      # write to file
      f.write(child.attrib[attribute] + "\n")

def find_element_text(element):
  if element is not None:
    f.write("Element: " + element + "\n\nText:\n")
    for child in root.iter(element):
      f.write(child.text)

def main():
  # assign returned tuple values from user_input() to new variables
  element_attribute, attribute, element_text = user_input()
  # call function to find attribute
  find_attribute(element_attribute, attribute)
  f.write("------------------\n")
  # call function to find element text
  find_element_text(element_text)
  f.close()

if __name__ == '__main__':
  main()
