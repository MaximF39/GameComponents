import time
import threading
from socket import socket
from loguru import logger

from .Game.Components.MovableSpaceObject import MovableSpaceObject
from .Packages.PackageCollector import PackageCollector
from .Packages.PackagesReader import PackagesReader
from .Packages.PackageDecoder import PackageDecoder
from .Config import cfg_server
from .StarWars import StarWars
from .Static.Type.Package.T_ServerRequest import T_ServerRequest
from .Static.Type.Package.T_UpdateValue import T_UpdateValue


class Server:
    host: str = cfg_server.host
    port: int = cfg_server.port
    server: socket
    cnt_listen = 100
    online = 0

    def __init__(self):
        self.start = time.time()
        self.id_to_conn = {}
        self.conn_to_id = {}
        self.Game = StarWars(self)


    def main(self) -> None:
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(self.cnt_listen)

        end = time.time()
        print("Сервер запущен и готов слушать юзеров\nза", end - self.start)

        threading.Thread(target=self.wait_user).start()
        threading.Thread(target=self.send_pack).start()

    @staticmethod
    def send_pack():
        while 1:
            for class_ in MovableSpaceObject.all:
                class_.move()
            for Pack in PackageCollector.all:
                Pack.send()
            time.sleep(1)

    def wait_user(self):
        try:
            while True:
                conn, addr = self.server.accept()
                if conn:
                    threading.Thread(target=self.entry_user, args=(conn,)).start()
        except Exception as e:
            print(10 * '\n', e)
            print("Отключаю сервер")

    def entry_user(self, conn):
        self.online += 1
        Player = self.authorisation_package(conn)
        self.send_Packages(Player)
        self.get_packages(conn, Player)

    @staticmethod
    def send_Packages(Player):
        Player.Pack += ((
            T_ServerRequest.VERSION,
            T_ServerRequest.ONLINE,
            T_ServerRequest.TOP_LIST,
            T_ServerRequest.TOP_CLANS_LIST,
            T_ServerRequest.TOP_RATING_LIST,
            T_ServerRequest.WEAPONS_PARAMETERS,
            T_ServerRequest.AMMOS_PARAMETERS,
            T_ServerRequest.RESOURCE_PARAMETERS,
            T_ServerRequest.ENGINES_PARAMETERS,
            T_ServerRequest.DEVICE_PARAMETERS,
            T_ServerRequest.DROID_PARAMETERS,
            T_ServerRequest.MAP,
            T_ServerRequest.SHIP_PARAMETERS,
            T_ServerRequest.LOGGED,
            T_ServerRequest.PLAYER,
            T_ServerRequest.PLAYER_SHIP,
            T_ServerRequest.TO_GAME,
            T_ServerRequest.LOCATION_SYSTEM,
            T_ServerRequest.ACTIVE_WEAPONS,
            T_ServerRequest.ACTIVE_DEVICES,
            T_ServerRequest.CLAN,
            T_ServerRequest.SHIPS_POSITION,
            T_ServerRequest.SHIPS_STASE,
            T_ServerRequest.HIDE_SHIP,))

        Player.Pack += (
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.PlayerClanPoints},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.Bonuses},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.PlayerCash},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.ControlUsed},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.ControlLeft},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.HyperRadius},
            {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.HyperCost},
        )

    def authorisation_package(self, conn):
        print('authorisation_package')
        PackageNumberGet, lenBytes = self.__default_get_package(conn)
        data = conn.recv(lenBytes)
        login, password = PackagesReader.login(data)
        id_ = self.online #self.DB.get_user_id(login, password)
        if id_:
            self.connect_user(id_, conn)
            print('His id', id_)
            print('Логин', login)
            print('Пароль', password)
            Player = self.Game.create_player(id_, login + str(id_))
            return Player

    def connect_user(self, id_, conn):
        self.id_to_conn[id_] = conn
        self.conn_to_id[conn] = id_

    @staticmethod
    def __default_get_package(conn):
        decoder = PackageDecoder(conn.recv(8))
        return decoder.read_int(), decoder.read_int()

    def get_packages(self, conn, Player):
        while True:
            try:
                PackageNumberGet, lenBytes = self.__default_get_package(conn)
                data = conn.recv(lenBytes)
                threading.Thread(target=self.read_package, args=(PackageNumberGet, data, Player)).start()
            except Exception as e:
                self.exit_user(conn, Player.id)
                print(f'Пользователь с {self.conn_to_id[conn]} id вышел')
                exit()

    def exit_user(self, conn, id_):
        print('i want delete', conn, id_)
        exec(f"del self.Game.Player_{id_}")
        conn.close()

    def read_package(self, pack_number, data, Player):
        PackagesReader(self.Game, Player, pack_number, data)

    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)

    def __del__(self):
        import pickle
        with open("Server_Class", 'wb') as f:
            pickle.dump(self, f)

def main() -> None:
    test = Server()
    test.main()
