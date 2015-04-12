"""
Definations of functions that get data from XML file using ClinVarSet ID. 

@author narumeena
@project ClinVar
@date 12/04/2015

@license MIT


"""
# import elementTree library
import elementtree.ElementTree as ET
import logging as log
log.basicConfig(file='myapp.log', level=log.INFO)

#tree = ET.ElementTree(file="/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/ClinVarFullRelease_2015-04.xml")


#log.info("%s",root.text)
#log.info( "tag=%s, attrib=%s",root.tag, root.attrib)  # getting attributes of root element 

#getting all titles of variants from XML file 

def getAllTitles(filePath):
	tree = ET.ElementTree(file=filePath)
	# getting top-level elements
	root =tree.getroot()
	for clinVarSet in root.findall('ClinVarSet'):
		title = clinVarSet.find('Title').text
		log.info("%s",title)

def getObservationsByTitles();
	tree = ET.ElementTree(file=filePath)
	# getting top-level elements
	root =tree.getroot()



# Path to the XML file
filePath = "/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/RCV000077146.xml"
getAllTitles(filePath)