import requests
import sys



def main():
    # Does argument exist?
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    #If exist - try to convert - except: sys.exit()
    try:
        n = float(sys.argv[1])
    except ValueError:
            sys.exit("Command-line argument is not a number")

    #URl e KEY to access api
    url = "https://rest.coincap.io/v3/assets/bitcoin"
    api_key = "049edc6c463c5c37e849fa1374d5fdfa26e075b6c1b42ce2e74c940bd12003ea"

    try:
        r = requests.get(f"{url}?apiKey={api_key}")
    except requests.RequestException:
        sys.exit()

    # Convert to json(dict) and math price
    resposta = r.json()
    actual_price_btc = float(resposta["data"]["priceUsd"])
    total = n * actual_price_btc

    #print
    print(f"${total:,.4f}")


main()
