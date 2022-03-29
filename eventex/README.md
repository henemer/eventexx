# Eventex

Sistema de Eventos encomendado pela Morena.

### Como desenvolver? 

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instação com o .env
6. Execute os testes.

```console
git clone https://github.com/henemer/eventexx.git wttd
cd wttd
python -m env .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python managem.py test
````

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku
3. Define uma SECRET_KEY segura para a instância
4. Defia DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku main --force
```
