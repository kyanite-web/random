while True:
    BOOM = "Boom! "
    array1 = input("Enter values, separated with a space:")
    arr = array1.split()
    Boomcount = 0
    looptimes = (len(arr))
    for i in range(looptimes):
        try:
            int(arr[i])
            Boomcount += arr[i].count("7")
        except ValueError:
            print("Letter Entered, Try again")
    print(Boomcount * BOOM)