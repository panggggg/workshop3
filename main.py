from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()  # FastAPI เป็น lib

# http method [get, post, put, patch, delete]
# command db [find, insert, update, update, delete]

# path ("/") ex. localhost:3001/ or 127.0.0.1:3001/
@app.get("/")  # get ข้อมูลออกมา #/ คือ root path
def index():
    return JSONResponse(
        content={"message": "Hello,  Pug and French World "}, status_code=200
    )  # content is dict, return status 200 is success


if __name__ == "__main__":  # check ว่าเป็น func main รึป่าว ถ้าเป็น run uvicorn
    uvicorn.run(
        "main:app", host="127.0.0.1", port=3001, reload=True
    )  # port สามารถกำหนดเป็นอะไรก็ได้ ไม่ควรกำหนดชน common port
    # reload = True คือ เหมาะกับตอน dev คอยเช็คตลอดว่าไฟล์มีการเปลี่ยนรึป่าว
    # reload = False คือ เหมาะกับตอน production เพราะกินทรัพยากร


############GET###########################
# path# #ex. localhost:3000/Pang #Output: My name is: Pang
# path 127.0.0.1:3001/proflie/Pang

# path parameter รับข้อมูลจาก path
@app.get("/profile/{name}")
def get_path_parameter(name: str):  # func get_path_params  name is variable
    print(name)
    return JSONResponse(
        content={
            "message": f"My name is: {name}"
        },  # {name} get from func and func get from path
        status_code=200,
    )


# query parameter#
@app.get("/profiles/")
def get_query_parameter(
    start: int = 0, limit: int = 0
):  # query_parameter กำหนด default value เป็น type int รับค่าจาก url #ex. ?start=2&limit=8
    print(start)
    print(limit)
    return JSONResponse(
        content={"message": f"profile start: {start} limit: {limit}"},
        status_code=200,
    )


# GET
# list of book#
@app.get(
    "/books"
)  # รายชื่อหนังสือทั้งหมดใน database #ควรตั้งชื่อ path ตามชื่อ table ใน database ดึงข้อมูลมาแสดงอย่างเดียว
def get_books():

    # dict_books เป็นการไป query มาจาก database
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    return JSONResponse(content={"status": "ok", "data": dict_books}, status_code=200)


# GET #      #get จะตามด้วย query_params
@app.get(
    "/books/{book_id}"
)  # แสดงหนังสือตาม id ของหนังสือที่กรอกไป ex. /books/5 #select * from books where id = book_id
def get_books_by_id(book_id: int):
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    book_filter = {}  # book_filter เป็นค่าว่าง
    for book in dict_books:  # loop ใน dict_books     #book เป็นตัวแปร
        if book["book_id"] == book_id:  # ["book_id"] นี่คือ list
            book_filter = book  # ถ้าเท่ากัน book_filter จะเท่ากับ book ถ้าไม่เท่ากันจะ return ค่าว่าง

    # การหา book ที่ id นั้นๆ ex.รับค่า book_id = 1 มาก็จะหาที่ id = 1
    # book_filter = list(filter(lambda book: book["book_id"] == book_id, dict_books))

    # validate result ตรวจสอบความถูกต้องของ result
    # result = (
    # book_filter[0] if len(book_filter) > 0 else {}
    # )  # ถ้าใส่ค่ามาถูกก็จะreturn ถ้าผิดก็จะreturnค่าว่าง

    response = {"status": "ok", "data": book_filter}

    return JSONResponse(content=response, status_code=200)


# create endpoint#
# Payload = body
# class สามารถนำไปใช้ในที่อื่นได้
# basemodel คือ class ที่ช่วยทำ payload ดีขึ้น
# createBookPayload exten from BaseModel


class createBookPayload(
    BaseModel
):  # ต้อง design BaseModel ก่อน คือ โครงสร้างในการ insert
    id: str
    name: str  # id, name, page is body
    page: int


# POST เปรียบเหมือนการ insert ข้อมูล
@app.post("/books")  # คือการ เพิ่ม books เข้าไป
def create_books(
    req_body: createBookPayload,
):  # req_body is argument ตามด้วย class ต้องส่ง request body มาเป็นแบบ createBookPayload
    req_body_dict = req_body.dict()  # convert to dict

    # ค่าที่ยิงมาจาก Postman
    # req_body_dict = {
    #   "id":"1",
    #   "name":"Python",
    #   "page":500
    # }

    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[  Log  ] id", id)
    print("[  Log  ] name", name)
    print("[  Log  ] page", page)

    book = {
        "id": id,
        "name": name,
        "page": page,
    }

    response = {
        "status": "ok",
        "data": book,
    }  # response จะเป็นอะไรก็ได้ ใน data จะแสดงรายการที่เรา insert ไป
    return JSONResponse(content=response, status_code=201)  # create สำเร็จ return 201


# request คือ สิ่งที่ต้องการให้ response ตอบกลับ


# update endpoint#
# class updateBookPayload(BaseModel):
# name: str
# page: int

# @app.patch("/books/{book_id}")
# def update_book_by_id(req_body: updateBookPayload, book_id: str):
# req_body_dict = req_body_.dict()

# name = req_body_dict["name"]
# page = req_body_dict["page"]

# print(f"name: {name}, page: {page}")

# update_message = f"Update book id {book_id} is complete !! "
# response = {"status": "ok", "data": update_message}
# return JSONResponse(content=response, status_code=200)


# delete endpoint#
# @app.delete("/books/{book_id}")
# def delete_book_by_id(book_id: int):
# delete_message = f"Delete book id {book_id} is complete !! "
# response = {"status": "ok", "data": delete_message}
# return JSONResponse(content=response, status_code=200)
