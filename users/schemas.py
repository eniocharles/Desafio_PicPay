from ninja import ModelSchema, Schema
from .models import User

class UserSchema(ModelSchema):
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'cpf', 'email', 'password']

class TypeSchema(Schema):
    type: str  

class TypeUserSchema(Schema):
    user: UserSchema
    type_user: TypeSchema

'''
Objetivo: Definir como os dados são enviados e recebidos pela API,
usando Django Ninja para criar schemas que facilitam o gerenciamento e a validação de dados.

UserSchema: Estrutura que representa os dados do usuário, como são enviados e recebidos pela API.

TypeSchema e TypeUserSchema: Estruturas que permitem definir o tipo de usuário (ex. People ou Company) ao criar uma conta na API.
'''