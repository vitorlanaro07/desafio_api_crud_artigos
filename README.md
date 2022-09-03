# desafio_api_crud_artigos
Desafio sugerido pela Devnology. (Criar uma api que salve links de artigos de tecnologias e seus respecitivos labels + automatização)

# Desafio completo
Para começar a explicação do que foi realizado queria agradecer pela a oportunidade que estão me dando, acredito atender as expectativas do que foi pedido.
Bom, essa API foi escrita em Python na versão 3.10, a principio, minha intenção era gerenciar as dependencias com pipenv mas acabou gerando alguns conflitos na aplicação,como resolução para isso optei pelo venv para a criação do ambiente virutal e controle de dependencias ficaram no arquivo "requirements.txt", utilizei do micro-framework web Flask, hospedei na Amazon ES2 em um VM-linux, utilizei o banco MySQL que também está hospedado na Amazon RDS, por se tratar de um aplicacao POO foi necessario a utilizão de um ORM(SQLAlchemy) para conversar com o DB, e também utilizei os conectores do MySQL com Python, por se tratar de um CRUD todas as operaões estão presentes e devidamente validadas, utilizei de web-scraping(BeautifulSoup4) para extrair os titulos/labels dos artigos e também de suas respectivas 'href' ou url. No que diz respeito a interface, foi utilizizado HTML, CSS e um pouco de JS, para CSS tento aproximar o meu código ao máximo possível do padrão BEM (Block-Element-Modifier).
Basicamente, é isso!
 
O Link para acesso a API é: http://ec2-54-158-72-226.compute-1.amazonaws.com:80 ou http://54.158.72.226
