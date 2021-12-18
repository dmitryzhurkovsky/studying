needed_states = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {
    'k_one': {'id', 'nv', 'ut'},
    'k_two': {'wa', 'id', 'mt'},
    'k_three': {'or', 'nv', 'ca'},
    'k_four': {'nv', 'ut'},
    'k_five': {'ca', 'az'}
}


def find_best_stations(needed_states: set, stations: dict) -> set:
    final_stations = set()

    while needed_states:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
            covered = needed_states & states_for_station  # intersection - пересечение
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        needed_states -= states_covered
        final_stations.add(best_station)

    return final_stations


find_best_stations(needed_states, stations)
