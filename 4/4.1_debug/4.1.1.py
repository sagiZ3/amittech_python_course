def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / (len(numbers) if numbers else 1)


def find_maximum(numbers):
    max_num = numbers[0] if numbers else None
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def process_data(data):
    processed = []
    for item in data:
        avg = calculate_average(item['values'])
        max_val = find_maximum(item['values'])
        processed.append({
            'id': item['id'],
            'average': avg,
            'max': max_val
        })
    return processed


def print_report(processed_data):
    for item in processed_data:
        print(f"ID: {item['id']}")
        print(f"  Average: {item['average']:.2f}")
        print(f"  Max: {item['max']}")
        print("")


def main():
    data = [
        {'id': 1, 'values': [3, 5, 7, 9, 11]},
        {'id': 2, 'values': [2, 4, 6, 8]},
        {'id': 3, 'values': []},
        {'id': 4, 'values': [10, 20, 30]},
        {'id': 5, 'values': [-5, -3, -1, 0, 1, 3]}
    ]

    processed_data = process_data(data)
    print_report(processed_data)


if __name__ == "__main__":
    main()