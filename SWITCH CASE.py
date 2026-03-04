###MODEL 1###
day=int(input("Enter a number:"))
match day:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3:
         print("WEDNESDAY")
    case 4:
         print("THURSDAY")
    case 5:
          print("FRIDAY")
    case 6:
         print("SATURDAY")
    case 7:
         print("SUNDAY")
    case _:
         print("INVALID DAY")


###MODEL 2###
day=int(input("Enter a day number:"))
switch={
            1:"MONDAY",
            2:"TUESDAY",
            3:"WEDNESDAY",
            4:"THURSDAY",
            5:"FRIDAY",
            6:"SATURDAY",
            7:"SUNDAY"
}
print(switch.get(day,"INVALID DAY"))
