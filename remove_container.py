import docker
import sys

args = sys.argv

HOST_DOCKER ='unix://var/run/docker.sock'
client = docker.DockerClient(base_url=HOST_DOCKER)

def remove_container(container_id):
    try:
        get_id = client.containers.get(container_id)
        container_name = get_id.name
        try:
            remove = get_id.remove(force=True)
            print(f'{container_id} removido com sucesso.')
        except Exception as err:
            print(f'Falha ao remover o container {container_id}')
    except Exception as err:
        print(f'O Container {container_id} não localizado, tente novamente.')

if len(args) <=1 :
    print(f'\nPor favor informe o container_id, conforme o exemplo abaixo:')
    print(f'Exemplo: remove_container.py 1234\n')
else:
    container_id = args[1]
    remove_container(container_id)