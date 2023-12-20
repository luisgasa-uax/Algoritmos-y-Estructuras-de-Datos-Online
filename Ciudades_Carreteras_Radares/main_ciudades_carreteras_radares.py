import Radar
import math

def add_bearing(radar, point, bearing):
    if not point in radar:
        radar[point] = {}
    for distance in radar:
        if distance != point:
            if distance <= bearing:
                if not distance in radar[point]:
                    radar[point][distance] = bearing
                else:
                    radar[point][distance] = min(radar[point][distance], bearing)

def create_radar(points, bearings):
    radar = {}
    for i in range(len(points)):
        add_bearing(radar, points[i], bearings[i])
    return radar


# example usage
points = ['A', 'B', 'C', 'D']
bearings = [5, 10, 15, 20]
radar_data = create_radar(points, bearings)
radar = radar.Radar(radar_data)


# now you can use the radar object to find distances and bearings between points
# example usage:
distance, bearing = radar.find_shortest_path('A', 'D')
print(f"Shortest distance from A to D: {distance}")
print(f"Bearing at A for shortest path: {bearing}")
# Prueba del código
radar = Radar(30, "sur", 80)
print(radar.get_datos())
print(radar.calcular_velocidad(100))




