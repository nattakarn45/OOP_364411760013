from Vehicle import Vehicle
#เพิ่มข้อมูล
def display_option():
    print("welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Delete Vehicle")
    print("3.Edit Vehicle Price")
    print("4.Edit Vehicle Color")
    print("5.display all Vehicle")
    print("6.exit")
    select = int(input("select(1-6)? : "))
    if select == 1:
        input_vehicle_data()
    elif select==2:
        delete_vehicle()
    elif select ==3:
        edit_vehicle_price()
    elif select==4:
        edit_vehicle_color()
    elif select ==5:
        display_vehicle()
    elif select ==6:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-6.")

def input_vehicle_data():
    brand  = input("Enter vehicle brand ")
    model  = input("Enter vehicle model ")
    color  = input("Enter vehicle color ")
    maxspeed  = int(input("Enter vehicle maxspeed:"))
    price = float(input("Enter vehicle price: "))

    Vehicle.my_vihecle.append(Vehicle(brand,model,color,maxspeed,price))
    print("\n---------------------------------")
    print("Already add vehicel to stor.")
    print("\n---------------------------------")

def display_vehicle():
    if len(Vehicle.my_vihecle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had{len(Vehicle.my_vihecle)} following:')
        n = 1 #countลบข้อมูล
        for x in Vehicle.my_vihecle:
            print(f'[{n}]:',end=" ")
            x.vehicle_detail()
            n = n+1
        print("\n")
# delete vehicle ลบ
def delete_vehicle():
    display_vehicle()
    if len(Vehicle.my_vihecle) !=0:
        print("You had no data to delete.")
        s = int(input("Select to delete?: "))

        Vehicle.delete_vehicle(vehicle, s-1)
        print("\n---------------------------------")
        print("Your data has been deleted.")
        print("---------------------------------\n")

# edit vehicle price
def edit_vehicle_price():
    display_vehicle()
    if len(Vehicle.my_vihecle) != 0:
        s = int(input("Select to edit?: "))
        #display previous price
        print(f'previous price: {Vehicle.my_vihecle[s-1].price}')
        new_price  = float(input("new price: "))
        Vehicle.edit_vehicle_price(Vehicle,s-1,new_price)
        print("\n---------------------------------")
        print("Your data has been deleted.")
        print("---------------------------------\n")

def edit_vehicle_color():
    display_vehicle()
    if len(Vehicle.my_vihecle) != 0:
        s = int(input("Select to edit?: "))
        #display previous price
        print(f'/nprevious color: {Vehicle.my_vihecle[s-1].color}')
        new_color  = input("new color: ")
        Vehicle.edit_vehicle_color(Vehicle,s-1,new_color)
        print("\n---------------------------------")
        print("Your data has been deleted.")
        print("---------------------------------\n")

# run
#my_vehicel  = []
s  = 0
while s == 0:
    display_option()
    #แสดงข้อมูลให้เห็นก่อน แล้วสามารถเลือกหรือลบข้อมูลออกได้