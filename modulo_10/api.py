import requests

# chave criada no site disponibilizado
API_KEY = "25287281d29bf235b8e6b6957375e083"
cidade = "Ipanema"

url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

retorno = requests.get ( url )

if retorno.status_code == 200 :

    dados = retorno.json ()
    temperatura = dados['main']['temp']
    clima = dados['weather'][0]['description']
    nome_cidade = dados['name']

    print (f"\n--- Previsão do tempo em\n: "
            f"{nome_cidade} está com {temperatura}°C"
            f" e as condição climáticas está: {clima.capitalize()}")
    print ("-"*20)

else :
    print ( "Ocorreu um erro ao obter os dados do tempo." )
    print ( f"Código de Erro: {retorno.status_code}" )
    print ( f"Mensagem da API: {retorno.json ().get ( 'message' )}" )
    print ( "Verifique se a cidade existe ou se sua API Key é válida." )