from sqlalchemy import Column, String, Integer
from model import Base
from sqlalchemy.orm import relationship

class Cores(Base):
    __tablename__ = 'cores'
    codigo = Column("id_cor", Integer, primary_key=True)
    nome = Column("nom_cor", String(100), unique=True)

    ## criar o vinculo com os modelos do veiculo
    veiculos = relationship("Veiculo", cascade="all,delete",
                                back_populates="cor") 
    
    def __init__(self, nome: str):
        """
        Cria a cor do veiculo

        Argumentos:
            nome: nome da cor do veiculo
        """
        self.nome = nome
