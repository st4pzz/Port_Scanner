
# Advanced Port Scanner

O **Advanced Port Scanner** é uma ferramenta desenvolvida em Python para escanear portas TCP de um host ou rede especificada. Ele possui uma interface gráfica amigável construída usando a biblioteca `tkinter`, que permite ao usuário iniciar o escaneamento de portas com facilidade. A aplicação também relaciona as portas mais conhecidas (Well-Known Ports) aos serviços associados, tornando-a uma ferramenta útil tanto para profissionais de segurança quanto para curiosos que desejam entender melhor a infraestrutura de rede.

## Características

- **Interface gráfica amigável**: A aplicação possui uma interface gráfica intuitiva e estilizada usando `tkinter` e `ttk`.
- **Escaneamento de portas TCP**: Permite escanear um intervalo especificado de portas TCP de um host.
- **Identificação de serviços conhecidos**: Relaciona portas conhecidas com os serviços que normalmente operam nessas portas.
- **Feedback em tempo real**: Exibe resultados do escaneamento diretamente na interface.

## Pré-requisitos

Para executar este programa, você precisa ter o Python instalado em seu sistema. O código é compatível com o Python 3.6 ou superior.

## Instalação

1. **Clone o repositório** (ou copie o código para um arquivo Python):

   ```bash
   git clone https://github.com/seu-usuario/advanced-port-scanner.git
   cd advanced-port-scanner
   ```

2. **Instale os pré-requisitos**:

   Este projeto utiliza bibliotecas padrão do Python, portanto, não há necessidade de instalar dependências adicionais. Certifique-se apenas de que o `tkinter` está instalado e disponível no seu ambiente Python.

## Uso

1. **Execute o script**:

   ```bash
   python advanced_port_scanner.py
   ```

2. **Insira as informações na interface gráfica**:
   - **Host**: Endereço IP ou nome do domínio do host que você deseja escanear.
   - **Start Port**: Número da porta inicial do intervalo de portas a serem escaneadas.
   - **End Port**: Número da porta final do intervalo de portas a serem escaneadas.
   
3. **Clique em "Start Scan"** para iniciar o escaneamento.

## Interface do Usuário

- **Campo de Host**: Onde você insere o endereço IP ou nome de domínio do host.
- **Campo de Porta Inicial**: Número da porta inicial para o escaneamento.
- **Campo de Porta Final**: Número da porta final para o escaneamento.
- **Botão "Start Scan"**: Inicia o escaneamento de portas no host especificado.
- **Área de Resultados**: Mostra as portas abertas e seus serviços associados após o escaneamento.

## Funcionalidades

### 1. Escaneamento de Portas

A aplicação utiliza sockets para tentar estabelecer conexões com as portas especificadas no intervalo dado. Para cada porta que responde, a aplicação adiciona essa porta à lista de portas abertas.

### 2. Identificação de Serviços

Após a detecção de uma porta aberta, o programa verifica no dicionário `WELL_KNOWN_PORTS` se há um serviço associado a essa porta. Se houver, ele exibe o serviço; caso contrário, exibe "Unknown Service".

## Exemplo de Uso

**Passo a Passo:**

1. Execute o script Python.
2. Na interface gráfica, insira `google.com` como o **Host**, `20` como a **Start Port** e `25` como a **End Port**.
3. Clique em **"Start Scan"**.
4. Observe o resultado na **Área de Resultados**. O programa listará as portas abertas e seus respectivos serviços.

## Contribuindo

Se você deseja contribuir para o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch para suas alterações (`git checkout -b minha-nova-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionei nova feature'`).
4. Faça push para a branch (`git push origin minha-nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.



---

**Advanced Port Scanner** - Simples, rápido e eficaz. Ideal para todos que desejam entender melhor as portas abertas em seus sistemas de rede!
```
