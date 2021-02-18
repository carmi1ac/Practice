import re
#This script is used to check a list of credentials (dumped on the darkweb or pastebin) for password policy matches.
#This script assumes the leaked list shows in the format of email@domain.com:password
#Copy and paste the list into a txt document and add the file path to open below
with open('<list you want to check>') as newlst:
    staticlist = newlst.readlines()
#Taking in the list of credentials and passwords   
    new_list = []
    for item in staticlist:
        new_item = item.strip('\n')
        new_list.append(new_item)

#checking for email addresses
#This part will check if the email address in the credential list matches the domain of your address in question.
#Once it finds the domain in question, it adds that credential item to a new list.
    second_list = []
    for element in new_list:
        if "@<domain>" in element:
            second_list.append(element)
#This section goes through and checks if the password is between 14 and 30 characters. This can be changed.
passwd1 = []
for item in second_list:
    if re.findall(r":\S{14,30}", item):
        passwd1.append(item)
#This section goes through the new list and checks if the policy is matched for uppercase, lowercase, digits, and special characters.
passwd2 = []
for item in passwd1:
    if re.findall(r":(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!%_*+?-])", item):
        passwd2.append(item)
#If all parameters are met, the credential item will be printed out.
print("\n")
print(passwd2)

print("\n")
print('---------The above credentials match the password policy---------')
print("\n")
input("Press Enter to exit")