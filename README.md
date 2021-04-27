# Crie uma Network no Docker
```bash
docker network create devtube
```

# Banco de Dados

```bash
docker build -t devtube_mysql_img -f docker/Dockerfile.mysql .
```

```bash
docker run -d -e MYSQL_ROOT_PASSWORD=root --network devtube --name devtube_mysql devtube_mysql_img
```

Espere 30 segundos para o Mysql Subir

```bash
docker exec -it devtube_mysql mysql -uroot -proot -e "source /mydata/database_create.sql"
```

# Aplicação
```bash
docker build -t devtube_app_img -f Dockerfile .
```
```bash
docker run -d --network devtube --name devtube_app devtube_app_img
```
```bash
docker exec devtube_app python3 manage.py collectstatic --no-input
```

## Nginx
```bash
docker build -t devtube_nginx_img -f docker/Dockerfile.nginx .
```
```bash
docker run -d -p 8080:80 --network devtube --name devtube_nginx devtube_nginx_img
```

# Deployment
- Acesse http://localhost:8080

Páginas para cadastrar curso:
http://localhost:8080/admin (usuário: admin senha: admin)