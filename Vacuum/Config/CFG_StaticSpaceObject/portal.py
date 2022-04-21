hives = [
    {10: 48}, # КОнтр - Инфель
    {48: 10}, # Инфель - контр
    {48: 19}, # Инфель - хаглд
    {50: 52}, # А"Кирс Он"кирт
    {52: 50}, # Он"кирт А"Кирс
    {96: 19}, # Овдар - хаглд
    {19: 19}
]

def get_hive(location_id, count):
    for d in hives:
        if location_id in d:
            if count == 2:
                continue
            return d[location_id]
    return 19

def get_to_id(to_id, count):
    for d in hives:
        if to_id in d:
            if count == 2:
                count -= 1
                continue
            return d[to_id]
    return 19
