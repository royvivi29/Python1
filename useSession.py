class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token 
        self.temp_counter = 0 
session = UserSession(101, 'a1b2c3d4e5')

attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')


for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')