from pydantic import BaseModel
from typing import List
from model import Base
from model.cores import Cores
 
class CorViewSchema(BaseModel):
    """ Define como uma cor de veículo deverá retornado: modelo
    """
    codigo: int = 1
    nome : str = 'Azul'


class CorBuscaSchema(BaseModel):
    """ Define como a estrutura que representa a busca de uma cor.Que será
        feita apenas com o codigo da cor .

    """
    codigo: int = 1


class ListaCoresSchema(BaseModel):
    """ Define como retorna a lista de cores de veiculos.
    """
    cores: List[CorViewSchema]


def apresenta_cor(cor: Cores):
    """ Retorna uma representação de uma cor de veiculo seguindo o schema definido em
       CorViewSchema.
    """
    return {       
            "codigo": cor.codigo,
            "nome": cor.nome
    }


def apresenta_lista_cores(lista: List[Cores]):
    """ Retorna uma representação de cores de veiculos seguindo o schema definido em
        CorViewSchema.

    """
    result = []
    for item in lista:       

        result.append({
            "codigo": item.codigo,
            "nome": item.nome         
        })

    return {"lista": result}    