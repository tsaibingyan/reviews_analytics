data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取成功，總計有 %d 筆資料' %len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
avg_len = sum_len / 1000000 
print('留言的平均長度是 %.2f ' %avg_len)

 
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有 %d 筆留言長度小於100' %len(new))

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('含有good的留言有 %d 筆' %len(good))
print(good[0])