from librouteros import connect


def interface_info(api):
    interfaces = api.path('interface')
    for i in interfaces:
        print(f"{i.get('name')}:  rx: {i.get('rx-byte')} - rx: {i.get('tx-byte')} ")

        