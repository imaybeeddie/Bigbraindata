import requests


def country_info():
    country_name = input('enter the country name: ')
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        country = data.get('name', {}).get('common', 'N/A')
        continent = data.get('continents', ['N/A'])[0]
        capital = data.get('capital', ['N/A'])[0]

        currencies = data.get('currencies', {})
        if currencies:
            currency_code = next(iter(currencies.keys()))
            currency_name = currencies[currency_code].get('name', 'N/A')
            currency_symbol = currencies[currency_code].get('symbol', 'N/A')
        else:
            currency_code = currency_name = currency_symbol = 'N/A'
        languages = ', '.join(data.get('languages', {}).values()) if data.get('languages') else 'N/A'
        population = data.get('population', 'N/A')
        area = data.get('area', 'N/A')
        timezones = ', '.join(data.get('timezones', [])) or 'N/A'
        neighbours = ', '.join(data.get('borders', [])) or 'None'

        print(f"\nCountry:{country}")
        print(f"\nContinent:{continent}")
        print(f"\nCapital:{capital}")
        print(f"\nCurrency Code:{currency_code}")
        print(f"\nCurrency Name:{country_name}")
        print(f"\nLanguage:{languages}")
        print(f"\nPopulation:{population:,}")
        print(f"\nArea:{area:,}")
        print(f"\nTimezones:{timezones}")
        print(f"\nBordering Countries:{neighbours}")
    else:
        print("Country not found or API error!")

country_info()