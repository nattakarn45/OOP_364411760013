from Vehicle import Vehicle
def display_option():
    print("welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.display all Vehicle")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select ==2:
        display_option()
    elif select ==3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

def input_vehicle_data():
    brand  = input("Enter vehicle brand ")
    model  = input("Enter vehicle model ")
    color  = input("Enter vehicle color ")
    maxspeed  = int(input("Enter vehicle maxspeed:"))
    price = float(input("Enter vehicle price: "))

    my_vehicel.append(Vehicle(brand,model,color,maxspeed,price))
    print("\n---------------------------------")
    print("Already add vehicel to stor.")
    print("\n---------------------------------")

def display_vehicel():
    if len(my_vehicel) ==0:
        print("You had no vehicel data.")
    else:
        print(f'You had{len(my_vehicel)} following:')
        for x in my_vehicel:
            x.vehicel_info()
        print("\n")

# run
my_vehicel  = []
s  = 0
while s == 0:
    display_option()
    #แสดงข้อมูลให้เห็นก่อน แล้วสามารถเลือกหรือลบข้อมูลออกได้