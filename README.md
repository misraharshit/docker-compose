# Steps to run the docker containers

1. Clone the required repo in your workstation and install docker and docker-compose. Then run below command:

```bash
	docker-compose up --build -d
```
2. To check the output of the metrics from the metrics container service:

```bash
	curl localhost:5050
```

3. To check response of docker-challege app.

```bash
	curl localhost:80
```


