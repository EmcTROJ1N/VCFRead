import re
import datetime

class VCFContact(object):
    def __init__(self, vcfStr):
        vcfArr = vcfStr.split("\n")
        vcfArr = list(filter(None, vcfArr))
        tmpVcf = [vcfArr[0]]
        
        for i in range(1, len(vcfArr)):
            if (len(tmpVcf[-1]) > 110 and vcfArr[i][0].isalpha() == False):
                if vcfArr[i][0] in ["=", " ", "\t"]:
                    tmpVcf[-1] += vcfArr[i][1:]
                else:
                    tmpVcf[-1] += vcfArr[i]
            else:
                tmpVcf.append(vcfArr[i])
        
        vcfArr = tmpVcf[:]
    
        if (vcfArr[0].replace(" ", "").upper() != "BEGIN:VCARD"):
            raise ValueError("Invalid data")
        vcfArr.pop(0)
        
        # VCF version
        if (re.match(r"VERSION: (3\.0|2\.1|4\.0|4\.1)", vcfArr[0]) == False):
            raise ValueError("Invalid data")
        self.VersionVCF = float(re.search(r"\d{1}.\d{1}", vcfArr[0]).group(0))
        vcfArr.pop(0)
        
        # Name

        FN = list(filter(re.compile(r"N.*:*").match, vcfArr))[0]
        initials = re.search(r":.*;.*;.*;.*;.*", FN).group(0)[1:].split(";")
        self.Name = dict(zip(
        [
            "LastName",
            "FirstName",
            "AdditionalName",
            "NamePrefix",
            "NameSuffix"
        ], initials))

        encoding = re.match(r"N;.*CHARSET=(.*);.*ENCODING=(.*):", FN)
        if encoding != None:
            self.Name["Charset"] = encoding.group(1)
            self.Name["Encoding"] = encoding.group(2)

        # Addresses
        self.Adresses = []
        for adr in list(filter(re.compile(r"ADR;.*").match, vcfArr)):
            self.Adresses.append(
                dict(zip(
                    ["PostOfficeAdress",
                     "Extended Adress",
                     "Street",
                     "Locality",
                     "Region",
                     "Postal code",
                     "Country"], re.search(r":.*;.*;.*;.*;.*;.*;.*", adr).group(0)[1:].split(";"))))
        
        # BDAY
        self.BDay = ""
        bday = list(filter(re.compile(r"BDAY:*").match, vcfArr))
        if (len(bday) > 0):
            self.BDay = bday[0][5:]

        # Email
        self.EMails = []
        for email in list(filter(re.compile(r"EMAIL.*:").match, vcfArr)):
            self.EMails.append(re.search(r":.*", email).group(0)[1:])

        # GEO
        self.GEO = dict()
        GEO = list(filter(re.compile(r"GEO:.*;.*").match, vcfArr))
        if (len(GEO) > 0):
            self.GEO = dict(zip(["latitude", "longitude"], map(float, GEO[0][4:].split(";"))))

        # LABEL
        self.Labels = []
        for label in list(filter(re.compile(r"LABEL.*:").match, vcfArr)):
            self.Labels.append(re.search(r":.*", label).group(0)[1:])

        # LANG
        self.Lang = ""
        lang = list(filter(re.compile(r"LANG:*").match, vcfArr))
        if (len(lang) > 0):
            self.Lang = lang[0][5:]

        # NOTE
        self.Notes = []
        for note in list(filter(re.compile(r"NOTE:.*").match, vcfArr)):
            self.Notes.append(re.search(r":.*", note).group(0)[1:])
        
        # PHONE
        self.PhoneNumbers = []
        regular = r".*TEL.*:"
        for phone in list(filter(re.compile(regular).match, vcfArr)):
            self.PhoneNumbers.append(phone.replace(re.search(regular, phone).group(0), ""))

        # TITLE
        self.JobTitles = []
        for title in list(filter(re.compile(r"TITLE:.*").match, vcfArr)):
            self.JobTitles.append(title[6:])

        # REV
        self.Revs = []
        for rev in list(filter(re.compile(r"REV:.*").match, vcfArr)):
            self.Revs.append(datetime.datetime.strptime(rev[4:], "%Y-%m-%dT%H:%M:%SZ"))

        # TZ
        self.TZ = ""
        tz = list(filter(re.compile(r"TZ:.*").match, vcfArr))
        if (len(tz) > 0):
            self.TZ = tz[0][3:]
        
        # Categories
        self.Caterories = []
        for category in list(filter(re.compile(r"CATEGORIES:.*").match, vcfArr)):
            self.Caterories.extend(category[11:].split(","))

        # PHOTO
        self.Photo = {}
        photo = list(filter(re.compile(r".*PHOTO.*").match, vcfArr))
        if (len(photo) > 0):
            photo = photo[0]
            photoRegular = re.search(r"\b(?:https?|ftp)://\S+\b", photo)
            if (photoRegular != None):
                self.Photo = photoRegular.group(0)
            else:
                photoPattern = re.match(r"PHOTO;ENCODING=(\w+);(\w+):(.+)", photo)
                self.Photo["Encoding"] = photoPattern.group(1)
                self.Photo["Format"] = photoPattern.group(2)
                self.Photo["Data"] = photoPattern.group(3)

    def IsMatchPhones(self, sourceContact):
        return len(list((set(self.PhoneNumbers) & set(sourceContact.PhoneNumbers)))) > 0
    
    def MergeContacts(self, sourceContact):
        self.Adresses.extend(sourceContact.Adresses)
        if self.BDay == None:
            self.BDay = sourceContact.BDay
        self.Caterories.extend(sourceContact.Categories)
        self.EMails.extend(sourceContact.EMails)
        if self.GEO == None:
            self.GEO = sourceContact.GEO
        self.JobTitles.extend(sourceContact.JobTitles)
        self.Labels.extend(sourceContact.Labels)
        if self.Lang == None:
            self.Lang = sourceContact.Lang
        if self.Name == None:
            self.Name = sourceContact.Name
        self.Notes.extend(sourceContact.Notes)
        self.PhoneNumbers.extend(sourceContact.PhoneNumbers)
        self.Revs.extend(sourceContact.Revs)
        if self.TZ == None:
            self.TZ = sourceContact.TZ

    def __str__(self):
        props = [f"{prop}: {getattr(self, prop)}" for prop in dir(self) if not callable(getattr(self, prop)) and not prop.startswith("__")]
        return "\n".join(props)