import asyncio
import threading
import Database
import Website

from Announcement import main_loop


def parse_size(amount, type):
    match type:
        case 'b':
            return amount

        case 'kb':
            return amount * (10 ** 3)

        case 'mb':
            return amount * (10 ** 6)


db_instance = Database.Database("torrents_and_clients.db")
torrent_list = db_instance.return_torrent_list()
client_list = db_instance.return_client_list()


def main(torrent_list, client_list, db_instance):
    asyncio.run(main_loop(torrent_list, client_list, db_instance))


threading.Thread(target=main, args=(torrent_list, client_list, db_instance)).start()
Website.main(torrent_list, client_list)

# main(torrent_list, client_list, db_instance)
