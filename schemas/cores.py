from pydantic import BaseModel
from typing import List
from model.cores import Cores

class CorSchema(BaseModel):
    """ Define como uma nova cor deve ser representada
    
    """
    nome: str = 'Azul'

class CorViewSchema(BaseModel):
    """ Define como uma cor de veículo deverá retornado: modelo
    """
    codigo: int = 1
    nome : str = 'Azul'

class CorBuscaEditSchema(BaseModel):
    """ Define como deverá ser passado as informação para a edição.
    
    """
    codigo : int = 1
    nome : str = 'verde'


class CorDeleteSchema(BaseModel):
    """ Define como a estrutura que vai fazer a exclusao da cor
    
    """
    codigo: int = 1
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