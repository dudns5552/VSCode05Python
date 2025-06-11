lists = []
cnt = 1
bool = False
while True:
  print("1. 입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종료")
  # 번호를 입력
  choice = int(input("선택 : "))

  if(choice == 1):
    print(f"{'입력기능':-^50}")
    data = {'번호': cnt, '이름': input("성명>>> "), '전화': input("전화>>> "),
    '주소': input("주소>>> ")}
    lists.append(data)
    cnt += 1
    
  elif(choice == 2):
    print(f"{'출력기능':-^50}")
    print("번호        성명                 전화                 주소")
    print('-'*50)
    for data in lists:
      print(f"{data['번호']}          {data['이름']}            {data['전화']}            {data['주소']}")
  
  elif(choice == 3):
    print(f"{'검색기능':-^50}")
    search = input("검색할 이름을 입력하세요 : ")
    for data in lists:
      if data['이름'] == search:
        print("번호        성명                 전화                 주소")
        print('-'*50)
        print(f"{data['번호']}          {data['이름']}            {data['전화']}            {data['주소']}")
        bool = True
    if bool == False:
      print("등록돼있지 않은 데이터입니다.")
    
  elif(choice == 4):
    print(f"{'수정기능':-^50}")
    search = input("수정할 이름을 입력하세요 : ")
    for i in range(len(lists)):
      if lists[i]['이름'] == search:
        lists[i] = {'번호': lists[i]['번호'], 
                    '이름': input("새로운 이름 :"), 
                    '전화': input("새로운 전화번호 : "),
                    '주소': input("새로운 주소 : ")}
        print('연락처가 변경되었습니다.')
        bool = True
    if not bool:
      print('일치하는 연락처가 없습니다.')
        
  elif(choice == 5):
    print(f"{'삭제기능':-^50}")
    search = input("삭제할 이름을 입력하세요 : ")
    
    for i in range(len(lists)):
      if lists[i]['이름'] == search:
        lists.remove(lists[i])
        bool = True
    if not bool:
      print('일치하는 연락처가 없습니다.')
    
  elif(choice == 6):
    print(f"{'종료합니다.':-^50}")
    break
    