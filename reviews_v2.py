

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 500000 == 0:   # % 求餘數
            print(len(data))
print('檔案讀取結束，留言總筆數 =', len(data))
#print(data[0])

# 文字計數
# sum = 0
# for x in range(1000000):
#   sum = sum + len(data[x])
# averge = sum / 1000000
# print('留言平均長度= ',averge)

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

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good這個字')

wc = {} #word_count  {}字典
for d in data:  # d是字串  data是清單
    words = d.split()  #words 是清單  split預設就是' '空白，如果沒有打''他會把連續空白處理掉
    for word in words:
        if word not in wc:
            wc[word] = 1  #新增新的key進wc字典
        elif word in wc :
            wc[word] += 1 #如果有出現就將value加1

for word in wc:  #這種loop是把每一個key給叫出來
    if wc[word] > 1000:
        print(word, wc[word])

print('字典的長度:', len(wc))

while True:
    search_word = input('請輸入要查詢的單字: ')
    if search_word == 'q':
        print('結束查詢!!!')
        break
    if search_word in wc:
        print(search_word, '出現了', wc[search_word] ,'次')
    else:
        print('這個字沒有出現過。')
           


