import pymysql

conn = pymysql.connect(host='localhost', user='sample_user',
                       password='1234', db='sample_db', charset='utf8')
curs = conn.cursor()

try:
    while True:
        print("1. 입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종료")
        choice = int(input("선택 : "))

        if choice == 1:
            print(f"{'입력기능':-^50}")
            name = input('이름 : ')
            phone = input('전화 : ')
            address = input('주소 : ')
            insert_sql = f"""INSERT INTO phonebooks (username, phone, address)
                             VALUES ('{name}', '{phone}', '{address}')"""
            curs.execute(insert_sql)
            conn.commit()
            print('입력이 성공하였습니다.')

        elif choice == 2:
            print(f"{'출력기능':-^50}")
            curs.execute("SELECT * FROM phonebooks")
            lists = curs.fetchall()
            print("번호        성명                 전화                 주소")
            print('-'*50)
            for data in lists:
                print(f"{data[0]}          {data[1]}            {data[2]}            {data[3]}")

        elif choice == 3:
            print(f"{'검색기능':-^50}")
            keyword = input("검색할 이름을 입력하세요 : ")
            search_sql = f"SELECT * FROM phonebooks WHERE username LIKE '%{keyword}%'"
            curs.execute(search_sql)
            lists = curs.fetchall()
            if not lists:
                print("등록돼있지 않은 데이터입니다.")
            else:
                print("번호        성명                 전화                 주소")
                print('-'*50)
                for data in lists:
                    print(f"{data[0]}          {data[1]}            {data[2]}            {data[3]}")

        elif choice == 4:
            print(f"{'수정기능':-^50}")
            name = input('수정할 이름을 입력하세요 : ')
            search_sql = f"SELECT * FROM phonebooks WHERE username LIKE '%{name}%'"
            curs.execute(search_sql)
            exist = curs.fetchall()
            if exist:
                new_name = input('새 이름 : ')
                new_phone = input('새 전화 : ')
                new_address = input('새 주소 : ')
                update_sql = f"""
                    UPDATE phonebooks
                    SET username = '{new_name}', phone = '{new_phone}', address = '{new_address}'
                    WHERE username = '{name}'
                """
                curs.execute(update_sql)
                conn.commit()
                print("연락처가 변경되었습니다.")
            elif not exist:
                print('일치하는 연락처가 없습니다.')

        elif choice == 5:
            print(f"{'삭제기능':-^50}")
            name = input("삭제할 이름을 입력하세요 : ")
            search_sql = f"SELECT * FROM phonebooks WHERE username LIKE '%{name}%'"
            curs.execute(search_sql)
            exist = curs.fetchall()
            if exist:
                delete_sql = f"DELETE FROM phonebooks WHERE username = '{name}'"
                curs.execute(delete_sql)
                conn.commit()
                print("1개의 레코드가 삭제됨")
            elif not exist:
                print('일치하는 연락처가 없습니다.')

        elif choice == 6:
            print(f"{'종료합니다.':-^50}")
            break

except Exception as e:
    conn.rollback()
    print("오류발생:", e)

conn.close()
