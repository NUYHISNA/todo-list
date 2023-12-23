import sqlite3

def set_todo():
    #cur.execute(f"INSERT INTO todo VALUES('{value[0]}','{value[1]}','{value[2]}','{value[3]}','{value[4]}')")
    #con.commit()
    pass
    
def run():
    #프로그램 실행 시작점
    todo = True
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    while(todo):
        user_input = input("숫자를 입력해주세요")
        if user_input == '1':
            print("해야할일작성")
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