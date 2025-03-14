# Gocase Buddy Chatbot
### Visão geral:

O Gocase Buddy é um chatbot desenvolvido para otimizar a comunicação com influenciadores, garantindo mais eficiência e organização no processo de marketing de influência da Gocase. O bot automatiza tarefas como envio de briefings, agendamento de postagens, lembretes e feedbacks pós-campanha, proporcionando uma experiência fluida e humanizada.

### Tecnologias utilizadas:
### Amazon Lex

**Chatbot:** Para automatizar a comunicação com influenciadores, desde o primeiro contato até o envio de briefings e feedbacks.

**Por quê?** O Lex permite criar interfaces de conversação naturais, escaláveis e integradas com outras ferramentas da AWS.

### Amazon Rekognition

**Análise de Imagens:** Para analisar postagens de influenciadores e verificar se estão alinhadas com as diretrizes da campanha.

**Por quê?** O Rekognition detecta texto, objetos e rostos em imagens, ajudando a monitorar o engajamento e a qualidade do conteúdo.

### Amazon Bedrock

**Geração de Respostas Humanizadas:** Para garantir que a comunicação seja natural e personalizada.

**Por quê?** O Bedrock usa modelos de linguagem avançados (ex: Claude da Anthropic) para gerar respostas contextualizadas e próximas do tom humano.

### Amazon S3 e DynamoDB

**Armazenamento de Dados:** Para guardar briefings, feedbacks e informações dos influenciadores.

**Por quê?** Esses serviços são escaláveis e seguros, ideais para gerenciar grandes volumes de dados.

