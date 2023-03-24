def gugu(dan) :
    for i in range(1, 20):
        print(f"{dan} X {i} = {dan * i}")
    
def total_gugu():
        for i in range(1, 20):
            gugu(i)
            print("----------------------")

total_gugu()