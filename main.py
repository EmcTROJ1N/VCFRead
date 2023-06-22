from VCFCollection import *
from VCFContact import *
from formatters import *

if __name__ == "__main__":
    contacts = VCFCollection("contacts.vcf")

    # contacts.FormatPhones(formatUkRuNum)

    # Display names
    # for name in contacts.GetArrProps("Name"):
    #     print(name["FirstName"], name["AdditionalName"], name["LastName"], sep=" ")

    # Matching
    # for contact in contacts.FindMatchContacts(contacts):
    #     print(contact.Name["FirstName"], contact.Name["AdditionalName"], contact.Name["LastName"], sep=" ")

    # Search by key-val
    # for contact in contacts.SearchBy("Name", "Gump"):
    #     print(contact, end="\n\n\n")

    # Display phones
    # for phones in contacts.GetArrProps("PhoneNumbers"):
    #     print(phones)