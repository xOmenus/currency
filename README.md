# currency
Запускаем: 
    ```docker-compose up -d```

Логи выводятся в stdout контейнера.

**WARNING**: Если хостовая система не unix like, то небходимо в docker-compose.yaml закомментировать блок:

```bash
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
```
