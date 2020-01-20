from django.core import management
from django.core.management.commands import loaddata

def reset_database():
    management.call_command('flush', verbosity=0, interactive=False)

def create_session_on_server(email):
    session_key = management.call_command('create_session', {email})
    return session_key.strip()