import config
import interface


api = config.connect_routeros('192.168.182.3', 'admin', '123', '8728')
interface.interface_info(api)













