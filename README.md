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
Сервис использует переменные:
```bash
  TIME_DELTA
  SQLDB_PATH
  CURRENCY
  BASE_CURRENCY
```
**TIME_DELTA**- отвечает за временной интервал обращения к API (принимает на вход еденичное значение)

**SQLDB_PATH**- отвечает за расположение файла с базой (принимает на вход еденичное значение)

**CURRENCY**- валюта курс которой мы хотим узнать относительно других (принимает на вход еденичное значение)

**BASE_CURRENCY**- валюта относительно которой получаем курс (принимает на вход список)
