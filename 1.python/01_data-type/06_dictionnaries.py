
# Dictionaries
# 키와 값의 쌍으로 구성된 데이터 구조로, 키를 통해 값을 찾을 수 있으므로 매우 빠른 조회 성능을 보여줌

teacher = {'name':'pig'}
print(type(teacher)) # 출력 결과 : <class 'dict'>
print(teacher['name']) # 출력 결과 : pig

# 생성 후 키-값 쌍 추가 / 수정 / 삭제
teacher['age'] = 20
print(teacher['age']) # 출력 결과 : 20

# in 키워드
print('name' in teacher) # 출력 결과 : True

# 1. get() : 매개변수로 전달받은 key에 해당하는 값을 반환한다.
print(teacher.get('name')) # 출력 결과 : pig

# 2. keys() : 모든 key 값을 반환
print(teacher.keys()) # 출력 결과 : dict_keys(['name', 'age'])

# 3. values() : 모든 values 값을 반환
print(teacher.values()) # 출력 결과 : dict_values(['pig', 20])

# 4. items()
print(teacher.items()) # 출력 결과 : dict_items([('name', 'pig'), ('age', 20)])
print(teacher) # 출력 결과 : {'name': 'pig', 'age': 20}

# 5. pop(key) : key 값에 해당하는 key-value 쌍을 제거
print(teacher.pop('age')) # 출력 결과 : 30
print(teacher ) # 출력 결과 : {'name': 'pig'}

# 6. clear() : 모든 항목 제거
teacher.clear()
print(teacher) # 출력 결과 : {}