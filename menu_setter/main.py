from modules import connector

connector.connect()
# 'Parsa', 'Ahmadian', 'PKPY', 'pk', '123'  --> str(list).replace('[', '').replace(']', '')
# Parsa, Ahmadian, PKPY, pk, 123 --> with ', '.join(list)