import requests


_URL = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

def get_dolar_value(url):
    response = requests.get(url)
    dolar_data = response.json()

    valor_oficial = str2float(dolar_data[0]['casa']['venta'])
    valor_blue = str2float(dolar_data[1]['casa']['venta'])
    # print(f'Valor oficial: {valor_oficial}, valor blue: {valor_blue}')
    return {'oficial': valor_oficial, 'blue': valor_blue }


def str2float(value):
    x = value.replace(',', '.')
    return float(x)

if __name__ == '__main__':

    result = get_dolar_value(_URL)
    print(result)


