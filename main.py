import time
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
for i in range(len(mission_names)):#for each item in list, loop the program
    print(mission_names[i], " Took place in " + str(mission_years[i]) + (". This mission was a success" if mission_success[i] == True else ". This mission ended in failure.")) #a single line that prints the missions, their years, and results on their own lines
    time.sleep(1)
mission_pass = 0
mission_total = len(mission_names)
print("Total number of missions: " + str(mission_total))

for x in range(len(mission_success)):#for each item in list that succeeds, add one to the integer count for successes
    if mission_success[x]:
        mission_pass += 1
print(str(mission_pass) + " Missions ended in a success total") #print results
time.sleep(1)
print(str(mission_pass/mission_total * 100) + f"% of missions were successful.")
time.sleep(1)
print("Missions that took place before the year 2000:") #print header for list of missions before 2000
time.sleep(1)
for y in range(len(mission_names)):#another loop for years
        if mission_years[y] < 2000:#check if list item happened before 2000
            print(mission_names[y])
            time.sleep(1)