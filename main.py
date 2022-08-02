from fastapi import FastAPI
from create_class import DbHelper
from api_base_model import User

app = FastAPI()


@app.get("/fetch")
async def get_student():
    obj = DbHelper().fetch_all()
    return obj


@app.get("/fetch_by_name")
async def get_student_with_name(name: str):
    username = name
    obj = DbHelper().fetch_by_name(username)
    return obj


@app.post("/create-user")
def create_user(input_json: User):
    userid = input_json.user_id
    username = input_json.name
    age = input_json.age
    DbHelper().insert_data(userid, username, age)
    return input_json


@app.delete("/delete-student/{student_id}")
def delete_user(userid: int):
    DbHelper().delete_user(userid)
    return {"message": "Student deleted successfully"}


@app.post("/update-user")
def update_user(input_json: User):
    user_id = input_json.user_id
    username = input_json.name
    age = input_json.age
    DbHelper().update_user(user_id, username, age)
    return input_json
