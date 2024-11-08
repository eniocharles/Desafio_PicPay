from ninja import Router
from .schemas import UserSchema, TypeUserSchema
from .models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

users_router = Router()

@users_router.post('/', response={200: dict, 400 : dict, 500 : dict})
def create_user(request, type_user_schema: TypeUserSchema):
    user = User(**type_user_schema.user.dict())
    user.password = make_password(type_user_schema.user.password)   # As senhas são armazenadas com hashing
    try:
        user.full_clean()
        user.save()
        assign_role(user, type_user_schema.type_user.type)  # Permite que apenas usuários autorizados realizem certas ações
    except ValidationError as e:
        return 400, {'errors': e.message_dict}
    except Exception as e:
        return 500, {'errors': 'Erro interno do servidor, contate o admin'}

    return {'user_id': user.id}

'''
Objetivo: Permitir a comunicação com o sistema, criando usuários, validando dados, e atribuindo papéis.

Endpoint /create_user:
    1° Recebe um TypeUserSchema, contendo informações do usuário e o tipo.
    2° Cria um novo usuário com os dados recebidos e realiza as seguintes operações:
        -Usa make_password para armazenar a senha de forma segura (hashing).
        -Valida todos os campos usando user.full_clean(), que checa o cpf e outros dados.
        -Salva o usuário no banco e atribui o papel (People ou Company) com assign_role.
'''
