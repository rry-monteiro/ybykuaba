import urllib.parse
import webbrowser

# motor de busca que vamnos usar
MOTOR: str = "https://duckduckgo.com/?q="


def search(query: str) -> None:
    """
    transforma o query em uma url com o motor + busca parseada pelo urllib
    e manda pro webbrowser, não retorna nada
    """
    busca: str = urllib.parse.quote(query)
    url: str = MOTOR + busca
    webbrowser.open(url)
