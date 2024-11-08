from rolepermissions.roles import AbstractUserRole

class People(AbstractUserRole):
    available_permissions = {
        'make_transfer' : True,
        'receive_transfer': True
    }

class Company(AbstractUserRole):
    available_permissions = {
        'make_transfer': False,
        'receive_transfer': True
    }

"""
Objetivo: Controlar o que cada tipo de usuário pode fazer dentro do sistema, como acessar recursos ou realizar transações.

People: Pode realizar e receber transferências financeiras.
Company: Apenas pode receber transferências.
"""