from flask import Flask
from flask_restful import Resource,Api,abort,reqparse,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy,Model

Myapp=Flask(__name__)


#database SQLITE DATABASE
database=SQLAlchemy(Myapp)
Myapp.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"

#API
api=Api(Myapp)


#สร้างตารางโดยใช้คำสั่ง python ไม่ต้องใช้สร้างเองหรือใช้คำสั่ง SQL
class CityModel(database.Model):
    id=database.Column(database.Integer,primary_key=True)
    name=database.Column(database.String(100),nullable=False)
    temp=database.Column(database.String(100),nullable=False)
    weather=database.Column(database.String(100),nullable=False)
    people=database.Column(database.String(100),nullable=False)

    #ใช้อ้างอิง
    def __repr__(self):
        return f"City(name={name},temp={temp},weather={weather},people={people})"

#คำสั่งใช้สร้างที่ออกแบบมา
database.create_all()

#Request parser
city_add_args=reqparse.RequestParser()
#add เพิ่ม argument ที่ต้องการจะเพิ่มเข้าฐานข้อมูลระบุให้ตรงกับที่เราสร้าง ชนิดข้อมูลถ้าไม่ถูกจะแสดงอะไร
city_add_args.add_argument("name",type=str,required=True,help="กรุณาป้อน City name")
city_add_args.add_argument("temp",type=str,required=True,help="กรุณาป้อน Temperature")
city_add_args.add_argument("weather",type=str,required=True,help="กรุณาป้อน Weather")
city_add_args.add_argument("people",type=str,required=True,help="กรุณาป้อน Num of people")


#Update request parser
city_update_args=reqparse.RequestParser()
city_update_args.add_argument("name",type=str,help="กรุณาป้อน City name ที่ต้องการแก้ไข")
city_update_args.add_argument("temp",type=str,help="กรุณาป้อน Temperature ที่ต้องการแก้ไข")
city_update_args.add_argument("weather",type=str,help="กรุณาป้อน Weather ที่ต้องการแก้ไข")
city_update_args.add_argument("people",type=str,help="กรุณาป้อน Num of people ที่ต้องการแก้ไข")

#add field เพื่อรุบุเวลาจะเพิ่มเข้า DB หรือร้องขอ
Resource_field={
    "id":fields.Integer,
    "name":fields.String,
    "temp":fields.String,
    "weather":fields.String,
    "people":fields.String
}




#Resource
class weatherCity(Resource):
    #ระบุอ้างอิงจาก Resorce field
    @marshal_with(Resource_field)
    def get(self,City_id):
        result=CityModel.query.filter_by(id=City_id).first()
        if not result:
            abort(404,message="ไม่พบข้อมูลจังหวัดที่คุณร้องขอ")
        return result

    @marshal_with(Resource_field) #ระบุอ้างอิงจาก Resorce field
    def post(self,City_id):
        #ใช้ตรวจสอบก่อนบันทึกว่ามี id ซ้ำไหมถ้าซ้ำก็แสดง รหัสนี้เคยบันทึกแล้ว
        result=CityModel.query.filter_by(id=City_id).first()
        if result:
            abort(409,message="รหัสนี้เคยบันทึกแล้ว")
        args=city_add_args.parse_args()
        #สร้าง obj จาก citymodel
        city=CityModel(id=City_id,name=args["name"],temp=args["temp"],weather=args["weather"],people=args["people"])
        database.session.add(city)
        database.session.commit() 
        return city,201
    
    @marshal_with(Resource_field)
    def patch(self,City_id):
        args=city_update_args.parse_args()
        result=CityModel.query.filter_by(id=City_id).first()
        if not result:
            abort(404,message="ไม่พบข้อมูลที่ต้องการแก้ไข")
        if args["name"]:
            result.name=args["name"]
        if args["temp"]:
            result.temp=args["temp"]
        if args["weather"]:
            result.weather=args["weather"]
        if args["people"]:
            result.people=args["people"]
        
        database.session.commit()
        return result
        

#call
api.add_resource(weatherCity,"/weather/<int:City_id>")


if __name__ == "__main__":
    Myapp.run(debug=True)