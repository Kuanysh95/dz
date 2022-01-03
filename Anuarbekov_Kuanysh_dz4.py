import datetime
import requests
from decimal import Decimal



def get_parc(resp, valute, text):
    return resp.text.split(valute)[1].split(text)[1][1:-2]


def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if response.text.find(val) != -1:
        nominal = int(get_parc(response, val, "Nominal"))
        my_date = datetime.datetime.strptime(response.text.split("Date")[1].split('"')[1], "%d.%m.%Y").date()
        name = get_parc(response, val, "Name")

        new_value = Decimal(".".join(get_parc(response, val, "Value").split(','))).quantize(Decimal("1.00"))

        return [my_date, name, new_value / nominal]


if __name__ == '__main__':
    lst = currency_rates("usd")
    print(f"на {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")
    lst = currency_rates("Eur")
    print(f"на {lst[0]} Курс 1 {lst[1]} равен {lst[2]} рублей")