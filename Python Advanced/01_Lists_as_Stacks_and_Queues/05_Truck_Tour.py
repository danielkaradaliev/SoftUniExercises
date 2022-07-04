from collections import deque


class PetrolStation:
    def __init__(self, petrol_amount, distance):
        self.petrol_amount = petrol_amount
        self.distance = distance

    def __str__(self):
        return f"Petrol amount: {self.petrol_amount}, Distance to next: {self.distance}"


number_of_petrol_pumps = int(input())
petrol_stations = [PetrolStation(int(x), int(y)) for x, y in [input().split() for _ in range(number_of_petrol_pumps)]]

for current_index in range(number_of_petrol_pumps):
    tank = 0
    current_petrol_station_order = deque(petrol_stations)
    for _ in range(number_of_petrol_pumps):
        tank += current_petrol_station_order[0].petrol_amount - current_petrol_station_order[0].distance
        current_petrol_station_order.popleft()

        if tank < 0:
            break

    else:
        print(current_index)
        break
    petrol_stations.append(petrol_stations.pop(0))
