


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




