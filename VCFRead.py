import quopri

def sortNum(num):
    for letter in num:
        if letter == '-':
            num = num.replace('-', '')
    if num[:3] == '+38':
        num = num.replace('+38', '')
    if num[:3] == '380':
        num = num.replace('38', '')
    if num[:2] == '+7':
        num = num.replace('+7', '7')
    return num

def readVCF(filename):
    arr = []
    with open(filename, 'r') as _file:
        file = list(_file)

    for i in range(len(file)):
        if file[i][:43] == 'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:':
            arr.append(dict())
            name = file[i][43:-1]
            if (file[i + 1][0] == '='):
                idx = i
                while (file[idx + 1][0] == '='):
                    name += file[idx + 1][:-1]
                    idx += 1
                for i in range(name.count('==')):
                    name = name.replace('==', '=')
            arr[-1]['Name'] = quopri.decodestring(name).decode('utf-8')
       
        if file[i][:9] == 'TEL;CELL:':
            arr[-1]['phone'] = sortNum(file[i][9:-1])
        if file[i][:5] == 'TEL;:':
            arr[-1]['phone'] = sortNum(file[i][5:-1])
        if file[i][:9] == 'TEL;HOME:':
            arr[-1]['phone'] = sortNum(file[i][9:-1])
    
    res = []
    for i in range(len(arr)):
        _keys = arr[i].keys()
        if not ('phone' in _keys):
            continue
    
        flag = True
        for contact in res:
            if arr[i]['phone'] == contact['phone']:
                flag = False
        
        if flag:
            res.append(arr[i])
    return res

def findTotal(fContacts, sContacts):
    result = []
    for fContact in fContacts:
        flag = False
        for sContact in sContacts:
            if fContact['phone'] == sContact['phone']:
                result.append('{0} - {1} - {2}'.
                format(fContact['Name'], sContact['Name'], fContact['phone']))
    return result

# myContacts = readVCF("contacts.vcf")
ariContacts = readVCF("contacts_ari.vcf")

# print(len(myContacts))

# result = findTotal(myContacts, ariContacts)

for line in ariContacts:
    print(line)

# for line in result:
#     print(line)