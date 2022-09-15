#BMI計算程式
height = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')
exercise = input('請問你平常有在運動嗎? ')
h = float(height)/100
w = float(weight)
bmi = w / (h * h)
print('你的BMI是', bmi)
if exercise == '有':
	if bmi < 18.5:
		print('你的體重過輕')
		print('除了運動也要多補充蛋白質喔!!')
	elif bmi >= 18.5 and bmi < 24:
		print('你的體重正常')
		print('很好 要繼續保持喔!!')
	elif bmi >= 24 and bmi < 27:
		print('你的體重過重')
		print('運動量要再增加喔!!')
	elif bmi >= 27 and bmi < 30:
		print('你的體重為輕度肥胖')
		print('你的運動量不夠喔!!')
	elif bmi >= 30 and bmi < 35:
		print('你的體重為中度肥胖')
		print('你確定你有在運動?')	
	else:
		print('你的體重為重度肥胖')
		print('你根本沒在運動吧?')
if exercise == '沒有':
	if bmi < 18.5:
		print('你的體重過輕')
		print('你太瘦了啦')
	elif bmi >= 18.5 and bmi < 24:
		print('你的體重正常')
		print('多運動有益身體健康喔!!')
	elif bmi >= 24 and bmi < 27:
		print('你的體重過重')
		print('你怎麼不去運動呢?')
	elif bmi >= 27 and bmi < 30:
		print('你的體重為輕度肥胖')
		print('要多注意你的體重喔!!')
	elif bmi >= 30 and bmi < 35:
		print('你的體重為中度肥胖')
		print('該去運動了吧!!')	
	else:
		print('你的體重為重度肥胖')
		print('快去運動!!')
