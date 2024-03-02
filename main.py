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
        cur.execute(f"INSERT INTO todo('created_date', 'contents) VALUES('{today_date}','{todo}')")
    con.commit()   
    
def read_todo(cur):
    #전체출력
    result = cur.execute("SELECT seq, created_date, contents, finish_date, done FROM TODO")
    todo = result.fetchall()
    for data in todo:
        print(f"번호: {data[0]}, 날짜: {data[1]}, 해야할 일: {data[2]}, 끝낸 날짜: {data[3]}, 실행한 횟수: {data[4]}")
 
def date_todo(cur):
    #특정날짜 투두리스트 출력
    print("특정 날짜를 입력해주세요. ex)YYYY-mm-dd")
    date_input = input()
    if len(date_input) == 0:
        date_input = datetime.today().strftime('%Y-%m-%d')
    result = cur.execute(f"SELECT seq, created_date, contents, finish_date, done FROM TODO WHERE created_date='{date_input}'")
    todo = result.fetchall()
    if len(todo) == 0:
        print("사용자의 값이 없습니다.") 
    for data in todo:
        print(f"번호: {data[0]}, 날짜: {data[1]}, 해야할 일: {data[2]}, 끝낸 날짜: {data[3]}, 실행한 횟수: {data[4]}")

def todo_done(cur,con):
    read_todo(cur)
    done_input = input("완료표시 할 태스크 번호 입력")
    cur.execute(f"update todo set done = 1 where seq = {done_input}")
    con.commit() 

def todo_delete(cur,con):
    read_todo(cur)
    delete_input = input("삭제 할 태스크 번호 입력")
    cur.execute(f"delete from todo where seq = {delete_input}")
    con.commit()

def sign_up(con,cur):
    print("아이디와 비밀번호를 입력해주세요.")
    id_input = input("로그인 아이디: ")
    pw_input = input("패스워드: ")
    username = input("유저네임: ")
    year = input("생년월일(ex.yymmdd): ")
    gender = input("성별(M/W): ")
    cur.execute(f"INSERT INTO user('login_ID', 'PassWord', 'user_name', 'user_gender', 'user_years') \
    VALUES('{id_input}', '{pw_input}', '{username}', '{gender}', '{year}')")
    con.commit()

"""
로그인
아이디와 패스워드를 받고 로그인 시도
로그인 성공:True
로그인 실패: False
"""
def sign_in(cur):
    user_id = input("아이디 입력: ")
    user_pw = input("패스워드 입력: ")

    result = cur.execute(f"SELECT seq FROM USER WHERE login_ID = '{user_id}' AND PassWord = '{user_pw}' ")
    user = result.fetchone()
    #로그인 성공시: (2,)
    #로그인 실패시: None

    if not user:
        print("로그인 실패") 
        return -1

    print("로그인 성공")
    return user[0]

def run():
    #프로그램 실행 시작점
    todo = True
    is_auth = -1
    con = sqlite3.connect("todo.db")
    cur = con.cursor()

    print("아이디가 없으시다면 회원가입: 1번")
    print("아이디가 있으시다면 로그인: 2번")
    auth = input("항목을 선택해주세요: ")
    if auth == "1":
        sign_up(con, cur)
        return
    elif auth == "2":
        is_auth = sign_in(cur)

    if is_auth == -1:
        print("로그인 실패로 프로그램 종료")
        return

    while(todo):
        user_input = input("숫자를 입력해주세요")
        if user_input == '1':
            print("해야할일작성")
            set_todo(con, cur)
        elif user_input == '2':
            print("전체출력")
            read_todo(cur)
        elif user_input == '3':
            print("특정날짜 조회")
            date_todo(cur)
        elif user_input == '4':
            print("완료표시하기")
            todo_done(cur,con)
        elif user_input == '5':
            print("해야할일삭제")
            todo_delete(cur,con)
        elif user_input == 'exit':
            print("프로그램종료")
            todo = False
    con.close()

run()
