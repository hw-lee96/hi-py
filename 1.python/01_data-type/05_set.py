# # SET
# # 중복을 허용하지 않음
# # 순서 상관 없이 요소를 저장하는 컬렉션

# ## {} 중괄호를 사용하여 집합을 생성
# ohgiraffers = {'pig', 'squirrel', 'bear', 'gorilla'}
# print(ohgiraffers) # {'gorilla', 'pig', 'bear', 'squirrel'} (순서가 없기 때문에, 호출할때마다 순서가 다름)

# ## 리스트로 set 생성
# another_safari_set = set(['monkey', 'tiger', 'wolf'])
# print(another_safari_set) # 출력 결과 : {'monkey', 'tiger', 'wolf'}
# mixed_set = {1, 'bear', (1,2,3)}
# print(mixed_set) # 출력 결과 : {1, 'bear', (1, 2, 3)}

# ohgiraffers.remove('pig')
# print(ohgiraffers) # 출력 결과 : {'bear', 'gorilla', 'squirrel'}
# ohgiraffers.add('pig')
# print(ohgiraffers) # 출력 결과 : {'bear', 'gorilla', 'squirrel', 'pig'}

# # SET 메소드
# ## 1. update()
# ## 2. discard()
# ## 3. pop()
# ## 4. clear()
# ## 5. union() : 두 set 합집합
# ## 6. interserction() : 두 set 자료형의 교집합을 반환
# ## 7. difference() : 좌향을 기준으로 우향의 차집합을 반환
# ## 8. copy() : 대상 set을 복사하여 반환