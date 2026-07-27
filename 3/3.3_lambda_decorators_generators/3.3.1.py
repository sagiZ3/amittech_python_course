def add_currency_symbol(func):
    def wrapper(price):
        return func(price) + "$"
    return wrapper

@add_currency_symbol
def get_price_format(price: int | float) -> str:
    return str(price)

def main():
    prices = [5, 50, 88, 11, 1, 33, 400, 61, 82, 100]
    print(f'Original Prices: {prices}')

    ten_discount_prices = list(map(lambda x: x * 0.9, prices))
    print(f'After 10% Discount On All Prices: {ten_discount_prices}')

    less_than_50_prices = list(filter(lambda x: x < 50, ten_discount_prices))
    print(f'Prices That Cost Less Then 50$: {less_than_50_prices}')

    ten_discount_prices = sorted(ten_discount_prices)
    print(f'Sorted Discounted Prices: {ten_discount_prices}')

    format_prices = [get_price_format(price) for price in ten_discount_prices]
    print(f'Final Prices (With Formatting): {format_prices}')


if __name__ == '__main__':
    main()
