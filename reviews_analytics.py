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