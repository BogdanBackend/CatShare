from threading import Thread, Event
from datetime import datetime
import logging
from server import start_server
from icon import create_icon

logging.basicConfig(level=logging.INFO)

def close(icon, item):
    time_start_close = datetime.now()
    logging.info('Closing app...')
    server_stop_event.set()
    icon.stop()
    logging.info(f'App closed after {datetime.now() - time_start_close}')

if __name__ == '__main__':
    server_stop_event = Event()
    server_thread = Thread(target=start_server, args=(server_stop_event,))
    server_thread.daemon = True
    server_thread.start()

    icon = create_icon(close)
    icon.run()
print('sd')