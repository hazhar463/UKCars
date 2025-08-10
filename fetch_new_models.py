import json
import urllib.request
import argparse

def fetch_new_models(year: int):
    """Fetch a list of car models and their prices for a given year using CarQuery API."""
    url = f"https://www.carqueryapi.com/api/0.3/?cmd=getTrims&year={year}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
    trims = data.get('Trims', [])
    results = []
    for item in trims:
        results.append({
            'make': item.get('model_make_id'),
            'model': item.get('model_name'),
            'price': item.get('model_price')
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Retrieve new car models and their prices")
    parser.add_argument('--year', type=int, default=2024, help='Year of car models to fetch')
    args = parser.parse_args()
    cars = fetch_new_models(args.year)
    for car in cars:
        price = car['price'] or 'N/A'
        print(f"{car['make']} {car['model']}: {price}")

if __name__ == '__main__':
    main()
