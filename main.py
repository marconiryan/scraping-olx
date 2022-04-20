from requests_html import *
import json


class HtmlContent:
    def __init__(self, URL):
        self.url = URL
        self.session = HTMLSession()
        self.asession = AsyncHTMLSession()
        self.requisicao = None
        self.asession.run(self._get_request)

    async def _get_request(self):
        self.requisicao = self.session.get(self.url)

    def get_link(self):
        return self.requisicao.html.links

    def get_element(self):
        return self.requisicao.html.find('#initial-data', first=True)

    def get_str(self):
        return self.get_element().attrs['data-json']

    def get_json(self):
        return json.loads(self.get_str())

    def get_next_link(self):
        if self.get_json()['listingProps']['nextPageLink'] == 'null':
            return None
        return self.get_json()['listingProps']['nextPageLink']

    def get_totalAds(self):
        return self.get_json()['listingProps']['totalOfAds']

    def get_paglimit(self):
        return int(self.get_totalAds()) // 50

    def get_current_page(self):
        return self.get_json()['listingProps']['pageIndex']


def get_prod(Anuncio: HtmlContent):
    produtos = Anuncio.get_json()['listingProps']['adList']
    for prod in produtos:
        try:
            print('\n----------------')
            print(prod['subject'])
            print(prod['price'])
            print(prod['url'])
            print('----------------\n')
        except KeyError:
            continue


def set_keyword_estate() -> str:
    keyword: str = input("Pesquisar:")
    print(
        "0.Brasil\n1.Acre\n2.Alagoas\n3.Amazonas\n4.Amazonas\n5.Bahia\n6.Ceará\n7.Distrito Federal\n8.Espirito Santo\n"
        "9.Goias\n10.Maranhão\n11.Minas Gerais\n12.Mato Grosso do Sul\n13.Mato Grosso\n14.Paará\n15.Paraíba\n"
        "16.Pernambuco\n17.Piauí\n18.Paraná\n19.Rio de Janeiro\n20.Rio Grande do Norte\n21.Rondônia\n22.Roraima\n"
        "23.Rio Grande do Sul\n24.Santa Catarina\n25.Sergipe\n26.São Paulo\n27.Tocantins")
    estate: int = int(input(":"))
    estados: dict = {1: 'ac', 2: 'al', 3: 'am', 4: 'ap', 5: 'ba', 6: 'ce', 7: 'df', 8: 'es', 9: 'go', 10: 'ma',
                     11: 'mg', 12: 'ms', 13: 'mt', 14: 'pa', 15: 'pb', 16: 'pe', 17: 'pi', 18: 'pr', 19: 'rj', 20: 'rn', 
                     21: 'ro', 22: 'rr', 23: 'rs', 24: 'sc', 25: 'se', 26: 'sp', 27: 'to'}
    try:
        return f'https://{estados[estate]}.olx.com.br/?o=1&q={keyword}'
    except KeyError:
        return f'https://olx.com.br/brasil?o=1&q={keyword}'


def set_url() -> list:
    URL: str = set_keyword_estate()
    opt: int = int(input("0.Pagina Especifica\n1.Todas as Paginas\n:"))
    if not opt:
        pagina: int = int(input("Pagina:"))
        return [URL.replace('o=', f'o={pagina}'), False]
    return [URL, True]


if __name__ == '__main__':
    url, all_pages = set_url()
    while True:
        try:
            anuncio = HtmlContent(url)
            get_prod(anuncio)
            if not all_pages:
                break
            if anuncio.get_current_page() <= anuncio.get_paglimit():
                url = anuncio.get_next_link()
            else:
                break

        except Exception as e:
            print(f"Erro{e}\n\n")
            break
