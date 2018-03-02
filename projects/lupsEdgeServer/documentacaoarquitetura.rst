Documentação da Arquitetura
***************************

A Figura apresenta o diagrama do novo Servidor de Borda desenvolvido, ilustrando os módulos que o compõem e os caminhos no processamento de informações.

.. image:: SB_Fog.png


SB-API
======

A SB-API é implementada sobre um web-server sendo responsável por toda e qualquer requisição proveniente de clientes ativos no momento, criando novos eventos para o mesmo. Os dados são recebidos via HTTP por requisição REST pela SB-API, e enviados tanto para o banco de dados, como para o Módulo de Interoperação em formato JSON. 

Através de um servidor RestFul utilizando o framework DJango (https://www.djangoproject.com/), as requisições são processadas nos padrões REST para o acesso às informações e aos serviços do Servidor de Borda. 

Na Tabela 1 são apresentados as possíveis URI's de acesso à SB-API. Esses recursos podem ser acessados pelos seguintes endereços: groups, users, manufacturers, gateways, actuators, baseParameters, contextServers, sensorsTypes, sensors, persistances, rules, schedules e topicos.




Tabela 1: Tabela URI do SBCore

+-------+---------------+-----------------------------------+
| Verbo | URI           | Descrição                         |
+=======+===============+===================================+
| GET   | IP            | Lista todos os tipos de recursos  |
+-------+---------------+-----------------------------------+
| GET   | IP/Recurso    | Lista um tipo de recurso          |
+-------+---------------+-----------------------------------+
| POST  | IP/Recurso    | Insere um recurso                 |
+-------+---------------+-----------------------------------+
| PUT   | IP/Recurso/ID | Atualiza informações do recurso   |
+-------+---------------+-----------------------------------+
| PATCH | IP/Recurso/ID | Atualiza informações do recurso   |
+-------+---------------+-----------------------------------+
| GET   | IP/Recurso/ID | Informações do recurso            |
+-------+---------------+-----------------------------------+
| DELETE| IP/Recurso/ID | Deleta o recurso                  |
+-------+---------------+-----------------------------------+


SB-Core
=======

O SB-Core é responsável pela atuação e processamento dos dados cadastrados na SB-API, bem como pelo acionamento de regras sobre os eventos a serem tratados. As mensagens transferidas entre cada um dos módulos estão formatadas em JSON, dessa forma ocorre a padronização na passagem dos argumentos necessários para atuação de cada etapa do Servidor de Borda. Quando a SB-API recebe dados do Servidor de Contexto, a mesma salva as informações no Banco de Dados, comunicando o SB-Core sobre uma possível inserção de um novo sensor ou de um  agendamento. Os agendamentos são registrados para sensores previamente cadastrados. Na Tabela podem ser visualizadas as URI's utilizadas.

Agendador
---------

O Agendador tem a funcionalidade de escalonar os eventos períodicos cadastrados no banco de dados da SB-API, como eventos típicos teríamos aqueles relacionados a leitura de sensores e a ativação de atuadores. Por sua vez, os eventos aperiódicos produzidos por outros Servidores de Borda são recebidos através do Módulo de Interoperação. 
    
Para a execução das tarefas segundo as demandas das aplicações dos usuários, utilizou-se uma biblioteca implementada em Python,    *Advanced Python Scheduler*(APScheduler). O *APScheduler* permite o cadastro de uma ação, considerando que a tal seja executada periodicamente ou apenas uma vez, permitindo a adição de novas tarefas e gerência de tarefas já cadastradas. 
    
A biblioteca *APScheduler* possui três modos de atuação que pode ser chamado, entre eles: 
    
	* **Cron-style scheduling**: é o modo mais completo, possui todos requisitos do \textit{CRON} e funcionalidades de adicionar horário de início e de fim nas atuações de tarefas;
    
    	* **Interval-based execution**: executa as tarefas com intervalos regulares, com a opção de adicionar horário de início e término;
        
    	* **One-off delayed execution**: executa uma única tarefa, determinada por data e horário específicos.
        


    
Gerenciador de Operação
-----------------------

Esse módulo tem como objetivo principal gerenciar a interoperação do Agendador com os demais módulos, ou seja, toda comunicação entre os módulos é direcionada pelo tratador de eventos, transformando cada comunicação em eventos.
  
Ao receber os dados, este módulo verifica o tipo de evento a ser realizado, entre eles: atuação, coleta e publicação. Após a verificação, um novo caminho é instanciado, repassando os argumentos necessários para o processamento no próximo módulo. 
    
    
Módulo de Atuação
-----------------

Realiza a requisição de atuação através do módulo de comunicação, transmitindo uma mensagem JSON com os parâmetros necessários para identificar um determinado atuador conectado em um dos gateways ativos.


Módulo de Publicação
--------------------

Responsável por efetuar a publicação do dado contextual no Servidor de Contexto e também por realizar a persistência local quando necessário. Recebe como parâmetros de publicação o *id* do Gateway, o *id* do sensor e o valor coletado. O endereço do Servidor de Contexto é montado através destas informações os dados contextuais são publicados no mesmo.

Caso a publicação não possa ser efetuada, o dado é armazenado em banco de dados local, para que a publicação ocorra posteriormente. A cada inicialização do Servidor de Borda é verificado no banco local possíveis dados não enviados ao Servidor de Contexto, realizando os envios pendentes.


Módulo de Coleta
----------------

Este Módulo realiza a requisição de coleta ao Módulo de Comunicação, enviando uma mensagem no formato JSON com os parâmetros necessários para a ação de coleta. Após o recebimento dos dados, os mesmos são repassados ao Motor de Regras para o seu processamento.

    
Motor de Regras
---------------

Este motor de regras recebe os dados contextuais formatados em JSON e realiza o processamento das regras cadastradas, podendo também realizar a requisição de coleta para uma combinação de eventos de contexto, ou mesmo uma requisição de atuação sob o ambiente.

O Motor de Regras(https://github.com/venmo/business-rules) é implementado em Python, de código aberto e sendo possível altera-lo para uso em fins específicos.


Módulo de Comunicação
---------------------

O Módulo de Comunicação é responsável por realizar as requisições de atuação e coleta do Servidor de Borda aos gateways. Realizando uma combinação do *UUID* do sensor ou atuador, procurando o IP de acesso a este gateway. Pode-se observar na Tabela, o formato das URI's utilizadas no acesso.


Módulo de Interoperação
-----------------------

O Módulo de Interoperação emprega um Servidor HTTP, recebendo notificações compostas de novos sensores e agendamentos cadastrados no Servidor de Borda pelo Servidor de Contexto, repassando ao Módulo Agendador em tempo real. Essas URI's de acesso, podem ser visualizadas na Tabela.

Outra funcionalidade provida pelo Módulo de Interoperação é permitir que os Servidores de Borda requisitem grandezas físicas do ambiente (dados contextuais) coletadas por outros Servidores de Borda.

SB-IPC
------

O Módulo SB-IPC utiliza o protocolo de comunicação *Message Queue Telemetry Transport*(MQTT) para troca de dados. Este protocolo de comunicação é baseado na arquitetura *publish/subscribe*, criado para redes inseguras e dispositivos restritos, com baixa largura de banda e alta latência.

Como característica o MQTT utiliza o protocolo da camada de transporte TCP/IP para fornecer conectividade, pequena sobrecarga de transporte e trocas minimizadas de mensagens para reduzir o tráfego de dados transportados na rede. Possui também um mecanismo que notifica quando um cliente se desconecta da rede de forma não prevista.

O protocolo segue o modelo cliente/servidor, onde os dispositivos sensoriados são os clientes que se conectam a um servidor chamado Broker, usando TCP/IP. Os clientes podem subscrever em diversos tópicos, e são capazes de receber as mensagens de diversos outros clientes que publicam neste tópico. 

Dessa forma, este módulo recebe dados de outros Servidores de Borda que são de seu interesse. Entre os dados recebidos, temos o dado contextual coletado e a regra relacionada a este dado. Os dados recebidos por este módulo são transmitidos ao Motor de Regras.
