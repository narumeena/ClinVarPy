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
#tree = ET.ElementTree(file="/Users/naru/Documents/aws_project/ClinVarPy/clinVarData/ClinVarFullRelease_2015-04.xml")

# getting top-level elements
root =tree.getroot()
log.info("%s",root.text)
log.info( "tag=%s, attrib=%s",root.tag, root.attrib)  # getting attributes of root element 




for level1 in root:
	log.info("Level 1")
	log.info("tag=%s, attrib=%s", level1.tag,level1.attrib)
	for level2 in level1:
		log.info("Level2 ")
		log.info("tag=%s, attrib=%s", level2.tag,level2.attrib)
		for level3 in level2:
			log.info("Level 3")
			log.info("tag=%s, attrib=%s", level3.tag,level3.attrib)
			for level4 in level3:
				log.info("Level 4")
				log.info("tag=%s, attrib=%s", level4.tag,level4.attrib)
				for level5 in level4:
					log.info("Level 5")
					log.info("tag=%s, attrib=%s", level5.tag,level5.attrib)
					for level6 in level5:
						log.info("Level 6")
						log.info("tag=%s, attrib=%s", level6.tag,level6.attrib)
						for level7 in level6:
							log.info("Level 7")
							log.info("tag=%s, attrib=%s", level7.tag,level7.attrib)
							for level8 in level7:
								log.info("Level 8")
								log.info("tag=%s, attrib=%s", level8.tag,level8.attrib)
log.info("len=%s, name = %s", len(root[0][2]),root[1][1].text)
























