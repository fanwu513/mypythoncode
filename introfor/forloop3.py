farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print(farm)

for farm in farms:
    if farm == farms[0]:
        print(farms[0]["name"], ' has ', farms[0]["agriculture"])
    if farm == farms[1]:
        print(farms[1]["name"], ' has ', farms[1]["agriculture"])
    if farm == farms[2]:
        print(farms[2]["name"], ' has ', farms[2]["agriculture"])
