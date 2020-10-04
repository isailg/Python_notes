pesos = input ("How many MXN do you have?")
pesos = float (pesos)

usd_value = 21.92
usd_u= pesos/usd_value
usd_u= round (usd_u,2)
usd_u = str(usd_u)

print("You have $"+ usd_u+ "usd")
