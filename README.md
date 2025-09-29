# Sistema de Notificações com RabbitMQ 📨

Este projeto é um pequeno teste de integração do **RabbitMQ com Python**, utilizando um **produtor** e dois **consumidores** para simular um sistema de notificações de usuários.

## 🔹 Como funciona
- O **produtor** envia mensagens JSON para a *exchange* `user_events`.
- As mensagens são roteadas para duas filas:
  - **login_queue** → recebe apenas eventos de login.
  - **log_queue** → recebe todos os eventos (login, upload e logout).
- Os **consumidores** leem as filas e exibem as mensagens no console.

## 📂 Estrutura do projeto
```
.
├── config.py
├── produtor.py
├── consumidor_login.py
├── consumidor_log.py
└── README.md
```

## ▶️ Como rodar

1. Certifique-se de que o **RabbitMQ** está rodando na sua máquina:
   ```bash
   rabbitmq-server
   ```

2. Abra **três terminais** diferentes e rode:
   ```bash
   python consumidor_login.py
   python consumidor_log.py
   python produtor.py
   ```

3. Resultado esperado:
   - Consumidor de login:
     ```
     [LOGIN] João acabou de fazer login!
     ```
   - Consumidor de log:
     ```
     [LOG] João executou o evento: user.login
     ```

## 📌 Objetivo
Aprender os conceitos básicos de **mensageria com RabbitMQ** e integração com **Python**, usando **produtor e consumidores** para simular eventos.

## 🔹 Dependências
- Python 3.10+
- Pika (`pip install pika`)
- RabbitMQ
