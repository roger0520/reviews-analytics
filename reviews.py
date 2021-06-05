


data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 500000 == 0:   # % 求餘數
            print(len(data))
print('檔案讀取結束，留言總筆數 =', len(data))

#sum = 0
#for x in range(1000000):
#   sum = sum + len(data[x])
#averge = sum / 1000000
#print('留言平均長度= ',averge)

sum = 0
for d in data:
    sum = sum + len(d)
print('留言平均長度= ', sum / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆留言提到good這個字')
# print(good[1])

#good = [d for d in data if 'good' in d]  　#這行的篩選是上面的快寫法 這是原封不動把d的內容放進清單
good = [1 for d in data if 'good' in d]  #這是變成要把1裝進去good的清單中
print(good)

#bad = ['bad' in d for d in data]
bad = [d for d in data if 'bad' in d]
print(len(bad))

# bad = []
# for d in data:
#     bad.append('bad' in d)
print(len(bad))
