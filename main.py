from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()

# http method [get, post, put, patch, delete]
# command db [find, insert, update, update, delete]


@app.get("/")  # get ข้อมูลออกมา #/ คือ root path
def index():
    return JSONResponse(
        content={"message": "Hello,  Pug and French World "}, status_code=200
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

# path#
# @app.get("/profile/{name}")
# def get_path_parameter(name:str):
# return JSONResponse(
# content={"message":f"My name is: {name}"},
# status_code=200,
# )


# query#
# @app.get("/profiles/")
# def get_query_parameter(start: int = 0, limit: int = 0): #query_parameter กำหนด default value เป็น type int รับค่าจาก url #ex. ?start=2&limit=8
# return JSONResponse(
# content={"message": f"profile start: {start} limit: {limit}"},
# status_code=200,
# )


# GET
# list of book#
# @app.get("/books") #รายชื่อหนังสือทั้งหมดใน database #ควรตั้งชื่อ path ตามชื่อ table ใน database
# def get_books():

# dict_books เป็นการไป query มาจาก database
# dict_books = [
# {
# "book_id": 1,
# "book_name": "Harry Potter and Philosopher's Stone",
# "page": 223,
# },

# {
# "book_id": 2,
# "book_name": "Harry Potter and the Chamber of Secrets",
# "page": 251,
# },

# {
# "book_id": 3,
# "book_name": "Harry Potter and the Prisoner of Azkaban",
# "page": 251,
# },
# ]

# retuen JSONResponse(content={"status":"ok", "data":dict_book},
# status_code=200)


# GET
# @app.get("/books/{book_id}") #แสดงหนังสือตาม id ของหนังสือที่กรอกไป ex. /books/5 #select * from books where id = book_id
# def get_books_by_id(book_id: int):
# book = {
# "book_id": 1,
# "book_name": "Harry Potter and Philisopher's Stone",
# "page": 223,
# }

# response = {"status":"ok", "data": book}

# return JSONResponse(content=response, status_code=200)


# create endpoint#
# Payload = body
# class createBookPayload(BaseModel): #ต้อง design BaseModel ก่อน คือ โครงสร้างในการ insert
# id: str
# name: str           # id, name, page is body
# page: int

# POST เปรียบเหมือนการ insert ข้อมูล
# @app.post("/books") #คือการ เพิ่ม books เข้าไป
# def create_books(req_body: createBookPayload):
# req_body_dict = req_body.dict() #convert to dict

# id = req_body_dict["id"]
# name = req_body_dict["name"]
# page = req_body_dict["page"]

# book = {
# "id": id,
# "name": name,
# "page": page,
# }

# response = {"status": "ok", "data": book} #response จะเป็นอะไรก็ได้ ใน data จะแสดงรายการที่เรา insert ไป
# return JSONResponse(content=response, status_code=201) #post ต้อง return 201

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
