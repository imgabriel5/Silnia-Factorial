# Potrzebujemy przeliczyć trochę waluty, czasy niepewne,
# warto mieć na uwadze swoją ulubioną walutę.
# Napisz klasę, która będzie zawierać dwie metody:

#       przeliczenie wybranej waluty z tabeli A na złotówki  <- dane wejściowe: kod waluty, ilość waluty
#       wskazanie aktualnego kursu z tabeli A <- dane wjećiowe: kod waluty

# Klasa w celu przeliczenia waluty powinna skorzystać z aktualnych kursów z Narodowego Banku Polskiego
# dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/

import requests
import json

class CurrencyConverter:
    def __init__(self):
        self.endpoint = "http://api.nbp.pl/api/exchangerates/"

    def get_currency_rate(self, currency_code):
        """
        Returns the current rate of a given currency code in relation to PLN from table A
        """
        url = f"{self.endpoint}/tables/A?format=json"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Could not retrieve exchange rates from NBP API")
        json_data = json.loads(response.content)
        rates = json_data[0]["rates"]
        for rate in rates:
            if rate["code"] == currency_code.upper():
                return rate["mid"]
        raise Exception(f"No rate found for currency code {currency_code}")

    def convert_currency_to_pln(self, currency_code, amount):
        """
        Converts given amount of currency to PLN using the current rate of given currency code from table A
        """
        rate = self.get_currency_rate(currency_code)
        return round(amount * rate, 2)

# Opis działania klasy:
#
# Konstruktor klasy CurrencyConverter ustawia adres endpointu API NBP, który będzie wykorzystywany w metodach klasy.
# Metoda get_currency_rate zwraca aktualny kurs waluty o podanym kodzie z tabeli A. Wykorzystuje do tego API NBP z parametrem format=json. Przeszukuje otrzymane dane, aż znajdzie walutę o podanym kodzie, po czym zwraca jej średni kurs (mid). W przypadku błędu lub braku wyniku, zgłasza wyjątek.
# Metoda convert_currency_to_pln przelicza podaną ilość waluty o podanym kodzie na PLN, wykorzystując metodę get_currency_rate. Zwraca wynik z dokładnością do 2 miejsc po przecinku.
# Przykładowe użycie klasy:

cc = CurrencyConverter()
print(cc.get_currency_rate("USD"))  # zwraca aktualny kurs dolara amerykańskiego
print(cc.convert_currency_to_pln("EUR", 100))  # przelicza 100 euro na PLN
