"""
Definition of functions to parse clinVar XML data file

@author narumeena
@project ClinVar
@date 11/04/2015

@license MIT


"""
# import elementTree library
import elementtree.ElementTree as ET
import logging as log
log.basicConfig(file='myapp.log', level=log.INFO)
# reading the XML file
tree = ET.ElementTree(file="/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/RCV000077146.xml")

# getting top-level elements
root =tree.getroot()
log.info("%s",root)
log.info( "tag=%s, attrib=%s" ,root.tag, root.attrib)  # getting attributes of root element 



for child in root:
		log.info("tag=%s, attrib=%s", child.tag,child.attrib)