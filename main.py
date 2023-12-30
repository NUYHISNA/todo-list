import sqlite3
from datetime import datetime

def set_todo(con, cur):
    today_date = datetime.today().strftime('%Y-%m-%d')
    print("오늘의 할일을 입력하시오.")
    todos = []
    while(True):
        todo_input = input()
        if todo_input == 'exit':
            print("프로그램 종료")
            break
        todos.append(todo_input)
    print(todos)
    # INSERT INTO todo('created_date', 'contents') VALUES ('2023-12-30', '베스킨라빈스먹기')
    for todo in todos:
        cur.execute(f"INSERT INTO todo('created_date', 'contents') VALUES('{today_date}','{todo}')")
    con.commit()   
    
def run():
    #프로그램 실행 시작점
    todo = True
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    while(todo):
        user_input = input("숫자를 입력해주세요")
        if user_input == '1':
            print("해야할일작성")
            set_todo(con, cur)
        elif user_input == '2':
            print("완료표시")
        elif user_input == '3':
            print("특정날짜 조회")
        elif user_input == '4':
            print("해야할일수정")
        elif user_input == '5':
            print("해야할일삭제")
        elif user_input == 'exit':
            print("프로그램종료")
            todo = False
    con.close()

run()