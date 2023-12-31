from pydantic import BaseModel
from model.modelo import Modelo
from typing import List
from model import Base

from schemas import MarcaViewSchema

class ModeloSchema(BaseModel):
    """Define como um novo registro de modelo de veículo será inserido """    
    nome: str = "Onix"
    codigo_marca: int = 1

class ModeloViewSchema(BaseModel):
    """ Define como uma modelo de veículo deverá retornado: modelo
    
    """

    codigo: int = 1
    nome: str = "GM"  
    codigo_marca = int = 1 
    marca: MarcaViewSchema  
    nome_marca: str = 'GMW'

class ModeloEditSchema(BaseModel):
    """Define como será recebido os dados para a edição """
    codigo: int = 1
    nome: str = 'GM-EUA'  
    marca_id: int = 44  

class ModeloBuscaDelSchema(BaseModel):
    """ Define como a estrutura que representa a busca de delete.Que será
        feita apenas com o codigo do  .

    """
    codigo: int = 1


class ListaModelosSchema(BaseModel):
    """ Define como retorna a lista de marcas de veiculos.
    """
    modelos: List[ModeloViewSchema]


class ModeloBuscaPorMarcaSchema(BaseModel):
    """ Define como a estrutura que representa a busca de modelos 
        que possuam o codigo da marca.

    """
    codigo_marca: int = 1


def apresenta_modelo(modelo: Modelo):
    """ Retorna uma representação de um modelo de veiculo seguindo o schema definido em
        ModeloViewSchema.
    """
    return {
        "codigo": modelo.cod_modelo,
        "nome": modelo.nom_modelo,
        "codigo_marca": modelo.cod_marca,
        "marca": [{"codigo": modelo.marca.cod_marca,"nome": modelo.marca.nom_marca}],
        "nome_marca": modelo.marca.nom_marca
    }


def apresenta_lista_modelo(lista: List[Modelo]):
    """ Retorna uma representação do modelo seguindo o schema definido em
        ModeloViewSchema.

    """
    result = []
    for item in lista:
       
        result.append({
            "codigo": item.cod_modelo,
            "nome": item.nom_modelo,
            "codigo_marca": item.cod_marca,
            "marca": [{"codigo": item.marca.cod_marca,"nome": item.marca.nom_marca}], 
            "nome_marca": item.marca.nom_marca
        })

    return {"lista": result}    



