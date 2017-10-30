import xlrd
import os.path
from twilio.rest import Client


# Find these values at https://twilio.com/user/account
account_sid = "AC0037890d3482af7680de7a402c35c729"
auth_token = "e31bdd16760272ff46b3e1a7e7194e43"

client = Client(account_sid, auth_token)

wb = xlrd.open_workbook(os.path.join('C:\Users\yash\Desktop', 'data.xlsx'))
wb.sheet_names()
sh = wb.sheet_by_index(0)
no_of_columns = len(sh.row_values(0))

print sh.ncols
print sh.nrows

i=0

for i in range(1, sh.nrows):
    name = sh.cell(i, 0).value
    roll_no = sh.cell(i, 1).value
    mob_no = sh.cell(i, 2).value
    sub1 = sh.cell(i, 3).value
    sub2 = sh.cell(i, 4).value
    sub3 = sh.cell(i, 5).value
    sub4 = sh.cell(i, 6).value
    sub5 = sh.cell(i, 7).value
    total = sub1+sub2+sub3+sub4+sub5
    max_marks = sh.cell(i, 8).value
    percentage = total*100/max_marks    
    print name

    client.api.account.messages.create(
    to="+919680019800",
    from_="+919995902061",
    body="Hello there!")


