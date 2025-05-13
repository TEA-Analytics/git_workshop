def calculate_average(data, column):
    total = 0
    for row in data:
        total += float(row[column])
    return total / len(data)

def group_by_column(data, column):
    grouped = {}
    for row in data:
        key = row[column]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(row)
    return grouped