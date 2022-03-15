# Если что-то кратно, то оставляем как есть, если нет, то оно включено, значит +1
def my_round(a, b):
    return 1 if a % b != 0 else 0


search_room, all_levels, old_room, old_pod, old_level = tuple(map(int, input().split(' ')))

answ_pod = -1
answ_floor = -1

if all_levels != 1 and search_room > old_pod:
    # получаем количество этажей дома до нашей квартиры
    levels_before = all_levels * old_pod - (all_levels - old_level)
    # получаем количество квартир на этаже
    rooms_in_level = (old_room // levels_before) + my_round(old_room, levels_before)

    flats_before = all_levels * rooms_in_level
    answ_pod = (search_room // flats_before) + my_round(search_room, flats_before)

    flat_our = search_room - flats_before
    answ_floor = (flat_our // rooms_in_level) + my_round(flat_our, rooms_in_level)
    if rooms_in_level < 2:
        answ_pod = 0

if all_levels == 1:
    answ_floor = 1

print(f'{answ_pod} {answ_floor}')
