cars = {"Audi Q8": 70000,"Audi A4": 60000,"BMW 3": 56000,"Chevrolet Camaro": 30000,"Cadillac Escalade": 80000,
        "Cadillac CT5": 37700,"Dodge Challenger": 30600,"Ford Mustang": 30000,"Honda Civic": 25000,
        "Pagani": 1500000,"Lamborghini Urus": 450000,"Toyota Landcruiser": 75000,"Range Rover": 90000,
        "Jeep Wranger": 250000,"Toyota Fortuner": 60000,"Porshce Panamera": 350000,"Brabus": 500000,"Toyota Camry": 45000,
        "Audi Q7": 50000,"lamborghini Hurricane": 300000,"Porsche 911": 250000,"Henessey Venom": 2500000,
        "Tundra": 80000,"Highlander": 65000,"Tesla Model S": 98000,"Rolls Royce Phantom": 450000,"Hyundai Accord": 30000,
        "Hyundai Accent": 18000,"Ford Bronco": 35000,"Mclaren": 650000,"Bugatti Chiron": 4500000,"Bugatti Veyron": 1500000}

car_name = input("Enter the car's name: ")

if car_name in cars:
    print("YES")
    car_cost = cars[car_name]
    print("The price of {1} is {0}".format(car_cost,car_name))
else:
    print("NO\nUnfortunately there is no car under such name at the moment")