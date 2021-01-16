
## Pré requisitos

- Python3 instalado
- Git instalado
- Docker Instalado

## Testes

- Clone o repositório.

```bash
git clone https://github.com/leandro-matos/python-example-dockerpy
```

- Acesse o diretório

```bash
cd python-example-dockerpy
```

- Crie uma virtual env

```bash
python3 -m venv .venv
```

- Ative a virtual env

```bash
source .venv/bin/activate
```

- Instale as bibliotecas

```bash
pip install -r requirements.txt
```

- Execute o script para listar os containers e também logs de execução:

```bash
python testing_docker.py
```

- Execute o script passando como parâmetro o id do container para sua remoção:

```bash
python remove_container.py
```
