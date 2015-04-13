"""
Definations of functions that get data from XML file using ClinVarSet ID. 

@author narumeena
@project ClinVar
@date 12/04/2015

@license MIT


"""
# import elementTree library
import xml.etree.ElementTree as ET
import logging as log
log.basicConfig(file='myapp.log', level=log.INFO)

#tree = ET.ElementTree(file="/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/ClinVarFullRelease_2015-04.xml")


#getting all Titles of variants from XML file 

def getAllTitles(filePath):
	tree = ET.ElementTree(file=filePath)
	# getting top-level elements
	root =tree.getroot()
	for clinVarSet in root.findall('ClinVarSet'):
		title = clinVarSet.find('Title').text;
		#clinVarAccession = clinVarSet.iterfind('ClinVarAccession').get('Acc')
		log.info("%s",title);

# get all RSV ClinVarAccession from XML data file 

def getAllClinVarRcvAccession(filePath):
	tree = ET.ElementTree(file=filePath);
	root = tree.getroot();	
	for clinVarAccession in root.iter('ClinVarAccession'):
		if clinVarAccession.get('Type') == "RCV":
			accession = clinVarAccession.get('Acc');
			version   = clinVarAccession.get('Version');
			accessionType = clinVarAccession.get("Type");
			dateUpdated = clinVarAccession.get('DateUpdated')
			log.info("RCV accession %s",accession)


# get all CSV ClinVarAccession from XML data file 

def getAllClinVarScvAccession(filePath):
	tree = ET.ElementTree(file=filePath);
	root = tree.getroot();
	for clinVarAccession in root.iter('ClinVarAccession'):
		if clinVarAccession.get('Type') == "SCV":
			accession = clinVarAccession.get('Acc');
			version   = clinVarAccession.get('Version');
			accessionType = clinVarAccession.get("Type");
			dateUpdated = clinVarAccession.get('DateUpdated')
			log.info("SCV accession %s",accession)

# get Record Status of XML data file 

def getReleaseSetStatus(filePath):
	tree = ET.ElementTree(file=filePath);
	root = tree.getroot();
	for release in root.iter('ReleaseSet'):
		dateUpdated = release.get('Dated');
		releaseType = release.get('Type');
		log.info("%s %s",dateUpdated,releaseType)

# get all Clinical Variant Set Ids from XML data file.

def getClinVarSetIDs(filePath):
	tree = ET.ElementTree(file=filePath);
	root = tree.getroot();
	for clinVarSetIds in root.iter('ClinVarSet'):
		clinVarId = clinVarSetIds.get('ID')
		log.info("%s",clinVarId)

# get status of record of Clinical Variant

def getRecordStatus(filePath):
	tree = ET.ElementTree(file=filePath);
	root = tree.getroot();
	for recordStatus in root.iter('RecordStatus'):
		status = recordStatus.text
		log.info("%s",status)
#def getObservationsByTitles(filePath):
#tree = ET.ElementTree(file=filePath)
# getting top-level elements
#root = tree.getroot()



# Path to the XML file
filePath = "/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/RCV000077146.xml"
#getAllTitles(filePath)
#getAllClinVarRcvAccession(filePath)
#getAllClinVarScvAccession(filePath)
#getReleaseSetStatus(filePath)
#getClinVarSetIDs(filePath)
getRecordStatus(filePath)




















