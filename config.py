from librouteros import connect
from librouteros.exceptions import TrapError


def connect_routeros(host, username, password, port):
    try:
        api = connect(host=host, username=username, password=password, port=port)
        return api
    except ConnectionError as e:
        print(f"Error connecting to RouterOS xonnection : {e}")
        return None
    except TrapError as e:
        print(f"Error connecting to RouterOS xtrap error: {e}")
        return None
    except Exception as e:
        print(f"Error connecting to RouterOS xexception: {e}")
        return None