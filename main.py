from menu_setter import connector

try:
    connector.connect()
except KeyboardInterrupt as e:
    print('\nbye bye!')

# 'Parsa', 'Ahmadian', 'PKPY', 'pk', '123'  --> str(list).replace('[', '').replace(']', '')
# Parsa, Ahmadian, PKPY, pk, 123 --> with ', '.join(list)
