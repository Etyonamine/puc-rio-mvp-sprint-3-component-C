from sqlalchemy import Column, String, Integer, ForeignKey
from model import Base
from sqlalchemy.orm import relationship

class Veiculo(Base):
    __tablename__ = 'veiculo'
    cod_veiculo = Column("pk_veiculo", Integer, primary_key=True)
    des_placa = Column(String(100), unique=True)
    cod_modelo = Column(Integer,
                         ForeignKey("modelo.pk_modelo"),
                        nullable=False)
    id_cor = Column(Integer, 
            ForeignKey("cores.id_cor"),
                        nullable=False
    )

    ## criar o vinculo com o modelo do veiculo
    modelo = relationship("Modelo", back_populates="veiculos")
    cor = relationship("Cores", back_populates = "veiculos_cores")
        
    def __init__(self, placa: str, codigo_modelo: Integer, codigo_cor: Integer):
        """
        Cria uma modelo de veiculo de marca especifica

        Argumentos:
            des_placa: placa
            cod_modelo: codigo_modelo
            id_cor: codigo da cor do veiculo
        """
        self.des_placa = placa
        self.cod_modelo = codigo_modelo
        self.id_cor = codigo_cor



    