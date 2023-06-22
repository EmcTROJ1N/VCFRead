from VCFContact import *
import quopri

class VCFCollection(object):

    def __init__(self, filename):
        self.Source = []
        vcfStr = ""
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                vcfStr += line
                if ("END:VCARD" in line.replace(" ", "").upper()):
                    contact = VCFContact(vcfStr)
                    self.Source.append(contact)
                    vcfStr = ""
    
    def __iter__(self):
        return iter(self.Source)

    def Print(self):
        for contact in self.Source:
            print(contact, end="\n\n")
    
    def GetArrProps(self, prop):
        return [getattr(contact, prop) for contact in self.Source]
    
    def SearchBy(self, prop, value):
        return [contact for contact in self.Source
                    if value in getattr(contact, prop)]
    
    def FormatPhones(self, formatter = None):
        removableSymbols = [" ", "+", "-", "(", ")"]
        
        for contact in self.Source:
            phones = []
            for phone in contact.PhoneNumbers:
                currentPhone = ''.join([char
                                for char in phone
                                    if char not in removableSymbols])
                if formatter != None:
                    currentPhone = formatter(currentPhone)
                phones.append(currentPhone)
            contact.PhoneNumbers = phones[:]
    
    def DecryptQuotedPrinableContacts(self):
        for contact in self.Source:
            if contact.Name.get("Encoding") == None:
                continue
            for key in contact.Name.keys():
                val = quopri.decodestring(contact.Name[key])
                val = val.decode(contact.Name["Charset"])
                contact.Name[key] = val
            del contact.Name["Encoding"]
            del contact.Name["Charset"]

    def DeleteDuplicates(self):
        idxs = []
        for i in range(len(self.Source) - 1):
            for j in range(i + 1, len(self.Source)):
                if self.Source[i].IsMathPhones(self.Source[j]):
                    self.Source[j].MergeContacts(self.Source[i])
                    idxs.append(i)
                    break
        idxs.reverse()
        for idx in idxs:
            self.Source.pop(idx)


    def FindMatchContacts(self, sourceCollection):
        match = []
        for destContact in self.Source:
            for sourceContact in sourceCollection:
                if destContact.IsMatchPhones(sourceContact):
                    match.append(sourceContact)
                    break
        return match