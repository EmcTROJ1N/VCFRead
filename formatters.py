def formatUkRuNum(phone):
    if (phone[0] == "*" or len(phone) < 4):
        return phone
    if phone.startswith("8"):
        phone = "7{}".format(phone[1:])
    if phone.startswith(tuple(["050", "071", "061"])):
        phone = "38{}".format(phone)
    return phone