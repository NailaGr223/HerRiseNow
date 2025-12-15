from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'can_access_admin': True,
    }

class Partner(AbstractUserRole):
    available_permissions = {  
        'can_view_payments': True,
    }

class Sponser(AbstractUserRole):
    available_permissions = {
        'can_make_payment': True,
        'can_view_own_transactions': True,
    }
class User(AbstractUserRole):
    available_permissions = {
        'can_view_content': True,
        'can_participate_in_community': True,
    }