[<img src="https://img.shields.io/badge/Serverless_Framework-ff5242?logo=serverless&logoColor=white">](https://www.serverless.com) 
[<img src="https://img.shields.io/badge/AWS-CLI-fa8818?logo=amazon-web-services&logoColor=ffff&labelColor=232F3E">](https://aws.amazon.com/pt/cli/)
[<img src="https://img.shields.io/badge/AWS-S3-2cae05?logo=amazon-web-services&logoColor=ffff&labelColor=232F3E">](https://aws.amazon.com/pt/s3/)
[<img src="https://img.shields.io/badge/Amazon-DynamoDB-0a43e8?logo=amazon-web-services&logoColor=ffff&labelColor=232F3E">](https://aws.amazon.com/pt/pm/dynamodb/)
[<img src="https://img.shields.io/badge/Amazon-Bedrock-03ab9d?logo=amazon-web-services&logoColor=ffff&labelColor=232F3E">](https://aws.amazon.com/pt/bedrock/)
[<img src="https://img.shields.io/badge/Amazon-Rekognition-03ab9d?logo=amazon-web-services&logoColor=ffff&labelColor=232F3E">](https://aws.amazon.com/pt/rekognition/)



### Arquitetura do projeto
![arquitetura-base](./assets/logo.png) 

### Serviços AWS implementados
| Serviço AWS     | Descrição                                           | Implementação no Projeto                                              |
|-----------------|-----------------------------------------------------|-----------------------------------------------------------------------|
| API Gateway     | Gerencia as chamadas de API                         | Integra as requisições dos usuários com o backend                     |
| Lambda          | Funções sem servidor para processar a lógica        | Processa o texto e a lógica de resposta                               |
| S3              | Armazenamento de arquivos                           | Armazena as imagens enviadas pelos usuários                           |
| Lex             | Interface de voz para o chat                        | Permite que o usuário interaja com comandos de voz pelo chat          |
| Bedrock         | Geração de linguagem natural para simplificação     | Gera explicações simplificadas a partir do texto extraído             |
| Rekognition     | Reconhecimento de imagem e extração de texto        | Extrai o conteúdo textual das imagens enviadas                        |


### 💻 Outras Ferramentas Utilizadas

| Ferramenta      | Descrição                                           | Implementação no Projeto                                              |
|-----------------|-----------------------------------------------------|-----------------------------------------------------------------------|
| Telegram        | Plataforma de comunicação que permite a troca de mensagens instantâneas, chamadas de voz e vídeo, além de suporte a bots para integração com outros serviços | Interface escolhida para implementar com Lex                          |
| Serverless      | Framework para deploy sem servidor                  | Configuração e deploy das funções e APIs AWS                          |

## Pré-requisitos

Para utilizar o projeto, será necessário cumprir alguns pré-requisitos para que a máquina possua as ferramentas necessárias para rodar o projeto.

- AWS CLI: Necessário para configurar e autenticar a AWS no ambiente.
- Serverless Framework: Usado para simplificar o deploy e gerenciamento da infraestrutura serverless.
- Bibliotecas e Ferramentas: boto3 para interações com a AWS e Postman para simplificar o envio de solicitações HTTP.
## Configuração Inicial


Cumpridos os pré-requisitos iniciais, podemos fazer uma configuração inicial para possibilitar a execução do projeto.

1. Efetue o git clone do projeto 

```bash
git clone https://github.com/carlosrodrigues07/Gocase-Buddy.git
```

2. Instale o framework serverless em seu computador. Mais informações [aqui](https://www.serverless.com/framework/docs/getting-started) 

```bash
npm install -g serverless 
```
3. Instale todas as bibliotecas necessárias
```bash
pip install -r requirements.txt
```

4. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

5. Em seguida insira as credenciais e execute o comando conforme exemplo: 
  
```bash
serverless config credentials \ 
   --provider aws \ 
   --key AKIAIOSFODNN7EXAMPLE \ 
   --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 
``` 
  
Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:
  
```bash
$ aws configure 
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE 
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 
Default region name [None]: us-east-1 
Default output format [None]: ENTER 
```

## Deploy e Execução

 Para efetuar o deploy da solução na sua conta aws execute (acesse a pasta [visao-computacional](./ouvi-texto) ):
  
```bash
serverless deploy 
```
  
Depois de efetuar o deploy, vocẽ terá um retorno parecido com isso: 
  
```bash
Deploying Gocase dev (us-east-1)

✔ Service deployed to stack Gocase-dev (78s)

endpoints:
  POST - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/webhook
functions:
  webhook: Gocase-dev-webhook (9 kB)
```

### Executando serverless localmente com serverless offline

Alternativamente, também é possível emular API Gateway e Lambda localmente usando o plugin `serverless-offline`. Para fazer isso, execute o seguinte comando:

```bash
serverless plugin install -n serverless-offline
```

Ele adicionará o plugin `serverless-offline` a `devDependencies` no arquivo `package.json`, assim como o adicionará a `plugins` em `serverless.yml`.

Após a instalação, você pode iniciar a emulação local com:

```
serverless offline
```

Caso você queira incluir dependências de terceiros, você precisará usar um plugin chamado `serverless-python-requirements`. Você pode configurá-lo executando o seguinte comando:

```bash
serverless plugin install -n serverless-python-requirements
```
## Rotas de acesso

| Método | Endpoint                                                        | Descrição                                                                                       |
|--------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `POST` | https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/webhook | Gerencia eventos recebidos via webhook e executa a lógica correspondente.                      |

Exemplo de requisição teste:

```json 
{
	"message": {
    "chat": {
      "id" : XXXXXXXX
    },
    "text": "Olá, tudo bem?"
  }
}
``` 

Saída:
```json
{
	"message": ""Olá! Seja bem-vindo(a) ao suporte para influenciadores da Gocase. Como posso ajudar?\n\n"
        "1📍 Saber o endereço da Gocase\n"
        "2📄 Obter o briefing da campanha\n"
        "3❓ Tirar dúvidas\n\n"
        "Digite o número da opção desejada ou escreva sua pergunta!""
}
```
## Utilização do Chatbot com Telegram
 
## 📞 Contato

**Carlos Henrique**  
📧 Email: [ch.rodrigues098@gmail.com](ch.rodrigues098@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/carlos-henrique-rodri/](https://www.linkedin.com/in/carlos-henrique-rodri/)
