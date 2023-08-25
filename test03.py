#input/ป้อนทางแป้นพิมพ์ ใฃ้ฟังก์ชั่น input() โดยสิ่งที่ป้อนเป็น string 

#ตัวแปร variable เป็น identifier
#identifier คือ ชื่อที่ dev. ตั้งชื่อมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
print('-----------------------')
print(f"ยินดีต้องรับ {std_id} ชื่อ {std_name}")
stdAge = 2023 - int(stdYearBorn)   #ต้องแปลง str เป็น number  -> int(), flot()
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge}")
print('-----------------------')
print("ยินดีต้อนรับ", std_id, "ชื่อ", std_name) 
print("คุณเกิดปี", stdYearBorn , "อายุ" , stdAge )
print('-----------------------')
print("ยินดีต้อนรับ "+ std_id, " ชื่อ "+ std_name)
print("คุณเกิดปี "+str(stdYearBorn)+' อายุ '+str(stdAge))
print('-----------------------')
print("ยินดีต้อนรับ {}  ชื่อ {} ".format(std_id,std_name))
print("คุณเกิดปี {} อายุ {} ".format (stdYearBorn,stdAge))
print('-----------------------')
print("ยินดีต้อนรับ %s  ชื่อ %s " %(std_id,std_name))
print("คุณเกิดปี %s อายุ %s " %(stdYearBorn,stdAge))
