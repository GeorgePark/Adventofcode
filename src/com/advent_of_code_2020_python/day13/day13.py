buses = [line.rstrip().replace('x,', '') for line in open("Day_13_2020.txt", "r")]

arrival_time = buses[0]
bus_times = buses[1].split(',')

waiting_times = {}

for bus in bus_times:
    waiting_times[bus] = int(bus) - (int(arrival_time) % int(bus))

print(waiting_times)


time = 0
step = 1
new_buses = [line.rstrip() for line in open("Day_13_2020.txt", "r")][1].split(',')

# grab all bus positions and time offset
bus_time_position = [(int(i), j) for j, i in enumerate(new_buses) if i != 'x']

print(bus_time_position)

# iterate through buses
for bus_position, mins in bus_time_position:
    # check to see if bus is departing at current time
    while (time + mins) % bus_position != 0:
        time += step
    # increase step multiple to find next min for next bus
    step *= bus_position

print(f'Part 2: {time}')