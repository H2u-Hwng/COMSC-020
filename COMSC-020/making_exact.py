money = float(input("Money = $"))

bills = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.01]

for n in bills:
    if (money >= n):
        count = int(money // n)
       
        if (money >= 1 and count > 1):
            print(f"{count} ${n} bills")
        elif (money >= 1):
            print(f"{count} ${n} bill")
        elif (money < 1 and count > 1):
            print(f"{count} {n*100:.0f}-cent coins")
        else:
            print(f"{count} {n*100:.0f}-cent coin")
        
        money -= count * n
        money = round(money, 2)