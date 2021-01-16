import docker

HOST_DOCKER ='unix://var/run/docker.sock'
client = docker.DockerClient(base_url=HOST_DOCKER)

docker_info = client.version()
components = docker_info['Components']

for component in components:
    if component['Name'] == 'Engine':
        version = component['Version']
        print(f'\nVersão do Docker Engine: {version}')
print('*'*40)
print('\nListando Containers em Execução: \n')

container_list = client.containers.list()

for container in container_list:
    container_short_id = container.short_id
    container_name = container.name
    container_attrs = container.attrs
    container_status = container.attrs['State']['Status']
    print(f'{container_short_id} - {container_name} - {container_status}')
print('*'*40)

try:
    print(f'\nLendo Logs do Container {container_name}: \n')
    container_id = container_short_id
    get = client.containers.get(container_id)
    for line in get.logs(stream=True):
        print(line.strip())
except Exception as err:
     print('\nNão há conteiners em execução !!')
print('*'*40)



