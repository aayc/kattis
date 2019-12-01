while True:
    try:
        s = input()
        print("{:.2f}".format(eval(s)))
    except:
        break
