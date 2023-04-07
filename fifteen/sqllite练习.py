#!/usr/bin/python3
# -*- coding=utf-8 -*-
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.orm import sessionmaker,declarative_base
from datetime import datetime
db_name = "sqllite3.db"
engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class UserHomeWork(Base):
    __tablename__ ='user_homework'
    id = Column(Integer,primary_key=True)
    student_name = Column(String(64),nullable=False,index=True)
    age = Column(Integer,nullable=False)
    homework_account = Column(Integer,nullable=False)
    last_update_time = Column(DateTime(timezone='Asia/Chongqing'),default=datetime.now())
    def __repr__(self):
        return f'学员姓名：{self.student_name} | 学员年龄：{self.age}'\
               f' | 作业数量：{self.homework_account} | 最后更新时间：{self.last_update_time}'
if __name__ == "__main__":
    session.query(UserHomeWork).delete()
    Base.metadata.create_all(engine,checkfirst=True)
    homework_dict = [
        {'student_name': '张三','age':37 ,'homework_account':1},
        {'student_name': '李四','age':33,'homework_account':5},
        {'student_name': '王五','age':32,'homework_account':10}
    ]
    for homework in homework_dict:
        homework_obj = UserHomeWork(**homework)
        session.add(homework_obj)
    session.commit()
    try:
        while True:
            print('请输入查询选项：')
            print('输入 1：查询整个数据库')
            print('输入 2：根据学员姓名查询')
            print('输入 3：根据学员年龄查询')
            print('输入 4：根据作业数量查询')
            print('输入 0：退出')
            option = input('请输入查询选项：')
            if option == '1':
                a = session.query(UserHomeWork).all()
                for row in a:
                    print(row)
            elif option == '2':
                a = input('请输入学员姓名：')
                b = session.query(UserHomeWork).filter(UserHomeWork.student_name == a).all()
                for row in b:
                    print(row)
            elif option == '3':
                a = input('搜索大于输入年龄的学员，请输入学员年龄：')
                b = session.query(UserHomeWork).filter(UserHomeWork.age > int(a)).all()
                for row in b:
                    print(row)
            elif option == '4':
                a = input('搜索大于输入作业数的学员，请输入作业数量：')
                b = session.query(UserHomeWork).filter(UserHomeWork.homework_account > int(a)).all()
                for row in b:
                    print(row)
            elif option == '0':
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()












