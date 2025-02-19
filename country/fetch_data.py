import requests
from .models import Country

# def fetch_and_store_data():
#     url = "https://api.countrylayer.com/v2/all?access_key=f02d12edf9a34d8e2d4b261c4f9076f2"
#     response = requests.get(url)

#     if response.status_code == 200:
#         countries = response.json()

#         for country  in countries:
#             country, created = Country.objects.update_or_create(
#                 name=country ['name'],
#                 defaults={
#                     'top_level_domain': country ['topLevelDomain'],
#                     'alpha2_code': country ['alpha2Code'],
#                     'alpha3_code': country ['alpha3Code'],
#                     'calling_codes': country ['callingCodes'],
#                     'capital': country ['capital'],
#                     'alt_spellings': country ['altSpellings'],
#                     'region': country ['region'],
#                 }
#             )
#             if created:
#                 print(f"Created new country: {country.name}")
#             else:
#                 print(f"Country already exists: {country.name}")

# fetch_and_store_data()

def fetch_and_store_countries():

    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()

        for country in countries:
            name = country["name"]["common"]
            cca2 = country["cca2"]
            capital = ["capital"][0]
            region = country["region"]
            languages = country.get('languages', {})
            language = ', '.join(languages.values()) if languages else ''
            population = country["population"]
            timezones = country.get('timezones', [])
            timezone = ', '.join(timezones) if timezones else ''
            flag = country.get('flags', {}).get('png', '')

            # Save to the database
            Country.objects.update_or_create(
                cca2=cca2,
                defaults={
                    "name": name,
                    "capital": capital,
                    "region": region,
                    "language": language,
                    "population": population,
                    "timezone": timezone,
                    "flag": flag,
                }
            )
        print("Countries updated successfully!")
    else:
        print("Failed to fetch data")

fetch_and_store_countries()
