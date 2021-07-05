def main(units: float, base_amount: float, unit_values: list) -> float:
    total_amount = 0

    if units < unit_values[0][1]:
        total_amount = round((units * unit_values[0][2]) + base_amount, 2)
        return total_amount

    unit_values.insert(0, (0, 0, 0))
    values = []

    for c, i in enumerate(unit_values):
        try:
            if c != 0 and unit_values[c][0] == unit_values[c + 1][0]:
                continue
        except IndexError:
            pass

        if i[0] < units <= i[1]:
            values.append(i)
            break

        values.append(i)

    for c, j in enumerate(values):
        try:
            total_amount += (values[c + 1][1] - values[c][1]) * values[c + 1][2]
        except IndexError:
            pass

    total_amount = round(total_amount + base_amount, 2)
    return total_amount


if __name__ == '__main__':
    try:
        total_units = float(input('Total consumed unit(s): '))
        total_base_amount = float(input('Base Monthly Charge: '))
    except (TypeError, ValueError):
        raise Exception('Please enter a numerical value')

    v = [
        (0, 50, 3.50), (0, 75, 4.00), (76, 200, 5.45),
        (201, 300, 5.70), (301, 400, 6.02), (401, 600, 9.30),
        (600, total_units, 10.70)
    ]

    result = main(units=total_units, base_amount=total_base_amount, unit_values=v)

    print()
    output = f'Total payable amount is {result}\nUnit rate is {round(result / total_units, 2)} taka/unit.'
    print(output)
