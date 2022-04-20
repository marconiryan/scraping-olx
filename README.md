# Web Scraping 

O script pega titulo, preço e link do anuncio, conforme a pesquisa. 

<img src="https://github.com/marconiryan/scraping-olx/blob/main/demo.gif"/>

#
### Como utilizar

~~~console
user:~$ python3 -m pip install -r requirements.txt 
~~~
~~~console
user:~$ python3 main.py
~~~


### Pesquisa
* A pesquisa pode ser feita em uma pagina especifica ou em todas as páginas encontradas. 
* O filtro de pesquisa pode ser realizada por estados ou por todo o país.

# 
### Personalização
Para personalizar o resultado da pesquisa basta seguir o [Exemplo](https://github.com/marconiryan/scraping-olx/blob/main/exemplo.json), usando a função *get_json()* 
``` Python
def get_json(self):
        return json.loads(self.get_str())


get_json()['listingProps']['pageIndex'] # Exemplo para retornar a página atual.
```

## Termos de Uso
Script feito para meios didáticos.<br>Foi contatado com a empresa sobre a utilização do script e não foi obtido nenhuma resposta.<br>Portanto, não me responsabilizo por nenhuma prática criminosa e por nenhuma violação nos termos de uso do site. 

