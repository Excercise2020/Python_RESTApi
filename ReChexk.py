import datetime,pytz
Timezone = pytz.timezone('Asia/Bangkok')

def now():
    datenow = datetime.datetime.now(Timezone)
    years = datenow.year+543
    x = "x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม"
    months = x.split()[datenow.month]
    day = datenow.day
    return years,months,day

print(now())
print("%d %s %d"%now())

#--------------------------------------------------------
Tz = pytz.timezone('Asia/Bangkok')
datez = datetime.datetime.now(Tz)
a = "x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม"
m = a.split()[datez.month]
y = datez.year+543
d = datez.day
print(y,m,d)