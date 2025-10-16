# Monitor de Recursos do Sistema

Este projeto é um monitor simples e configurável de uso de CPU, memória RAM e disco, desenvolvido em Python.
Ele lê limites personalizados definidos em um arquivo .env e exibe avisos caso algum recurso ultrapasse o valor estipulado.

Ideal para uso em scripts automatizados, servidores locais ou sistemas embarcados que precisem de controle de desempenho leve e direto.

## Funcionalidades

- Monitora uso da CPU, RAM e disco.

- Permite definir limites personalizados através de variáveis no arquivo .env.

- Informa se o uso está normal ou acima do limite.

- Estrutura simples e clara, ideal para expansão futura.

 -Gera (ou prepara) o arquivo de log dos resultados.

## Dependências

Antes de rodar o projeto, instale as dependências necessárias:

`pip install psutil python-dotenv`

## Configuração do .env

Crie um arquivo chamado config.env na raiz do projeto e defina os limites desejados:

CPU_LIMITE=80
RAM_LIMITE=75
DISK_LIMITE=90

Caso alguma variável não seja definida, o script ignora sua verificação e informa isso no console.

## Como Executar

`python monitor.py`

O script exibirá no console algo como:

Limite de CPU definido pelo usuario: 80%
CPU: 45%
O USO DA CPU ESTÁ NORMAL

## Estrutura de Pastas
```📁 monitor-servidor
│
├── monitor.py              # Script principal
├── config.env              # Arquivo de configuração com limites
├── logs/
│   └── log.txt             # (em branco no início, reservado para logs futuros)
└── README.md               # Documentação do projeto
```

## Versionamento

O projeto segue o padrão Semantic Versioning (SemVer):

MAJOR.MINOR.PATCH

Versão atual: v1.0.0

Primeira versão funcional e estável do script.

## Licença

Este projeto está licenciado sob a MIT License — uso livre, desde que sejam mantidos os créditos ao autor.

Consulte o arquivo LICENSE
 para mais informações.