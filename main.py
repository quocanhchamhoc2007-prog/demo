from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from seviver import (
    get_all,shearch_team_sv,get_by_id,post_class,put_class,delete_class,
)
from schema import create_class

app = FastAPI()


# 1 kiem tra sever
@app.get("/")
def test_get():
    return {"statusCode": 200, "error": None, "message": "API đang chạy", "data": None}


# 2 lay danh sach lop hoc phan
@app.get("/class-sections")
def get_all_class(db: Session = Depends(get_db)):
    team = get_all(db)
    return {
        "status_code": 200,
        "error": "null",
        "message": "lấy danh sách lớp học thành công",
        "data": team,
    }


# 3 tim kiem theo mon hoc
@app.get("/class-sections/search")
def search_team(subject_name: str, db: Session = Depends(get_db)):
    team = shearch_team_sv(subject_name, db)
    return {
        "statusCode": 200,
        "error": None,
        "message": "Lấy danh sách lớp học thành công",
        "data": team,
    }


# 4 lay chi tiet lop hoc phan
@app.get("/class-sections/{section_id}")
def get_class_by_id(section_id: int, db: Session = Depends(get_db)):
    team = get_by_id(section_id, db)
    return {
        "status_code": 200,
        "error": "null",
        "message": "lấy danh sách lớp học thành công",
        "data": team,
    }


# 5 them lop hoc phan
@app.post("/class-sections", status_code=201)
def add_class(new_class: create_class, db: Session = Depends(get_db)):
    team = post_class(new_class, db)
    return {
        "statusCode": 201,
        "error": None,
        "message": "Thêm lớp học phần thành công",
        "data": team,
    }


# 6 cap nhat lop hoc phan
@app.put("/class-sections/{section_id}")
def update_class(section_id: int, update: create_class, db: Session = Depends(get_db)):
    team = put_class(section_id, update, db)
    return {
        "statusCode": 200,
        "error": None,
        "message": "Cập nhật lớp học phần thành công",
        "data": team,
    }


# 7 xoa lop hoc phan


@app.delete("/class-sections/{section_id}")
def remove_class(section_id: int, db: Session = Depends(get_db)):
    delete_class(section_id, db)
    return {
        "statusCode": 200,
        "error": None,
        "message": "Xóa lớp học phần thành công",
        "data": None,
    }
