import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_old import Lead, Base

# Configuração do banco de dados SQLite
DATABASE_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DATABASE_URL)

# Cria as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Função para gerar leads fictícios
def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
    emails = ['johndoe@gmail.com', 'janesmith@gmail.com', 'chrisjohnson@gmail.com', 'patriciabrown@gmail.com', 'michaelwilliams@gmail.com']
    telefones = ['(11) 91234-5678', '(21) 98765-4321', '(31) 99876-5432', '(41) 94567-8901', '(51) 91234-6789']

    for _ in range(100):
        name = random.choice(names)
        email = random.choice(emails)
        telefone = random.choice(telefones)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)

        # Cria uma instância de Lead e adiciona à sessão
        lead = Lead(name, email, telefone, latitude, longitude, temperature, interest)
        session.add(lead)

    # Faz o commit de todas as operações no banco de dados
    session.commit()

# Executa a função para gerar os leads ao rodar o script
if __name__ == '__main__':
    generate_leads()
    print("Leads gerados e salvos no banco de dados com sucesso!")
