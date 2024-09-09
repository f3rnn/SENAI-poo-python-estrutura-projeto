import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco

os.system("clear")

pessoa_um = Pessoa("dejair", 23, Sexo.MASCULINO, Endereco("avenida rua", 123))
print(pessoa_um)