# else 문

# for 문이 종료된 후 else가 동작
for x in [1,2,3]:
    print(x)
else:
    print('끝')

# continue 문
# 반복문 안에서 continue를 만나면 다음 실행문은 실행되지 않고 다음 반복으로 넘어감
# 특정 순간을 생략하고 진행하기 위해 사용
for i in range(3):
    if i == 1:
        continue
    print(i)

# break 문
# 반복문을 종료
print()
for x in [1,2,3]:
    if x == 2:
        print('끝')
        break
    else:
        print(x)