def main():
    try:
        total_consumed_unit = float(input('Total consumed unit(s): '))
        base_payable_amount = float(input('Base Monthly Charge: '))
    except (TypeError, ValueError):
        return 'Please inter a numerical value.'

    total_payable_amount = 1.0

    values = [
        (0, 50, 3.05), (0, 75, 4.00), (76, 200, 5.45),
        (201, 300, 5.70), (301, 400, 6.02), (401, 600, 9.30),
        (600, None, 10.70)
    ]

    for i in values:
        print(i)

    return 'done'


if __name__ == '__main__':
    response = main()
    print(response)
