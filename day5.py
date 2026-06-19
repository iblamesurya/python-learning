#currency converter
# Write code below 💖
pesos = float(input("What do you have left in pesos?"))
soles = float(input("What do you have left in soles?"))
reais = float(input("What do you have left in reais?"))
usd = (pesos*0.00029 + soles*0.30 + reais*0.19) 
print(usd)
