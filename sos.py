mes = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Uankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"
mes = mes.split(" ")

dict = {"Zero":0, "One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Niner":9, "Dash":"-"}

for word in mes:
    if dict.get(word) != None:
        print(dict.get(word), end="")
    else:
        print(word[0], end="")