from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json


'''contact data container class'''
class Contact:
    def __init__(self, full_name, email, phone_number, is_friend):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend

    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} {'(Friend)' if self.is_friend else ''}"


'''our base class for reading file data'''
class FileReader(ABC) :
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass


'''abstract base class for all Contact Data Adapters'''
class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass


'''specific implementation of the adapter to read XML Source data'''
class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # parse XML data into an ElementTree object
        root = ET.fromstring(self.data_source.read()) # Read XML data from a file
        # extract contact information from the XML and create Contact objects
        contacts = []
        for elem in root.iter():
            if elem.tag == 'contact':
                full_name = elem.find('full_name').text
                email = elem.find('email').text
                phone_number = elem.find('phone_number').text
                is_friend = elem.find('is_friend').text.lower() == 'true'
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts


'''specific implementation of the adapter to read JSON Source data'''
class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # parse JSON data into a dictionary
        data_dict = json.loads(self.data_source.read()) # Read JSON data from a file
        # extract contact information from the dictionary and create Contact objects
        contacts = []
        for contact_data in data_dict['contacts']:
            full_name = contact_data['full_name']
            email = contact_data['email']
            phone_number = contact_data['phone_number']
            is_friend = contact_data['is_friend']
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts


'''specific implementation of the file reader to be used with XML Files'''
class XMLReader(FileReader):
    def read(self):
        # read the contents of the XML file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()


'''specific implementation of the file reader to be used with JSON files'''
class JSONReader(FileReader):
    def read(self):
        # read the contents of the JSON file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()


'''simple display routine to display Contact data to the console'''
def print_contact_data(contacts_source : ContactsAdapter):
    for contact in contacts_source.get_contacts():
        print(contact)


############################################################################
# Usage
############################################################################


xml_reader = XMLReader('contacts.xml')
# create an XML adapter and convert the data to a list of Contact objects
xml_adapter = XMLContactsAdapter(xml_reader)
# print the Contact objects
print_contact_data(xml_adapter)

json_reader = JSONReader('contacts.json')
# create a JSON adapter and convert the data to a list of Contact objects
json_adapter = JSONContactsAdapter(json_reader)
# print the Contact objects
print_contact_data(json_adapter)

# expected output
'''
Patric Doe (patric.doe@example.com) - 777-1234 (Friend)
Alex Smith (alex.smith@example.com) - 777-5678
John Doe (john.doe@example.com) - 555-1234 (Friend)
Jane Smith (jane.smith@example.com) - 555-5678
Darren Walker (d.walker@example.com) - 555-9999 (Friend)
'''
