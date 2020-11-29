from flask import Flask
from flask_restful import Api,Resource,abort

app=Flask(__name__)
api=Api(app)

#--------------------------------------------------------------------------------------

#แบบไม่มีพารามิเตอร์
#design
class weatherCity(Resource):
    def get(self):
        return {"ID":"1","Country":"Thailand","City":"Bangkok","Temperature":"33 OC"}

    def post(self):
        return {"ID":"2","Country":"Japan","City":"Tokyo","Temperature":"20 OC"}

#call
api.add_resource(weatherCity,"/weather")

#---------------------------------------------------------------------------------------

#แบบมีพารามิเตอร์
#design
class data(Resource):
    def get(self,name):
        return {"data":"Hello : "+name}


    def post(self,name):
        return {"ID":"Create Resorce : "+name}


#call ชนิด String
api.add_resource(data,"/data/<string:name>")


#---------------------------------------------------------------------------------------

#ร้องขอข้อมูลหรือสอบถามข้อมูล ระบุ จังหวัด ชนิด String
#dataset
mycity={
    "Bangkok":{"weather":"อากาศร้อน","Temperature":"40 OC","People":"15000"},
    "Ubon":{"weather":"อากาศหนาว","Temperature":"11 OC","People":"18800"},
    "Korat":{"weather":"อากาศเย็น","Temperature":"16 OC","People":"125000"},
    1:{"name":"Sakdinan","lastname":"khamnang"},
    2:{"name":"king","lastname":"kong"}
}

#design
class datacity(Resource):
    def get(self,namecity):
        return mycity[namecity]

    
#call ชนิด String
api.add_resource(datacity,"/datacity/<string:namecity>")

#---------------------------------------------------------------------------------------

#ร้องขอข้อมูลหรือสอบถามข้อมูล ระบุ จังหวัด ชนิด integer และเช็ค ค่าที่ส่งมาว่ามี ข้อมูลที่ขอมาไหม
#อย่างเช่น ใน dataset มี 2 ข้อมูล คือ 1 และ 2 แต่ร้องขอ 3 มา จะให้แสดงกลับไปว่าอะไร
#dataset
myname={
    1:{"name":"Sakdinan","lastname":"khamnang"},
    2:{"name":"king","lastname":"kong"}
}

def notFound(name_id):
    if name_id not in myname:
        abort(404,message="No data For id ")

#design
class Name(Resource):
    def get(self,name_id):
        notFound(name_id)
        return mycity[name_id]

    
#call ชนิด integer
api.add_resource(Name,"/name/<int:name_id>")

#------------------------------------------------------------------------------------

#Main Run
if __name__ == "__main__":
    app.run(debug=True)