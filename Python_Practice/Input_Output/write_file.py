cities = ["Delhi",
          "Mumbai",
          "Kolkata",
          "Chennai",
          "Gurgaon"]

# Let's write the above mentioned list into a file
# 'w' is important here, otherwise py will try to open the file in 'r' mode
with open("./cities.txt", 'w') as city_file:
    for a_city in cities:
        print(a_city, file=city_file)

# Reading the file, we just wrote
with open("./cities.txt") as city_file:
    for city in city_file:
        print(city.strip())
