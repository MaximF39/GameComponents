from ..Config.CFG_Shop.cfg_upgrade_ship import cfg_upgrade
from ..Config.cfg_main import cfg_const, cfg_main, RADIUS_BETWEEN_PLANET
from ..Game.Items.Item import Item
from ..Game.Items.T_Item import T_Item
from ..Game.Utils.DotMap import DotMap
from ..Static.ParseJson import parse_xml, ship_CN
from .PackageCreator import PackageCreator
from ..Config.CFG_Shop.cfg_trading import cfg_trading
from ..Static.Type.Package.T_ServerRequest import T_ServerRequest


class PackagesManager:
    stateLoop: int

    def __init__(self, Player):
        self.Player = Player

    @staticmethod
    def isValidPackageLength(creator: int) -> bool:
        return 0 <= creator < 60000

    def processPackages(self, _loc1_: T_ServerRequest, *args):
        _loc2_: list = list()
        match _loc1_:
            case T_ServerRequest.SHIPS_POSITION:
                return self.shipsPosition()
            case T_ServerRequest.SHIPS_STASE:
                return self.shipsState()
            case T_ServerRequest.MESSAGE:
                return self.message()
            case T_ServerRequest.PLAYER_SHIP_UPDATE:
                return self.playerShipUpdate()
            case T_ServerRequest.PLANETS_STATE:
                return self.planetsState()
            case T_ServerRequest.PLANETS_UPDATE:
                return self.planetsUpdate()
            case T_ServerRequest.REPOSITORY:
                return self.repository()
            case T_ServerRequest.CLAN_REPOSITORY:
                return self.clan_repository()
            case T_ServerRequest.WEAPON_TROUBLES:
                return self.weaponTroubles()
            case T_ServerRequest.SHIP:
                return self.ship()
            case T_ServerRequest.SHOOTS:
                return self.shoots()
            case T_ServerRequest.ITEMS:
                return self.items()
            case T_ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices()
            case T_ServerRequest.ACTIVE_WEAPONS:
                return self.activeWeapons()
            case T_ServerRequest.HIDE_SHIP:
                return self.hideShip()
            case T_ServerRequest.SHIP_DESTROYED:
                return self.shipDestroyed()
            case T_ServerRequest.SHIP_JUMPED:
                return self.shipJumped()
            case T_ServerRequest.PLANET:
                return self.planet()
            case T_ServerRequest.INVENTORY:
                return self.inventory()
            case T_ServerRequest.TRADING_ITEMS:
                return self.tradingItems()
            case T_ServerRequest.RESOURCE_UPDATE_INFO:
                return self.resourceUpdate()
            case T_ServerRequest.ASTEROIDS:
                return self.asteroids()
            case T_ServerRequest.EFFECT_CREATED:
                return self.effectCreated()
            case T_ServerRequest.LOCATION_PLANET:
                return self.locationPlanet()
            case T_ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem()
            case T_ServerRequest.LOCATION_BATTLE:
                return self.locationBattle()
            case T_ServerRequest.PLAYER:
                return self.player()
            case T_ServerRequest.QUEST_MESSAGE:
                return self.questMessage()
            case T_ServerRequest.PLAYER_SKILLS:
                return self.playerSkills()
            case T_ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData()
            case T_ServerRequest.PLAYER_SHIP:
                return self.playerShip()
            case T_ServerRequest.DROID_BUILDING_DIALOG:
                return self.droidBuildingDialog()
            case T_ServerRequest.TRADING_SHIPS:
                return self.tradingShips()
            case T_ServerRequest.WEAPONS_PARAMETERS:
                return self.weaponsParameters()
            case T_ServerRequest.ENGINES_PARAMETERS:
                return self.engineParameters()
            case T_ServerRequest.AMMOS_PARAMETERS:
                return self.ammoParameters()
            case T_ServerRequest.RESOURCE_PARAMETERS:
                return self.resourceParameters()
            case T_ServerRequest.DEVICE_PARAMETERS:
                return self.deviceParameters()
            case T_ServerRequest.DROID_PARAMETERS:
                return self.droidParameters()
            case T_ServerRequest.SHIP_PARAMETERS:
                return self.shipParameters()
            case T_ServerRequest.LOGGED:
                return self.logged()
            case T_ServerRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems()
            case T_ServerRequest.SYSTEM_MESSAGE:
                return self.systemMessage()
            case T_ServerRequest.LOG_MESSAGE:
                return self.logMessage()
            case T_ServerRequest.LOG_MESSAGE_STRING:
                return self.logMessagestr()
            case T_ServerRequest.SYSTEM_MESSAGE_STRING:
                return self.systemMessagestr()
            case T_ServerRequest.MAP:
                return self.map()
            case T_ServerRequest.QUESTS_JOURNAL:
                return self.questsJournal()
            case T_ServerRequest.ARENA_REQUESTS:
                return self.arenaRequests()
            case T_ServerRequest.PLANET_QUESTS:
                return self.planetQuests()
            case T_ServerRequest.ADDITIONAL_QUEST_MESSAGE:
                return self.additionalQuestMessage()
            case T_ServerRequest.BATTLE_REQUEST_CHANGED:
                return self.battleRequestChanged()
            case T_ServerRequest.TOP_LIST:
                return self.topList()
            case T_ServerRequest.TOP_RATING_LIST:
                return self.topRatingList()
            case T_ServerRequest.TOP_CLANS_LIST:
                return self.topClansList()
            case T_ServerRequest.NEWS_LIST:
                return self.newsList()
            case T_ServerRequest.ONLINE:
                return self.online()
            case T_ServerRequest.VERSION:
                return self.version()
            case T_ServerRequest.SHIP_HEALTH:
                return self.shipHealth()
            case T_ServerRequest.NPC_MESSAGE:
                return self.npcMessage()
            case T_ServerRequest.UPDATE_HOLD:
                return self.updateHold()
            case T_ServerRequest.GINETIC_LAB_OPTIONS:
                return self.gineticLabOptions()
            case T_ServerRequest.CLAN:
                return self.clan()
            case T_ServerRequest.CHECK_VALUE_RESULT:
                return self.checkvalueResult()
            case T_ServerRequest.ACCEPTED_CLAN_INFO:
                return self.acceptedClanInfo()
            case T_ServerRequest.CLAN:
                return self.clan_id()
            case T_ServerRequest.CLANS_LETTERS:
                return self.clansLetters()
            case T_ServerRequest.CLANS_LIST:
                return self.clansList()
            case T_ServerRequest.CLAN_JOIN_REQUESTS:
                return self.clanJoinRequests()
            case T_ServerRequest.PLAYER_INFO:
                return self.playerInfo()
            case T_ServerRequest.PLAYER_LOGGED_ON:
                return self.playerLoggedOn()
            case T_ServerRequest.PLAYER_LOGGED_OFF:
                return self.playerLoggedOff()
            case T_ServerRequest.PLAYER_CLAN:
                return self.playerClan()
            case T_ServerRequest.FRIEND_CLANS:
                return self.friendClans()
            case T_ServerRequest.ENEMY_CLANS:
                return self.enemyClans()
            case T_ServerRequest.UPDATE_VALUE:
                return self.updatevalue(*args)
            case T_ServerRequest.FRIEND_REQUESTS:
                return self.friendRequests()
            case T_ServerRequest.DROID_EVENT:
                return self.droidEvent()
            case T_ServerRequest.EFFECT_REMOVED:
                return self.effectRemoved()
            case T_ServerRequest.MISSIONS:
                return self.missions()
            case T_ServerRequest.TO_GAME:
                return self.toGame()
            case T_ServerRequest.PLAYER_ANGAR:
                return self.playerAngar()
            case T_ServerRequest.TRADE_INVITATION:
                return self.tradeInvitation()
            case T_ServerRequest.SHOW_TRADING:
                return self.showTrading()
            case T_ServerRequest.TRADING_CASH:
                return self.tradingCash()
            case T_ServerRequest.TRADE_SELL_ITEMS:
                return self.tradeSellItems()
            case T_ServerRequest.EVIL:
                return self.Evil()
            case T_ServerRequest.TRADE_ACCEPTED:
                return self.tradeAccept()
            case T_ServerRequest.TRADE_BUY_ITEMS:
                return self.tradeBuyItems()
            case T_ServerRequest.FINISH_TRADING:
                return self.finishTrading()
            case T_ServerRequest.SHIP_UPDATE_INFO:
                return self.shipUpdateInfo()
            case T_ServerRequest.TEAM_LIST:
                return self.teamList()

    def tradingCash(self):
        creator = PackageCreator(T_ServerRequest.TRADING_CASH)
        creator.write_int(5)
        self.__send_pack(creator.get_package())

    def tradeAccept(self, accept:bool):
        creator = PackageCreator(T_ServerRequest.TRADE_ACCEPTED)
        creator.write_bool(accept)
        self.__send_pack(creator.get_package())

    def shipUpdateInfo(self):
        creator = PackageCreator(T_ServerRequest.SHIP_UPDATE_INFO)

        _loc6_ = DotMap(Item(T_Item.Ship_id, ship_CN(self.Player.class_number)).__dict__)
        creator.write_short(_loc6_.class_number)
        creator.write_short(_loc6_.size)
        creator.write_unsigned_byte(_loc6_.weapon_slots)
        creator.write_unsigned_byte(_loc6_.device_slots)
        creator.write_unsigned_byte(_loc6_.armor)
        creator.write_unsigned_byte(_loc6_.shields)
        creator.write_short(_loc6_.max_energy)
        creator.write_short(_loc6_.max_health)
        creator.write_short(_loc6_.cpu)
        creator.write_short(_loc6_.radar)
        creator.write_unsigned_byte(_loc6_.max_speed)
        rest = _loc6_.restrictions
        creator.write_unsigned_byte(len(rest))
        for r in rest:
            _loc2_ = DotMap(r)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.value_type)
            creator.write_int(_loc2_.value)

        feat = _loc6_.features
        creator.write_unsigned_byte(len(feat))
        for f in feat:
            _loc3_ = DotMap(f)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.value)

        _loc9_ = DotMap(Item(T_Item.Ship_id, cfg_upgrade[self.Player.class_number]).__dict__)

        creator.write_short(_loc9_.class_number)
        creator.write_short(_loc9_.size)
        creator.write_unsigned_byte(_loc9_.weapon_slots)
        creator.write_unsigned_byte(_loc9_.device_slots)
        creator.write_unsigned_byte(_loc9_.armor)
        creator.write_unsigned_byte(_loc9_.shields)
        creator.write_short(_loc9_.max_energy)
        creator.write_short(_loc9_.max_health)
        creator.write_short(_loc9_.cpu)
        creator.write_short(_loc9_.radar)
        creator.write_unsigned_byte(_loc9_.max_speed)
        rest = _loc9_.restrictions
        creator.write_unsigned_byte(len(rest))
        for i in rest:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.value_type)
            creator.write_int(_loc2_.value)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc3_ = DotMap(i)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.value)
        creator.write_bool(_loc9_.satisfying)

        UpdateCost = []
        _loc10_ = DotMap()
        creator.write_int(_loc10_.cash)
        for i in UpdateCost:
            _loc5_ = DotMap(i)
            creator.write_short(_loc5_.class_number)
            creator.write_int(_loc5_.count)
            creator.write_bool(_loc5_.enough)
        self.__send_pack(creator.get_package())

    def finishTrading(self):
        creator = PackageCreator(T_ServerRequest.FINISH_TRADING)
        _loc2_ = 0
        creator.write_int(_loc2_)
        self._write_items(creator, True, False, False)
        _loc4_: int = 0
        creator.write_int(_loc4_)
        self._write_items(creator, True, False, False)
        self.__send_pack(creator.get_package())

    def tradeSellItems(self):
        creator = PackageCreator(T_ServerRequest.TRADE_SELL_ITEMS)
        self._write_items(creator, True, True)
        self.__send_pack(creator.get_package())

    def tradeBuyItems(self):
        creator = PackageCreator(T_ServerRequest.TRADE_BUY_ITEMS)
        self._write_items(creator, True, True)
        self.__send_pack(creator.get_package())

    def playerAngar(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_ANGAR)
        angar = self.Player.angar
        creator.write_unsigned_byte(len(angar))
        for FakeShip in angar:
            ship = DotMap(FakeShip.ship)
            creator.write_short(ship.class_number)
            creator.write_int(ship.cost)
            creator.write_short(ship.maxHold)
            creator.write_unsigned_byte(ship.weapon_slots)
            creator.write_unsigned_byte(ship.device_slots)
            creator.write_unsigned_byte(ship.armor) # до 127 броня. 128 == - 128. if armor > 127: armor = 256 - armor
            creator.write_unsigned_byte(ship.shields)
            creator.write_short(ship.max_energy)
            creator.write_short(ship.max_health)
            creator.write_short(ship.cpu)
            creator.write_short(ship.radar)
            creator.write_unsigned_byte(ship.max_speed)
            data_restr = ship.restrictions
            creator.write_unsigned_byte(len(data_restr))
            for rest in data_restr:
                _loc4_ = DotMap(rest)
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.value_type)
                creator.write_int(_loc4_.value)
            data_feat = ship.features
            creator.write_unsigned_byte(len(data_feat))
            for feat in data_feat:
                _loc5_ = DotMap(feat)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.value)
            creator.write_bool(ship.satisfying)
        self.__send_pack(creator.get_package())

    def updateHold(self):
        return
        creator = PackageCreator(T_ServerRequest.UPDATE_HOLD)
        update_hold = bool()
        creator.write_bool(update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self.__send_pack(creator.get_package())

    def gineticLabOptions(self):
        creator = PackageCreator(T_ServerRequest.GINETIC_LAB_OPTIONS)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.option)
            creator.write_int(_loc2_.cost)
        self.__send_pack(creator.get_package())

    def npcMessage(self, text=4, avatar=2001):
        creator = PackageCreator(T_ServerRequest.NPC_MESSAGE)
        creator.write_int(text)  # message SystemMessageType
        creator.write_int(avatar)  # avatar
        self.__send_pack(creator.get_package())

    def additionalQuestMessage(self):
        creator = PackageCreator(T_ServerRequest.ADDITIONAL_QUEST_MESSAGE)
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.__send_pack(creator.get_package())

    def arenaRequests(self):
        creator = PackageCreator(T_ServerRequest.ARENA_REQUESTS)
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.playersCount)
            creator.write_int(_loc2_.maxPlayers)
            creator.write_int(_loc2_.maxShipType)
            creator.write_int(_loc2_.minShipType)
            creator.write_unsigned_byte(_loc2_.type)
        self.__send_pack(creator.get_package())

    def battleRequestChanged(self):
        creator = PackageCreator(T_ServerRequest.BATTLE_REQUEST_CHANGED)
        _loc3_ = DotMap()
        creator.write_int(_loc3_.id)
        creator.write_int(_loc3_.playersCount)
        creator.write_int(_loc3_.maxPlayers)
        creator.write_int(_loc3_.maxShipType)
        creator.write_int(_loc3_.minShipType)
        creator.write_unsigned_byte(_loc3_.type)
        creator.write_int(_loc3_.award)
        _loc3_.cost = (_loc3_.type - 1) * 2000
        for i in _loc3_.playersCoun:
            _loc2_ = DotMap(i)
            creator.write_bool(_loc2_.isReady)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.shipClass)
            creator.write_int(_loc2_.race)
        self.__send_pack(creator.get_package())

    def questsJournal(self):
        creator = PackageCreator(T_ServerRequest.QUESTS_JOURNAL)
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.__send_pack(creator.get_package())

    def activeDevices(self):
        creator = PackageCreator(T_ServerRequest.ACTIVE_DEVICES)
        data_active_devices = self.Player.Ship.active_devices
        creator.write_unsigned_byte(len(data_active_devices))
        for active_device in data_active_devices:
            creator.write_short(active_device.class_number)
            creator.write_bytes(active_device.guid)
            creator.write_float(active_device.reloaded_time)
        self.__send_pack(creator.get_package())

    def activeWeapons(self):
        creator = PackageCreator(T_ServerRequest.ACTIVE_WEAPONS)
        activeWeapons = self.Player.Ship.active_weapons
        for index, active_weapon in enumerate(activeWeapons):
            creator.write_short(active_weapon.class_number)
            creator.write_unsigned_byte(index + 1) #active_weapon.index) # hz
        self.__send_pack(creator.get_package())
        
    def playerShipUpdate(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_SHIP_UPDATE)
        creator.write_short(self.Player.Ship.energy)
        creator.write_short(self.Player.Ship.health)
        creator.write_unsigned_byte(self.Player.controlLeft)
        creator.write_unsigned_byte(self.Player.controlUsed)
        self.__send_pack(creator.get_package())

    def tradingShips(self):
        creator = PackageCreator(T_ServerRequest.TRADING_SHIPS)

        data = self.Player.SpaceObject.ships

        creator.write_int(self.Player.class_number)#ship.id)  # id
        creator.write_int(self.Player.cost)#ship.cost)  # ship cost

        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_buy) #ship.buy_coef)  # buyCoeficient
        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_sell) #ship.sell_coef)  # sellCoeficient

        creator.write_int(len(data))

        for _loc6_ in data:
            creator.write_bytes(_loc6_.guid)
            creator.write_short(_loc6_.ship["class_number"])
            creator.write_int(_loc6_.ship["cost"])
            creator.write_short(_loc6_.ship["size"])
            creator.write_unsigned_byte(_loc6_.ship["weapon_slots"])
            creator.write_unsigned_byte(_loc6_.ship["device_slots"])
            creator.write_unsigned_byte(_loc6_.ship["armor"])
            creator.write_unsigned_byte(_loc6_.ship["shields"])
            creator.write_short(_loc6_.ship["max_energy"])
            creator.write_short(_loc6_.ship["max_health"])
            creator.write_short(_loc6_.ship["cpu"])
            creator.write_short(_loc6_.ship["radar"])
            creator.write_unsigned_byte(_loc6_.ship["max_speed"])
            data_restr = _loc6_.ship["restrictions"]
            creator.write_unsigned_byte(len(data_restr))
            for restr in data_restr:
                creator.write_unsigned_byte(restr['type'])
                creator.write_unsigned_byte(restr['value_type'])
                creator.write_int(restr['value'])
            data_ship_feature = _loc6_.ship["features"]
            creator.write_unsigned_byte(len(data_ship_feature))
            for feat in data_ship_feature:
                _loc5_ = DotMap(feat)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.value)

        self.__send_pack(creator.get_package())

    def tradingItems(self, shop_type=1):
        creator = PackageCreator(T_ServerRequest.TRADING_ITEMS)
        creator.write_int(shop_type) # type shop

        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_sell)  # sellCoeficient
        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_buy)  # buyCoeficient

        self._write_items(creator, self.Player.inventory, True, True, True, True)

        self.__send_pack(creator.get_package())

    def resourceUpdate(self):
        creator = PackageCreator(T_ServerRequest.RESOURCE_UPDATE_INFO)
        ss = 22
        creator.write_int(ss)  # id
        self._write_items(creator, True, True)
        self._write_items(creator, True, True)
        self.__send_pack(creator.get_package())

    def _write_items(self, creator:PackageCreator, items, param2: bool, param3: bool, param4: bool = True,
                     param5: bool = False) -> None:

        creator.write_int(len(items))
        for item in items:
            creator.write_int(item.class_number)
            creator.write_bytes(item.guid)
            creator.write_int(item.get_wear)
            if param4:
                creator.write_int(0) #item.level)
            if param2:
                creator.write_bool(False) # zeroCost
            if param5:
                creator.write_int(12)  # random don't use
                # raise NotImplementedError("What is it? ")
            if param3:
                creator.write_bool(item.satisfying)

    def shipsPosition(self):
        """ id, x, y, targetX, targetY """
        creator = PackageCreator(T_ServerRequest.SHIPS_POSITION)
        creator.write_int(self.Player.clicked)
        for player in self.Player.Location.players:
            creator.write_int(player.id)
            creator.write_float(player.Ship.V2D.x)
            creator.write_float(player.Ship.V2D.y)
            creator.write_float(player.Ship.T_V2D.x)
            creator.write_float(player.Ship.T_V2D.y)
        self.__send_pack(creator.get_package())

    def shipsState(self):
        creator = PackageCreator(T_ServerRequest.SHIPS_STASE)
        players = self.Player.Location.players
        for _loc2_ in players:
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.Ship.speed)
            creator.write_short(_loc2_.Ship.health)
            creator.write_short(_loc2_.Ship.energy)
            creator.write_short(_loc2_.PlayerRelation)
        self.__send_pack(creator.get_package())

    def weaponTroubles(self):
        creator = PackageCreator(T_ServerRequest.WEAPON_TROUBLES)
        data = []
        creator.write_unsigned_byte(len(data))
        for trouble in data:
            _loc2_ = DotMap(trouble)
            creator.write_unsigned_byte(_loc2_.trouble)
            creator.write_unsigned_byte(_loc2_.index)
        self.__send_pack(creator.get_package())

    def repository(self):
        creator = PackageCreator(T_ServerRequest.REPOSITORY)

        self._write_items(creator, self.Player.repository, False, False)

        creator.write_float(1.0)  # costCoef _loc4_.costCoef # проверить пакет хранилища
        creator.write_int(len(data))
        for _loc2_ in data:
            creator.write_int(_loc2_.class_number)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # random don't use
        self.__send_pack(creator.get_package())

    def clan_repository(self):
        creator = PackageCreator(T_ServerRequest.CLAN_REPOSITORY)
        items = self.Player.Сlan.repository
        self._write_items(creator, items, False, False)
        creator.write_float(1) #_loc4_.costCoef)
        creator.write_int(len(items))
        for i in items:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.class_number)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # don't use
        self.__send_pack(creator.get_package())

    def planetsState(self):
        creator = PackageCreator(T_ServerRequest.PLANETS_STATE)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)  # id SpaceObject
            creator.write_float(_loc1_.angel)  # angel
        self.__send_pack(creator.get_package())

    def planetsUpdate(self):
        creator = PackageCreator(T_ServerRequest.PLANETS_UPDATE)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)
            creator.write_float(_loc1_.angel)
            creator.write_bytes(_loc1_.race)
            creator.write_bytes(_loc1_.aliance)
            creator.write_int(_loc1_.clan_id)
        self.__send_pack(creator.get_package())

    def ship(self):
        creator = PackageCreator(T_ServerRequest.SHIP)
        creator.write_short(self.Player.race)
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_short(self.Player.Ship.maxHold)
        creator.write_float(self.Player.Ship.x)
        creator.write_float(self.Player.Ship.y)
        creator.write_int(self.Player.level)
        creator.write_short(self.Player.Ship.max_health)
        creator.write_short(self.Player.Ship.max_energy)
        creator.write_int(self.Player.avatar)
        creator.write_unsigned_byte(self.Player.Ship.max_speed)
        creator.write_float(self.Player.Ship.T_V2D.x)
        creator.write_float(self.Player.Ship.T_V2D.y)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_unsigned_byte(self.Player.status)
        creator.write_int(self.Player.clan_id)
        droids = self.Player.Ship.droids
        creator.write_unsigned_byte(len(droids))
        for droid in droids:
            _loc2_ = DotMap(droid)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_short(_loc2_.type)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
        self.__send_pack(creator.get_package())

    def planet(self):
        creator = PackageCreator(T_ServerRequest.PLANET)
        _loc2_ = DotMap()
        creator.write_bytes(_loc2_.class_number)
        creator.write_int(_loc2_.id)
        creator.write_unsigned_byte(_loc2_.race)
        creator.write_int(_loc2_.radius)
        creator.write_int(_loc2_.size)
        creator.write_float(_loc2_.serverAngle)
        creator.write_bool(_loc2_.landable(self.Player))
        self.__send_pack(creator.get_package())

    def inventory(self):
        creator = PackageCreator(T_ServerRequest.INVENTORY)
        inventory = self.Player.inventory
        _loc5_: int = creator.write_short(len(inventory))
        for _, ItemClass in inventory.items():
            creator.write_short(ItemClass.class_number)
            creator.write_bytes(ItemClass.guid)
            creator.write_short(ItemClass.wear)
            creator.write_bool(ItemClass.inUsing)
            creator.write_unsigned_byte(ItemClass.level)
            creator.write_bool(ItemClass.satisfying())
        creator.write_unsigned_byte(self.Player.Ship.armor)
        creator.write_unsigned_byte(self.Player.Ship.shields)
        creator.write_short(inventory.Hold) # Трюм
        creator.write_short(self.Player.Ship.cpu)
        creator.write_short(self.Player.Ship.cpu_used) # ship.cpu_used
        creator.write_unsigned_byte(self.Player.exp.level)
        creator.write_unsigned_byte(3) # ship.maxDroids

        # for i in data: # Какие-то дополнительные предметы
        #     _loc2_ = DotMap(i)
        #     creator.write_short(_loc2_.ItemClass)
        #     creator.write_bytes(_loc2_.id)
        self.__send_pack(creator.get_package())

    def player(self, mode=False):
        creator = PackageCreator(T_ServerRequest.PLAYER)

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.exp.level)
        creator.write_int(self.Player.cash)
        creator.write_unsigned_byte(self.Player.race)
        creator.write_int(self.Player.avatar)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_int(self.Player.clan_id)
        creator.write_int(self.Player.role)
        creator.write_unsigned_byte(self.Player.clanRequestStatus)
        creator.write_unsigned_byte(self.Player.clanJoinRequestStatus)
        creator.write_int(self.Player.PlayerRelation)
        self.__send_pack(creator.get_package())

    def questMessage(self):
        creator = PackageCreator(T_ServerRequest.QUEST_MESSAGE)
        quest = DotMap()
        creator.write_int(quest.questId)
        creator.write_int(quest.nextQuestId)
        creator.write_int(quest.giverType)
        creator.write_int(quest.status)
        creator.write_utf(quest.giverName)
        data = []
        creator.write_int(len(data))
        for i in data: # ? maybe messagee
            _loc2_ = ''
            creator.write_utf(_loc2_)
        creator.write_int(quest.ParentSystemID)
        creator.write_unsigned_byte(quest.LocationType)
        creator.write_int(quest.LocationID)
        quest_award = []
        creator.write_int(len(quest_award))
        for award in quest_award:
            _loc3_ = DotMap(award)
            creator.write_int(_loc3_.class_number)
            creator.write_int(_loc3_.level)
            creator.write_int(_loc3_.type)
            creator.write_int(_loc3_.value)
        quest_target = []
        creator.write_int(quest_target)
        for target in quest_target:
            _loc4_ = DotMap(target)
            creator.write_int(_loc4_.targetId)
            creator.write_int(_loc4_.targetSystemId)
            creator.write_int(_loc4_.targetPlanetId)
            creator.write_int(_loc4_.type)
            creator.write_int(_loc4_.value)
        self.__send_pack(creator.get_package())

    def playerSkills(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_SKILLS)
        Player = getattr(self.Player.Game, f"Player_{self.Player.id}")
        creator.write_unsigned_byte(Player.exp.level)
        creator.write_int(Player.exp)
        creator.write_int(Player.exp.next)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.skills['Free'])
        creator.write_int(1) #Player.expForFirstSkillLevel)
        creator.write_float(1)#Player.expSkillGrowCoef)
        creator.write_float(1)#Player.expSkillReduserCoef)
        creator.write_unsigned_byte(cfg_const['maxSkill'])
        creator.write_unsigned_byte(Player.status.level)
        creator.write_unsigned_byte(Player.exp.level)
        if Player.points > 0:
            creator.write_int(0)
            creator.write_int(Player.status)
        else:
            creator.write_int(Player.status)
            creator.write_int(0)
        creator.write_int(Player.status.next)
        self.__send_pack(creator.get_package())

    @staticmethod
    def write_skills(creator, param2) -> None:
        creator.write_unsigned_byte(param2["Control"])
        creator.write_unsigned_byte(param2["Defending"])
        creator.write_unsigned_byte(param2["EnergyWeapons"])
        creator.write_unsigned_byte(param2["KineticWeapons"])
        creator.write_unsigned_byte(param2["Mining"])
        creator.write_unsigned_byte(param2["Piloting"])
        creator.write_unsigned_byte(param2["Repairing"])
        creator.write_unsigned_byte(param2["RocketWeapons"])
        creator.write_unsigned_byte(param2["Trading"])
        creator.write_unsigned_byte(param2["Attacking"])
        creator.write_unsigned_byte(param2["Tactics"])
        creator.write_unsigned_byte(param2["Targeting"])
        creator.write_unsigned_byte(param2["Electronics"])
        creator.write_unsigned_byte(param2["Biocemistry"])
        creator.write_unsigned_byte(param2["Mechanics"])
        creator.write_unsigned_byte(param2["Cybernetics"])

    def playerSkillsData(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_SKILLS_DATA)
        Player = getattr(self.Player.Game, f"Player_{self.Player.id}")
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.experience)
        creator.write_int(Player.forNextLevel)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.freeSkills)
        creator.write_int(Player.expForFirstSkillLevel)
        creator.write_float(Player.expSkillGrowCoef)
        creator.write_float(Player.expSkillReduserCoef)
        creator.write_unsigned_byte(Player.maxSkill)
        creator.write_unsigned_byte(Player.status)
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.pirateStatus)
        creator.write_int(Player.policeStatus)
        self.__send_pack(creator.get_package())

    def playerShip(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_SHIP)

        creator.write_int(self.Player.Ship.class_number)
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.inventory.Hold.max)
        creator.write_int(self.Player.Ship.energy)
        creator.write_int(self.Player.Ship.max_energy)
        creator.write_float(self.Player.Ship.V2D.x)
        creator.write_float(self.Player.Ship.V2D.y)
        creator.write_int(self.Player.team)
        creator.write_unsigned_byte(self.Player.Ship.max_speed)
        creator.write_unsigned_byte(self.Player.Ship.weapon_slots)
        creator.write_unsigned_byte(self.Player.Ship.device_slots)
        creator.write_int(self.Player.Ship.max_health)
        creator.write_short(self.Player.Ship.radar)
        creator.write_short(self.Player.Ship.cpu)
        self.__send_pack(creator.get_package())


    def weaponsParameters(self):
        creator = PackageCreator(T_ServerRequest.WEAPONS_PARAMETERS)
        data_weapons = parse_xml("WeaponParameters")
        creator.write_int(len(data_weapons))
        for weapon in data_weapons:
            _loc2_ = DotMap(weapon)
            creator.write_int(_loc2_.class_number)
            creator.write_int(_loc2_.autoShots)
            creator.write_int(_loc2_.radius)
            creator.write_int(_loc2_.reload_time)
            creator.write_int(_loc2_.energy_cost)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_bool(_loc2_.needAmmo)
            creator.write_int(_loc2_.CN_ammo)
            creator.write_int(_loc2_.min_damage)
            creator.write_int(_loc2_.max_damage)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.effect)
            if _loc2_.class_number == 1000:
                creator.write_int(5000)
            else:
                creator.write_int(1000)
            restr = _loc2_.restrictions
            creator.write_unsigned_byte(len(restr))
            for rest in restr:
                _loc5_ = DotMap(rest)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.value_type)
                creator.write_int(_loc5_.value)
        self.__send_pack(creator.get_package())

    def ammoParameters(self):
        creator = PackageCreator(T_ServerRequest.AMMOS_PARAMETERS)
        data_ammo = parse_xml("AmmoParameters")
        creator.write_int(len(data_ammo))
        for ammo in data_ammo:
            _loc2_ = DotMap(ammo)  # AmmoParameters()
            creator.write_int(_loc2_.class_number)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_int(_loc2_.damage)
        self.__send_pack(creator.get_package())

    def resourceParameters(self):
        creator = PackageCreator(T_ServerRequest.RESOURCE_PARAMETERS)
        data_resourse = parse_xml('ResourseParameters')
        creator.write_int(len(data_resourse))
        for resourse in data_resourse:
            _loc2_ = DotMap(resourse)  # ResourceParameters()
            creator.write_int(_loc2_.class_number)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
        self.__send_pack(creator.get_package())

    def deviceParameters(self):
        creator = PackageCreator(T_ServerRequest.DEVICE_PARAMETERS)
        data_device = parse_xml("DeviceParameters")
        creator.write_int(len(data_device))
        for device in data_device:
            _loc4_ = DotMap(device)
            creator.write_int(_loc4_.class_number)
            creator.write_float(_loc4_.size)
            creator.write_int(_loc4_.cost)
            creator.write_int(_loc4_.energy_cost)
            creator.write_int(_loc4_.reload_time)
            if _loc4_.class_number == 1000:
                creator.write_int(5000)
            else:
                creator.write_int(1000)

            dev_eff = _loc4_.effects
            creator.write_unsigned_byte(len(dev_eff))
            for dev_eff in dev_eff:
                _loc3_ = DotMap(dev_eff)  # DeviceEffect()
                creator.write_unsigned_byte(_loc3_.target_type)
                creator.write_int(_loc3_.value)
                creator.write_int(_loc3_.effect_time)
                creator.write_unsigned_byte(_loc3_.effect_type)

            dev_restr = _loc4_.restrictions
            creator.write_unsigned_byte(len(dev_restr))
            for restr in dev_restr:
                _loc8_ = DotMap(restr)  # Restriction()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.value_type)
                creator.write_int(_loc8_.value)
        self.__send_pack(creator.get_package())

    def droidParameters(self):
        creator = PackageCreator(T_ServerRequest.DROID_PARAMETERS)
        
        data_droids = parse_xml("DroidParameters")
        creator.write_int(len(data_droids))
        
        for droid_param in data_droids:
            _loc2_ = DotMap(droid_param)  # DroidParameters()
            creator.write_short(_loc2_.class_number)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_unsigned_byte(_loc2_.energy_cost)
            creator.write_unsigned_byte(_loc2_.armor)

            creator.write_short(_loc2_.droid_type)
            creator.write_short(_loc2_.CN_weapon)
            creator.write_short(_loc2_.health)

            data_restr = _loc2_.restrictions
            creator.write_unsigned_byte(len(data_restr))
            for restr in data_restr:
                _loc5_ = DotMap(restr)  # Restriction()
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.value_type)
                creator.write_int(_loc5_.value)
        self.__send_pack(creator.get_package())

    def shipParameters(self):
        creator = PackageCreator(T_ServerRequest.SHIP_PARAMETERS)
        data_ship = parse_xml('ShipParameters')
        creator.write_int(len(data_ship))
        for ship in data_ship:
            _loc2_ = DotMap(ship)
            creator.write_short(_loc2_.class_number)
            creator.write_int(_loc2_.cost)
            creator.write_short(_loc2_.size)
            creator.write_unsigned_byte(_loc2_.weapon_slots)
            creator.write_unsigned_byte(_loc2_.device_slots)
            creator.write_unsigned_byte(_loc2_.armor)
            creator.write_unsigned_byte(_loc2_.shields)
            creator.write_short(_loc2_.max_energy)
            creator.write_short(_loc2_.max_health)
            creator.write_short(_loc2_.cpu)
            creator.write_short(_loc2_.radar)
            creator.write_unsigned_byte(_loc2_.max_speed)

            data_restr = _loc2_.restrictions
            creator.write_unsigned_byte(len(data_restr))
            for restr in data_restr:
                _loc7_ = DotMap(restr)
                creator.write_unsigned_byte(_loc7_.type)
                creator.write_unsigned_byte(_loc7_.value_type)
                creator.write_int(_loc7_.value)

            data_ship_feat = _loc2_.features
            creator.write_unsigned_byte(len(data_ship_feat))
            for ship_feat in data_ship_feat:
                _loc8_ = DotMap(ship_feat)
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_int(_loc8_.value)
        self.__send_pack(creator.get_package())

    def engineParameters(self):
        creator = PackageCreator(T_ServerRequest.ENGINES_PARAMETERS)
        data_engine = parse_xml("EngineParameters")
        creator.write_int(len(data_engine))
        for engine_ in data_engine:
            engine_ = DotMap(engine_)  # EngineParameters()
            creator.write_short(engine_.class_number)
            creator.write_float(engine_.size)
            creator.write_int(engine_.cost)
            creator.write_unsigned_byte(engine_.hyperjump_radius)
            creator.write_int(1000)
            creator.write_unsigned_byte(engine_.energy_cost)
        self.__send_pack(creator.get_package())

    def map(self):
        creator = PackageCreator(T_ServerRequest.MAP)
        data_system = parse_xml('GalaxyMap')
        creator.write_short(len(data_system))
        for system in data_system:
            _loc2_ = DotMap(system)  # ReachableSystem()
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.class_number)
            creator.write_short(_loc2_.map_x)
            creator.write_short(_loc2_.map_y)
            creator.write_unsigned_byte(_loc2_.sector)
            creator.write_unsigned_byte(_loc2_.lineTo)

            data_planet = _loc2_.planets
            creator.write_unsigned_byte(len(data_planet))
            for planet in data_planet:
                planet = DotMap(planet)  # PlanetData()
                creator.write_short(planet.id)
                creator.write_unsigned_byte(planet.race)
                creator.write_unsigned_byte(planet.class_number)
                creator.write_unsigned_byte(planet.aliance)

            data_space_objects = _loc2_.staticSpaceObjects
            creator.write_unsigned_byte(len(data_space_objects))

            for static_space_object in data_space_objects:
                static_space_object = DotMap(static_space_object)  # StaticObjectData()
                creator.write_unsigned_byte(static_space_object.type)
                creator.write_unsigned_byte(static_space_object.aliance)
                creator.write_unsigned_byte(static_space_object.race)

        self.__send_pack(creator.get_package())

    def reachableSystems(self):
        creator = PackageCreator(T_ServerRequest.REACHABLE_SYSTEMS)
        data_system = []
        creator.write_unsigned_byte(len(data_system))
        for system in data_system:
            _loc2_ = DotMap(system)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_bool(_loc2_.current)
            creator.write_short(_loc2_.energyForJump)
        _loc6_: int = 0
        creator.write_unsigned_byte(_loc6_)  # radiuse
        _loc7_: int = 0
        creator.write_unsigned_byte(_loc7_)  # sector
        self.__send_pack(creator.get_package())

    def version(self):
        creator = PackageCreator(T_ServerRequest.VERSION)
        version = cfg_main['version']
        creator.write_utf(version)
        self.__send_pack(creator.get_package())

    def shipHealth(self):
        creator = PackageCreator(T_ServerRequest.SHIP_HEALTH)
        ship = getattr(self.Player.Game, f'Player_{self.Player.id}').ship
        creator.write_int(ship.id)
        creator.write_int(ship.health)
        self.__send_pack(creator.get_package())

    def online(self):
        creator = PackageCreator(T_ServerRequest.ONLINE)
        creator.write_int(1)
        creator.write_int(self.Player.Game.Server.online)
        self.__send_pack(creator.get_package())

    def topList(self):
        creator = PackageCreator(T_ServerRequest.TOP_LIST)
        all_player = []#top_list()
        creator.write_int(len(all_player))
        for player in all_player:
            creator.write_utf(player['login'])
            creator.write_int(player['level'])
            creator.write_int(player['experience'])
            creator.write_int(player['clan_id'])
            creator.write_unsigned_byte(player['race'])
            creator.write_short(player['shipClass'])
        self.__send_pack(creator.get_package())

    def topRatingList(self):
        creator = PackageCreator(T_ServerRequest.TOP_RATING_LIST)
        top_players = []#top_rating_list()
        creator.write_int(len(top_players))
        for player in top_players:
            creator.write_utf(player['login'])
            creator.write_int(player['level'])
            creator.write_int(player['points'])
            creator.write_int(player['clan_id'])
            creator.write_unsigned_byte(player['race'])
            creator.write_short(player['shipClass'])
        self.__send_pack(creator.get_package())

    def topClansList(self):
        creator = PackageCreator(T_ServerRequest.TOP_CLANS_LIST)
        clans = []#top_clan_list()
        for clan in clans:
            creator.write_int(clan['id'])
            creator.write_int(clan['rating'])
            creator.write_int(clan['leaderId'])
            creator.write_unsigned_byte(clan['aliance'])
            creator.write_unsigned_byte(clan['level'])
            creator.write_utf(clan['name'])
            creator.write_utf(clan['shortName'])
            creator.write_utf(clan['logoFileName'])
        self.__send_pack(creator.get_package())

        #
        # def auctionList(self):
        #     creator = PackageCreator(T_ServerRequest.AUCTION_SHOP_PACKAGE)
        # PacStr = T_ServerRequestStr(
        #     data = []
        #     creator.write_int(len(data))
        #     for i in data:
        #         _loc3_ = DotMap(i)
        #         creator.write_int(_loc2_.ItemClass)
        #         creator.write_guid(_loc3_.guid)
        #         creator.write_int(_loc3_.wear)
        #         creator.write_int(_loc3_.ownerid)
        #         creator.write_int(_loc3_.price)
        #         creator.write_int(_loc3_.ransom)
        #         creator.write_int(_loc3_.lastPlayerID)
        #         creator.write_utf(_loc3_.ownerName)
        #         creator.write_utf(_loc3_.lastPlayerName)
        #     self.__send_pack(creator.get_package())

    def newsList(self):
        creator = PackageCreator(T_ServerRequest.NEWS_LIST)
        data = []
        creator.write_int(len(data))
        for text in data:
            creator.write_utf(text)  # text
        self.__send_pack(creator.get_package())

    def Evil(self):
        creator = PackageCreator(T_ServerRequest.EVIL)
        _loc2_ = ''
        creator.write_utf(_loc2_)
        self.__send_pack(creator.get_package())

    def locationPlanet(self):
        creator = PackageCreator(T_ServerRequest.LOCATION_PLANET)

        SpaceObject = self.Player.SpaceObject

        creator.write_unsigned_byte(SpaceObject.class_number)
        creator.write_int(SpaceObject.id)
        creator.write_unsigned_byte(SpaceObject.race)
        creator.write_int(SpaceObject.Radius)
        creator.write_int(SpaceObject.size)
        creator.write_unsigned_byte(SpaceObject.aliance)
        creator.write_int(SpaceObject.clan_id)
        creator.write_float(SpaceObject.angle)
        creator.write_unsigned_byte(0)#SpaceObject.QCount)
        shops = []#SpaceObject.shops
        creator.write_short(len(shops)) # len(shop_data))

        for type_shop in shops:
            creator.write_int(type_shop) #SpaceObject.id) #_loc3_.id)
            creator.write_unsigned_byte(type_shop)#_loc3_.type)

        player_info_data = []
        for player in player_info_data:
            _loc2_ = DotMap(player)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.name)
            creator.write_int(_loc2_.clan_id)
            creator.write_int(_loc2_.level)

        self.__send_pack(creator.get_package())

    def planetQuests(self):
        creator = PackageCreator(T_ServerRequest.PLANET_QUESTS)
        data = []
        creator.write_short(len(data))
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.__send_pack(creator.get_package())

    def locationSystem(self):
        creator = PackageCreator(T_ServerRequest.LOCATION_SYSTEM)
        creator.write_int(self.Player.Location.id) # id
        creator.write_float(self.Player.Location.map_x)  # self.Location.x
        creator.write_float(self.Player.Location.map_y)  # self.Location.y
        creator.write_unsigned_byte(self.Player.Location.sector)  # self.Location.sector
        creator.write_short(len(self.Player.Location.players))
        for Player in self.Player.Location.players:
            creator.write_short(Player.race) #
            creator.write_int(Player.id)
            creator.write_utf(Player.login)
            creator.write_short(Player.inventory.Hold.max)
            creator.write_float(Player.Ship.V2D.x)  # setPosition
            creator.write_float(Player.Ship.V2D.y)
            creator.write_int(Player.exp.level)
            creator.write_short(Player.Ship.health)
            creator.write_short(Player.Ship.energy)
            creator.write_int(Player.avatar)
            creator.write_unsigned_byte(int(Player.Ship.speed))
            creator.write_float(Player.Ship.T_V2D.x)
            creator.write_float(Player.Ship.T_V2D.y)  # setMovePoint
            creator.write_unsigned_byte(Player.aliance)
            creator.write_unsigned_byte(Player.status)
            creator.write_int(Player.clan_id)
            creator.write_unsigned_byte(len(Player.Ship.droids))

            for Driod in Player.Ship.droids:
                creator.write_unsigned_byte(Driod.id)
                creator.write_short(Driod.type)
                creator.write_short(Driod.weaponClass)
                creator.write_short(Driod.health)

        creator.write_short(len(self.Player.Location.Planets))
        for planet in self.Player.Location.Planets:
            creator.write_unsigned_byte(planet.class_number)
            creator.write_int(planet.id)
            creator.write_unsigned_byte(planet.race)
            creator.write_int(planet.Radius)
            creator.write_int(planet.size)
            creator.write_float(planet.angle)
            creator.write_bool(planet.landable(self.Player))
            creator.write_unsigned_byte(planet.aliance)
            creator.write_int(planet.clan_id)

        creator.write_short(len(self.Player.Location.StaticSpaceObjects))
        for StaticSpaceObject in self.Player.Location.StaticSpaceObjects:
            creator.write_int(StaticSpaceObject.type)
            creator.write_int(StaticSpaceObject.id)
            creator.write_float(StaticSpaceObject.V2D.x)
            creator.write_float(StaticSpaceObject.V2D.y)
            creator.write_bool(StaticSpaceObject.landable(self.Player))
        self.__send_pack(creator.get_package())

    def locationBattle(self):
        creator = PackageCreator(T_ServerRequest.LOCATION_BATTLE)
        creator.write_int(self.Player.id)
        creator.write_float(self.Player.Ship.V2D.x)
        creator.write_float(self.Player.Ship.V2D.y)
        players = self.Player.Location.players
        creator.write_short(len(players))
        for player in players:
            creator.write_short(player.Ship.class_number)
            creator.write_int(player.id)
            creator.write_utf(player.login)
            creator.write_short(player.Ship.size)
            creator.write_float(player.Ship.V2D.x)
            creator.write_float(player.Ship.V2D.y)
            creator.write_int(player.exp.level) # hz
            creator.write_short(player.Ship.max_health)
            creator.write_short(player.Ship.max_energy)
            creator.write_int(player.avatar) # hz
            creator.write_unsigned_byte(player.aliance)
            creator.write_unsigned_byte(player.status)
            creator.write_int(player.clan_id)
            droids = player.droids
            creator.write_unsigned_byte(len(droids))
            for _loc4_ in droids:
                creator.write_unsigned_byte(_loc4_.guid)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)
        self.__send_pack(creator.get_package())

    def shoots(self):
        creator = PackageCreator(T_ServerRequest.SHOOTS)
        data = [
            {
            'id': self.Player.id,
            'shoot':[{
              'class_number': 110,
                "damage": 1000,
                "destroyedTarget": 2,
                "targetId": self.Player.id,
                "target_type": 1,
                "muzzleIndex": 1
            }]
            },
        ]

        creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_short(len(_loc2_.shoot))
            for shoot in _loc2_.shoot:
                _loc5_ = DotMap(shoot)
                creator.write_short(_loc5_.class_number)
                creator.write_short(_loc5_.damage)
                creator.write_unsigned_byte(_loc5_.destroyedTarget)
                creator.write_int(_loc5_.targetId)
                creator.write_unsigned_byte(_loc5_.target_type)
                creator.write_unsigned_byte(_loc5_.muzzleIndex)
        self.__send_pack(creator.get_package())

    def items(self):
        creator = PackageCreator(T_ServerRequest.ITEMS)
        data = self.Player.Location.inventory
        for item_ in data:
            creator.write_int(self.Player.Location.id)
            creator.write_short(item_.class_number)
            creator.write_short(int(item_.x))
            creator.write_short(int(item_.y))
        self.__send_pack(creator.get_package())

    def message(self, data_message:dict):
        creator = PackageCreator(T_ServerRequest.MESSAGE)
        _loc2_ = DotMap({
            "from_player": 'Max223',
            "text": "Hello",
            "type": 1,
            "isPrivate": False,
            "isAdmin": False,
        })
        _loc2_ = DotMap(data_message)
        creator.write_utf(_loc2_.from_player)  # name player
        creator.write_utf(_loc2_.text)
        creator.write_unsigned_byte(_loc2_.type)  # 1 - global  2 - local 3 - clan_id 4 - trade 5 - client chat
        creator.write_bool(_loc2_.isPrivate)
        creator.write_bool(_loc2_.isAdmin)
        self.__send_pack(creator.get_package())

    def asteroids(self):
        creator = PackageCreator(T_ServerRequest.ASTEROIDS)
        for asteroid in self.Player.Location.asteroids:
            creator.write_int(asteroid.id)
            creator.write_float(asteroid.V2D.x)
            creator.write_float(asteroid.V2D.y)
            creator.write_float(asteroid.T_V2D.x)
            creator.write_float(asteroid.T_V2D.y)
            creator.write_unsigned_byte(asteroid.speed)
            creator.write_int(asteroid.health)
        self.__send_pack(creator.get_package())

    def effectCreated(self, effect_type):
        creator = PackageCreator(T_ServerRequest.EFFECT_CREATED)
        creator.write_int(self.Player.id)
        effects = self.Player.effects
        creator.write_unsigned_byte(len(effects))
        for effect in effects:
            creator.write_int(effect.targetId)# time 255)# _loc2_.targetId)
            creator.write_unsigned_byte(2) #_loc2_.destroyedTarget)
            creator.write_bool(False)# Мб энергон _loc2_.effectFailed)
        creator.write_unsigned_byte(effect_type)  # EffectType
        _loc8_: float = 20.0
        creator.write_float(_loc8_)  # don't use
        _loc9_: int = 200
        creator.write_int(_loc9_)  # damage damageToShow
        self.__send_pack(creator.get_package())

    def effectRemoved(self, effect_type):
        creator = PackageCreator(T_ServerRequest.EFFECT_REMOVED)
        creator.write_int(self.Player.id)
        creator.write_unsigned_byte(effect_type)
        self.__send_pack(creator.get_package())

    def logMessage(self):
        creator = PackageCreator(T_ServerRequest.LOG_MESSAGE)
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.__send_pack(creator.get_package())

    def logMessagestr(self):
        creator = PackageCreator(T_ServerRequest.LOG_MESSAGE_STRING)
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.__send_pack(creator.get_package())

    def systemMessage(self):
        creator = PackageCreator(T_ServerRequest.SYSTEM_MESSAGE)
        _loc2_ = 6
        _loc3_ = 5
        creator.write_int(_loc2_)  # SystemMessageType
        creator.write_int(_loc3_)  # hz
        self.__send_pack(creator.get_package())

    def systemMessagestr(self):
        creator = PackageCreator(T_ServerRequest.SYSTEM_MESSAGE_STRING)
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.__send_pack(creator.get_package())

    def droidBuildingDialog(self, droid):
        creator = PackageCreator(T_ServerRequest.DROID_BUILDING_DIALOG)
        creator.write_bytes(droid.guid)# hz _loc3_.deviceGuid)
        creator.write_int(1)#len(self.Owner.droids))#len(data))
        # for droid in self.Owner.droids:
        creator.write_bytes(droid.guid)
        creator.write_int(droid.class_number)
        creator.write_int(droid.level)
        creator.write_int(droid.energy_cost)
        self.__send_pack(creator.get_package())

    def hideShip(self):
        creator = PackageCreator(T_ServerRequest.HIDE_SHIP)
        creator.write_int(-13)
        self.__send_pack(creator.get_package())

    def shipDestroyed(self):
        creator = PackageCreator(T_ServerRequest.SHIP_DESTROYED)
        ship_destroyed = DotMap()
        creator.write_int(ship_destroyed.id)
        self.__send_pack(creator.get_package())

    def shipJumped(self):
        creator = PackageCreator(T_ServerRequest.SHIP_JUMPED)
        location = DotMap()
        creator.write_int(location.id)  # findShip
        self.__send_pack(creator.get_package())

    def clan(self):
        creator = PackageCreator(T_ServerRequest.CLAN)
        data = []#top_clan_list()
        for clan in data:
            clan = DotMap(clan)
            creator.write_int(clan.id)
            creator.write_int(clan.leaderId)
            creator.write_utf(clan.leaderName)
            creator.write_utf(clan.logoFileName)
            creator.write_utf(clan.name)
            creator.write_utf(clan.shortName)
            creator.write_unsigned_byte(clan.aliance)
        self.__send_pack(creator.get_package())
    
    def __send_pack(self, pack):
        self.Player.Game.Server.id_to_conn[self.Player.id].send(pack)
    
    def playerClan(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_CLAN)
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        creator.write_int(_loc5_.leaderID)
        creator.write_utf(_loc5_.leaderName)
        creator.write_utf(_loc5_.logoFileName)
        creator.write_utf(_loc5_.name)
        creator.write_utf(_loc5_.shortName)
        creator.write_unsigned_byte(_loc5_.aliace)
        creator.write_utf(_loc5_.description)
        creator.write_short(_loc5_.joinRequestsCount)
        creator.write_int(_loc5_.points)
        creator.write_int(_loc5_.cash)
        creator.write_unsigned_byte(_loc5_.level)
        creator.write_unsigned_byte(_loc5_.maxMembers)
        creator.write_unsigned_byte(_loc5_.maxFriends)
        creator.write_short(_loc5_.friendRequests)
        creator.write_int(_loc5_.currentLevelPoints)
        creator.write_int(_loc5_.nextLevelPoints)
        creator.write_int(_loc5_.nextLevelCash)
        creator.write_int(_loc5_.bonuses)
        # cnt = _loc2_
        data2 = self.Player.Clan
        creator.write_int(len(data2))
        for enemy in data2:
            creator.write_int(enemy) # _loc5_.enemyClans)
        data2 = []
        creator.write_int(len(data2))
        for friend in data2:
            creator.write_int(friend)#_loc5_.friendClans)
        data2 = []
        creator.write_int(len(data2))
        for member in data2:
            member = DotMap(member)
            creator.write_int(member.id)
            creator.write_int(member.role)
            creator.write_utf(member.name)
        self.__send_pack(creator.get_package())

    def teamList(self):
        creator = PackageCreator(T_ServerRequest.TEAM_LIST)
        _loc4_ = None  # : PlayerInfoData
        data = []
        cnt_player_team = len(data)  #
        creator.write_int(cnt_player_team)
        if cnt_player_team > 0:
            Player = DotMap()
            Player.team = DotMap()
            creator.write_int(Player.team.leaderID)
            creator.write_int(Player.team.maxMembers)
            for team in data:
                team = DotMap(team)
                creator.write_int(team.shipId)
                creator.write_int(team.id)
                creator.write_utf(team.name)
        data = []
        creator.write_int(len(data))
        for team in data:
            player = DotMap(team)
            creator.write_int(player.ShipId)
            creator.write_int(player.id)
            creator.write_utf(player.name)
        self.__send_pack(creator.get_package())

    def checkvalueResult(self):
        creator = PackageCreator(T_ServerRequest.CHECK_VALUE_RESULT)
        _loc2_ = 5
        _loc3_ = True
        creator.write_int(_loc2_)
        creator.write_bool(_loc3_)
        self.__send_pack(creator.get_package())

    def acceptedClanInfo(self):
        creator = PackageCreator(T_ServerRequest.ACCEPTED_CLAN_INFO)
        _loc2_: int = 0
        _loc3_: str = ''
        _loc4_: str = ''
        _loc5_: str = ''
        _loc6_: int = 0
        creator.write_int(_loc2_)
        creator.write_utf(_loc3_)
        creator.write_utf(_loc4_)
        creator.write_utf(_loc5_)
        creator.write_int(_loc6_)
        self.__send_pack(creator.get_package())

    def clan_id(self):
        creator = PackageCreator(T_ServerRequest.clan_id)
        player = DotMap()
        creator.write_int(player.clan_id)
        self.__send_pack(creator.get_package())

    def clansLetters(self):
        creator = PackageCreator(T_ServerRequest.CLANS_LETTERS)
        data = []
        for clan in data:
            creator.write_utf(clan)
        self.__send_pack(creator.get_package())

    def clansList(self):
        creator = PackageCreator(T_ServerRequest.CLANS_LIST)
        data = []
        _loc3_ = self.Player.clan
        creator.write_utf(_loc3_)
        for clan in data:
            creator.write_int(clan)
        self.__send_pack(creator.get_package())

    def clanJoinRequests(self):
        creator = PackageCreator(T_ServerRequest.CLAN_JOIN_REQUESTS)
        data = []
        for jounRequest in data:
            player = DotMap(jounRequest)
            creator.write_int(player.playerID)
            creator.write_utf(player.playerName)
            creator.write_utf(player.message)
        self.__send_pack(creator.get_package())

    def logged(self):
        creator = PackageCreator(T_ServerRequest.LOGGED)

        creator.write_int(cfg_const['stateLoop'])
        creator.write_unsigned_byte(cfg_const['bankSendOperationFee'])
        creator.write_int(cfg_const['clanJoinCost'])
        creator.write_unsigned_byte(cfg_const['clanCreateLevelNeed'])
        creator.write_int(cfg_const['bonuses'])

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_short(self.Player.Ship.class_number)  #
        creator.write_short(self.Player.Ship.cpu)
        creator.write_unsigned_byte(self.Player.race)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_unsigned_byte(self.Player.status.level)
        creator.write_unsigned_byte(self.Player.exp.level)
        creator.write_int(self.Player.clan_id)
        creator.write_bool(self.Player.delete_enqueued)
        creator.write_bool(self.Player.can_delete)
        creator.write_bool(True)
        self.write_skills(creator, self.Player.skills)
        self.__send_pack(creator.get_package())

    def playerInfo(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_INFO)
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.name)
        creator.write_unsigned_byte(self.Player.level)
        creator.write_unsigned_byte(self.Player.status)
        creator.write_short(self.Player.class_number)
        creator.write_int(self.Player.clan_id)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_unsigned_byte(self.Player.race)
        creator.write_int(self.Player.points)
        creator.write_int(self.Player.role)
        self.__send_pack(creator.get_package())

    def playerLoggedOn(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_LOGGED_ON)
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.name)
        creator.write_int(self.Player.clan_id)
        creator.write_int(self.Player.level)
        self.__send_pack(creator.get_package())

    def playerLoggedOff(self):
        creator = PackageCreator(T_ServerRequest.PLAYER_LOGGED_OFF)
        creator.write_int(self.Player.id)
        self.__send_pack(creator.get_package())

    def friendClans(self):
        creator = PackageCreator(T_ServerRequest.FRIEND_CLANS)
        data = []
        for friend in data:
            ClanData = DotMap(friend)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.__send_pack(creator.get_package())

    def enemyClans(self):
        creator = PackageCreator(T_ServerRequest.ENEMY_CLANS)
        data = []
        for enemy in data:
            ClanData = DotMap(enemy)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.__send_pack(creator.get_package())

    def friendRequests(self):
        creator = PackageCreator(T_ServerRequest.FRIEND_REQUESTS)
        data = []
        for friend in data:  # clan_id Data
            friendRequests = DotMap(friend)
            creator.write_int(friendRequests.id)
            creator.write_int(friendRequests.leaderID)
            creator.write_utf(friendRequests.leaderName)
            creator.write_utf(friendRequests.logoFileName)
            creator.write_utf(friendRequests.name)
            creator.write_utf(friendRequests.shortName)
            creator.write_unsigned_byte(friendRequests.aliace)
        self.__send_pack(creator.get_package())

    def droidEvent(self):
        creator = PackageCreator(T_ServerRequest.DROID_EVENT)
        _loc2_ = DotMap()
        _loc3_ = 5
        _loc4_ = 5
        creator.write_unsigned_byte(_loc2_.id)
        creator.write_short(_loc2_.type)
        creator.write_short(_loc2_.weaponClass)
        creator.write_int(_loc3_)
        creator.write_unsigned_byte(_loc4_)
        self.__send_pack(creator.get_package())

    def updatevalue(self, num_pack, value=0):
        creator = PackageCreator(T_ServerRequest.UPDATE_VALUE)
        creator.write_unsigned_byte(num_pack)
        match num_pack:
            case 1:
                value = self.Player.Clan.cash #clan Cash
            case 2:
                value = clanPoints
            case 3:
                value = self.Player.points # Owner.point
            case 4:
                value = ClanFriendRequests
            case 5:
                value = ClanLevel
            case 6:
                value = ClanNextLevelPoints
            case 7:
                value = ClanMaxMembers
            case 8:
                value = ClanJoinRequestStatus
            case 9:
                value = self.Player.cash
            case 10:
                value = self.Player.ControlUsed
            case 11:
                value = self.Player.ControlLeft
            case 12:
                value = self.Player.clan_id
            case 13:
                value = self.Player.bonus
            case 14:
                value = 20#self.Owner.HyperRadius
            case 15:
                value = 20#self.Owner.HyperCost
            case 16:
                value = self.Player.ClanLeader
            case 17:
                value = self.Player.ClanBonuses
        creator.write_int(value)
        self.__send_pack(creator.get_package())
        
    def missions(self):
        creator = PackageCreator(T_ServerRequest.MISSIONS)
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        _loc5_.current = True
        _loc6_ = 6
        _loc7_ = 7
        creator.write_unsigned_byte(_loc6_)
        creator.write_unsigned_byte(_loc7_)
        data_reachable_system = []
        creator.write_unsigned_byte(len(data_reachable_system))
        for system in data_reachable_system:
            system = DotMap(system)
            creator.write_int(system.id)
        data = []  # PlanetData
        for planet in data:
            planet = DotMap(planet)
            creator.write_int(planet.id)
            creator.write_bytes(planet.class_number)
            creator.write_unsigned_byte(planet.aliance)
            creator.write_unsigned_byte(planet.race)
            creator.write_int(planet.starId)
        self.__send_pack(creator.get_package())

    def tradeInvitation(self):
        creator = PackageCreator(T_ServerRequest.TRADE_INVITATION)
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self.__send_pack(creator.get_package())

    def showTrading(self):
        creator = PackageCreator(T_ServerRequest.SHOW_TRADING)
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        _loc5_: list = []
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self._write_items(creator, True, True)
        self.__send_pack(creator.get_package())

    def toGame(self):
        creator = PackageCreator(T_ServerRequest.TO_GAME)
        self.__send_pack(creator.get_package())
