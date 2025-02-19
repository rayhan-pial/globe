To run the projects follow the steps:

step 1: pip install -r requirements.txt

step 2: python manage.py makemigrations

step 3: python manage.py migrate

step 4: python manage.py shell

        from country.fetch_data import fetch_and_store_data
        fetch_and_store_data()
        exit()

step 5: python manage.py runserver



Urls to get the results:

For Login    : /user-api/login/
For Register : /user-api/register/

Rest Representation

For List And Create Countries              : /country-api/country/countries/
For Retrieve, Update And Delete A Country  : /country-api/country/countries/<int:country_id>/
For Same Regional Countries                : /country-api/regional/<int:country_id>/
For Same Language Countries                : /country-api/language/<str:language>/
For Prtially Search By Country Name        : /country-api/country-name/<str:country>/

Web Representation

For List of all countries                  : /country-api/all-country/
For List of neighbors of a country         : /country-api/countries/<int:country_id>/
