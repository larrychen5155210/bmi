#BMI計算程式
h = input('請輸入你的身高: ')
w = input('請輸入你的體重: ')
h = float(h)/100
w = float(w)
bmi = w / (h * h)
print('你的BMI是', bmi)
if bmi < 18.5:
	print('你的體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的體重正常')
elif bmi >= 24 and bmi < 27:
	print('你的體重過重')
elif bmi >= 27 and bmi < 30:
	print('你的體重為輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的體重為中度肥胖')	
else:
	print('你的體重為重度肥胖')

