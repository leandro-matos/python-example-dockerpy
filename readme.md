
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
Output

```bash
Versão do Docker Engine: 20.10.1
****************************************

Listando Containers em Execução: 

9ecd7af223 - optimistic_tereshkova - running
d790ade6ae - cranky_shaw - running
****************************************

Lendo Logs do Container cranky_shaw: 

b'/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration'
b'/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/'
b'/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh'
b'10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf'
b'10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf'
b'/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh'
b'/docker-entrypoint.sh: Configuration complete; ready for start up'
```

- Execute o script passando como parâmetro o id do container para sua remoção:

```bash
python remove_container.py {id}
```

Output

```bash
{id} removido com sucesso.
```