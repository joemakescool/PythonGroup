def printDigit(d):
    """
    This function calculates a barcode based on inputed digit
    """

    if (d == "1"):
        bar = ":::||"
    elif (d == "2"):
        bar = "::|:|"
    elif (d == "3"):
        bar = "::||:"
    elif (d == "4"):
        bar = ":|::|"
    elif (d == "5"):
        bar = ":|:|:"
    elif (d == "6"):
        bar = ":||::"
    elif (d == "7"):
        bar = "|:::|"
    elif (d == "8"):
        bar = "|::|:"
    elif (d == "9"):
        bar = "|:|::"
    else:
        bar = "||:::"
    return bar


def printBarCode(zipCode):
    """
    This function calculates the barcode needed for a specific zipcode
    It also checks it's validity
    """
    mult = 0

    zipCode = str(zipCode).strip("''")

    mult = 0
    print("---------------------------------------------------------")
    if not zipCode.isdigit():
        print("Input is invalid, must be ONLY numbers.", "Tried", zipCode)
        return
    elif (len(str(zipCode)) != 5):
        print("Input is invalid, must be a 5 digit number.", "Tried", zipCode)
    else:
        total = int(zipCode[0]) + int(zipCode[1]) + int(zipCode[2]) + int(zipCode[3]) + int(zipCode[4])
        while total > mult:
            mult += 10
        check = mult - total
        print(zipCode)
        print("|" + printDigit(zipCode[0]) + printDigit(zipCode[1]) + printDigit(zipCode[2]) + printDigit(
            zipCode[3]) + printDigit(zipCode[4]) + printDigit(str(check)) + "|")
    print("---------------------------------------------------------")




