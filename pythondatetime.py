#Date,Time
import datetime,pytz


x = datetime.datetime.now()

y = x.strftime("%Y")
m = x.strftime("%b")
d= x.strftime("%d")
print(y+"-"+m+"-"+d)
print(x.month)

#--------------------------------------------------------------------------
datez = x.strftime("%Y-%B-%d")
print(datez)

#--------------------------------------------------------------------------
tz = pytz.timezone('Asia/Bangkok') #Set time zone
def now(): #function
    now1 = datetime.datetime.now(tz)
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
    #[now1.month] คือ เรียกเดือนเป็นตัวเลขออกมา เช่น เดือน พ.ย ผลลัพธ์ที่ได้คือ 11 โดยจะนำ 11 ไปอ้างอิงจากผลลัพธ์ที่ split ออกมา ตำแหน่งที่ 11 คือ พ.ย
    thai_year = now1.year + 543
    time_str = now1.strftime('%H:%M:%S')
    return "%d %s %d %s"%(now1.day, month_name, thai_year, time_str) # 30 ตุลาคม 2560 20:45:30
    # %s สำหรับการแสดงผล String %f สำหรับการแสดงผล Float และ %d สำหรับการแสดงผล Integer
print(now())




