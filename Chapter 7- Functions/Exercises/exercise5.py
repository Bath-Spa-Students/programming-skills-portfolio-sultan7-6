def describe_city(city, country='U.A.E'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Dubai')
describe_city('Riyadh', 'K.S.A')
describe_city('Al Ain')