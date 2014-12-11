"""
Import to List Wrapper
"""
import xml.etree.ElementTree as ET

class MktoList:
	def __init__(self, client, programName=None, listName=None, fieldnames=None):
		self.fieldNames=fieldnames
		self.rows=""
		self.client=client
		self.programName=programName
		self.listName=listName
		self.debug=False
	
	def submit(self):
		body = ("<ns1:paramsImportToList>" +
					"<programName>" + self.programName + "</programName>" +
					"<importListMode>UPSERTLEADS</importListMode>" +
					"<listName>"+self.listName+"</listName>"+
					"<clearList>false</clearList>"+
					"<importFileHeader>"+self.fieldNames+"</importFileHeader>"+
					"<importFileRows>"+self.rows+"</importFileRows>"+
				"</ns1:paramsImportToList>")
		if self.debug:
			flog = open('tmp/mktolog.xml', 'w+')
			flog.write(body)
		response=self.client.request(body)
		root = ET.fromstring(response.text)
		return root.find('.//importStatus').text
		
	def addRow(self, row):
		self.rows+="<stringItem>"+row+"</stringItem>"
	
	def setFieldNames(self, fieldnames):
		self.fieldNames=fieldnames
		
	def setProgram(self, programName):
		self.programName=programName
		
	def setList(self, listName):
		self.listName=listName

class MktoCustomObject:
	def __init__(self, client, fieldnames=None):
		'''
		MktoCustomObject constructor - fieldnames is an array of field names
		'''
		self.fieldNames=fieldnames
		self.customobjectxml = ""
		self.rows=""
		self.keys=""
		self.client=client
		self.debug=False

	def submit(self, customobjectxml):
		'''
		<attribute>
            <attrName>MKTOID</attrName>
            <attrValue>1090177</attrValue>
        </attribute>
		'''
		body = ("<ns1:paramsSyncCustomObjects>" +
					"<objTypeName>" + self.programName + "</objTypeName>" +
					"<customObjList>" + 
					self.customobjectxml +
					"</customObjList>" +
					"<operation>UPSERT</operation>" +
					"</ns1:paramsSyncCustomObjects>")
		if self.debug:
			flog = open('tmp/mktolog.xml', 'w+')
			flog.write(body)
		response=self.client.request(body)
		root = ET.fromstring(response.text)
		return None

	def addOneCustomObjectRow(self, row):
		'''
		builds customobjectxml for submission to marketo via the submit method
		fieldmap = [purchase+email, orderid, productname, productimg, qty, unitprice]
		rows = ['purchase+hendrerit.a.arcu@dolorNulla.ca.demo', '1098', 'Marketo Shirt', 'http://www.marketo.com/_assets/uploads/PageLayer-ProductMenuItem/6/_resampled/ColorizedImage02044-marketing-automation-newest.png?20140403145938', '5', '$95.99 ']
		'''
		attributes = ""
		for i in range(2,len(self.fieldNames)):
			attributes += "<attribute><attrName>" + self.fieldNames[i] + "</attrName><attrValue>" + row[i] + "</attrValue></attribute>"
		self.customobjectxml += ("<customObj><customObjKeyList><attribute><attrName>" + 
		                         self.fieldNames[0] + "</attrName><attrValue>" + 
		                         row[0] + "</attrValue></attribute><attribute><attrName>" + 
		                         self.fieldNames[1] + "</attrName><attrValue>" + 
		                         row[1] + "</attrValue></attribute></customObjKeyList><customObjAttributeList>" + 
		                         attributes + "</customObjAttributeList></customObj>")

	def setNames(self, headers):
		'''
		Takes in a row of column headings - [purchase+email, orderid, productname, productimg, qty, unitprice]
		and adds them to the instantiated object as fieldNames
		'''
		self.fieldNames = headers

	def addKeys(self, attribute):
		'''
		Takes an attribute as tuple and makes it a string of XML
		attribute = ('MKTOID','117')
		'''
		self.keys += "<attribute><attrName>"+attribute[0]+"</attrName><attrValue>"+attribute[1]+"</attrValue></attribute>"

	def addAttributes(self, attribute):
		'''
		Takes an attribute as tuple and makes it a string of XML
		attribute = ('bikecolor','red')
		'''
		self.rows += "<attribute><attrName>"+attribute[0]+"</attrName><attrValue>"+attribute[1]+"</attrValue></attribute>"

	def testXML(self):
		print self.customobjectxml

class MergeLeads:
	def __init__(self, client, typeofmerge):
		'''
		winningleadkeylist is like this [winner1, winner2, winner3]
		losingleadkeylist is like this [(loser1,anotherloser1,anotherloser1),(loser2, anotherloser2, anotherloser2),etc. etc.]
		'''
		self.type = typeofmerge
		self.winningleadkeylist = []
		self.losingleadkeylist = []
		self.winningleadxml = ''
		self.losingleadsxml = ''

	def submit(self):
		'''
		<attribute>
            <attrName>MKTOID</attrName>
            <attrValue>1090177</attrValue>
        </attribute>
		'''
		body = ("<ns1:paramsMergeLeads>" +
					"<winningLeadKeyList>" + self.winningleadxml + "</winningLeadKeyList>" +
					"<losingLeadKeyLists>" + 
					self.losingleadsxml +
					"</losingLeadKeyLists>" +
					"<operation>UPSERT</operation>" +
					"</ns1:paramsMergeLeads>")
		if self.debug:
			flog = open('tmp/mktolog.xml', 'w+')
			flog.write(body)
		response=self.client.request(body)
		root = ET.fromstring(response.text)
		return None

	def addonewinninglead(self, winningleadid):
		self.winningleadxml += ("<attribute><attrName>IDNUM</attrName><attrValue>" + winningleadid + "</attrValue></attribute>")

	def addonelosinglead(self, losingleadid):
		self.losingleadsxml += ("<keyList><attribute><attrName>IDNUM</attrName><attrValue>"+ losingleadid +"</attrValue></attribute></keyList>")

'''
<ns1:paramsMergeLeads>
      <winningLeadKeyList>
        <attribute>
          <attrName>IDNUM</attrName>
          <attrValue>2</attrValue>
        </attribute>
      </winningLeadKeyList>
      <losingLeadKeyLists>
        <keyList>
          <attribute>
            <attrName>IDNUM</attrName>
            <attrValue>15</attrValue>
          </attribute>
        </keyList>
        <keyList>
          <attribute>
            <attrName>IDNUM</attrName>
            <attrValue>16</attrValue>
          </attribute>
        </keyList>
      </losingLeadKeyLists>
</ns1:paramsMergeLeads>
'''



