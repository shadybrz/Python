def convert(number):
    x = input("x?")
    if x%3==0:
        print("Pling")
    elif x%5==0:
        print("Plang")
    elif x%7==0:
        print("Plong")
    elif x%3==0 and x%5==0:
        print("PlingPlang")
    elif x%3==0 and x%7==0:
        print("PlingPlong")
    elif x%5==0 and x%7==0:
        print("PlangPlong")
    elif x%3==0 and x%5==0 and x%7==0:
        print("PlingPlangPlong")
    elif x%3!=0 and x%5!=0 and x%7!=0:
        print(x)
    pass
