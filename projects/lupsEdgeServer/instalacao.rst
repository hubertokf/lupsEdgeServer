Instalação
**************************

Nessa etapa é explicado o passo a passo da instalação e os comandos a ser utilizados.


Ponto Inicial
=========================

1. Passo:
	Instalar o python3 e pip:

	* sudo apt-get install python3
	* sudo apt-get install python3-pip

2. Passo:
	Acesse a pasta de destino e execute o arquivo para instalar as dependências:

	* cd lupsEdgeServer/projects/lupsEdgeServer/
	* sudo ./installPackages 

3. Passo:
	Acesse a pasta de destino para instalar o Motor de Regras:

	* cd lupsEdgeServer/projects/lupsEdgeServer/EngineRules
	* sudo python3 setup.py install


4. Passo:
	Acesse a pasta de destino para criar/atualizar o Banco de Dados:

	* cd lupsEdgeServer/projects/lupsEdgeServer/
	* python manage.py makemigrations
	* python manage.py migrate

5. Passo
	Inicializa o serviço

	* ./runserver



.. warning:: Folder "lupsEdgeServer/projects/lupsEdgeServer/" is mother, where you will find the installation files and execution