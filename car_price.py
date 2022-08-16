def make_dict(cars):
    d = {}
    d['Brand'] = cars[0]
    if cars[1] != 'NA':
        d['Price'] = float(cars[1])
    else:
        d['Price'] = 0
    d['Body'] = cars[2]
    if cars[3] !='NA':
        d['Mileage'] = int(cars[3])
    else:
        d['Mileage'] = 0
    if cars[4] != 'NA':
        d['EngineV'] = float(cars[4])
    else:
        d['EngineV'] = 0
    d['Engine_Type'] = cars[5]
    d['Registration'] = cars[6]
    if cars[7] != 'NA':
        d['Year'] = int(cars[7])
    else:
        d['Year'] = 0
    d['Model'] = cars[8].replace('\n','')

    return d

# ['ï»¿Brand', 'Price', 'Body', 'Mileage', 'EngineV', 'Engine Type', 'Registration', 'Year', 'Model\n']

def make_database():
    cars = open("cars_multiple_linearR.csv", "r")
    line_cnt = 1
    car_prices = []
    for line in cars:
        row = line.split(',')
        if line_cnt >= 2:
            record = make_dict(row)
            car_prices.append(record)

        line_cnt += 1

    return car_prices


def grouped_by_brand(db):
    group = {}
    for item in db:
        brand = item['Brand']
        if brand in group:
            group[brand] += 1
        else:
            group[brand] = 1

    return group

def group_by_model(db):
    group1 = {}
    for item in db:
        model = item['Model']
        if model in group1:
            group1[model] += 1
        else:
            group1[model] = 1

    return group1

def group_by_column(db, column):
    gen_group = {}
    for item in db:
        col = item[column]
        if col in gen_group:
            gen_group[col] += 1
        else:
            gen_group[col] = 1
    return gen_group

def audi(db):
    audi_brand = []
    for item in db:
        brnd = item['Brand']
        yr = item['Year']
        eng = item['Engine_Type']
        # bdy = item['Body']
        if brnd == 'Audi' and yr >= 2015 and eng == 'Petrol':
            audi_brand.append(item)
            # audi_brand[brnd, yr] += 1

    return audi_brand

def pretty_print(cars):
    for item in cars:
        print(f"Brand: {item['Brand']}")
        print(f"Price: {item['Price']}")
        print(f"Body: {item['Body']}")
        print(f"Mileage: {item['Mileage']}")
        print(f"EngineV: {item['EngineV']}")
        print(f"Engine_Type: {item['Engine_Type']}")
        print(f"Registration: {item['Registration']}")
        print(f"Year: {item['Year']}")
        print(f"Model: {item['Model']}")
        print("-" * 100)

def add_num(a, b):
    result = a + b
    return result

if __name__ == "__main__":
    db = make_database()
    brand_year = audi(db)
    pretty_print("\n", brand_year)
