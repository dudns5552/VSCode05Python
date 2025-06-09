import pickle

name='개발자'
age = 99
address = '서울시 중구 세종대로'
times={'JAVA' : 20, 'HTML' : 2, 'Oracle' : 10, 'Python' : 3}

with open('./saveFiles/developer.p', 'wb') as file:
  pickle.dump(name, file)
  pickle.dump(age, file)
  pickle.dump(address, file)
  pickle.dump(times, file)