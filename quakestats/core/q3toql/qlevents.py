from copy import (
    deepcopy,
)

from quakestats.core.q3toql import (
    entities,
)


class QLEvent(dict):
    name = None
    payload = {}

    def __init__(self, time: int, match_guid: str, warmup: bool = False):
        self['TYPE'] = self.name
        self['DATA'] = {
            'TIME': time,
            'WARMUP': warmup,
            'MATCH_GUID': match_guid,
        }
        self['DATA'].update(deepcopy(self.payload))

    def update_payload(self, data: dict):
        self["DATA"].update(data)

    @property
    def data(self) -> dict:
        return self['DATA']

    @property
    def type(self) -> str:
        return self['TYPE']


class MatchStarted(QLEvent):
    name = "MATCH_STARTED"
    payload = {
        "INSTAGIB": 0,
        "FACTORY": "quake3",
        "FACTORY_TITLE": "quake3",
        "INFECTED": 0,
        "TIME_LIMIT": 0,
        "TRAINING": 0,
        "FRAG_LIMIT": 0,
        "CAPTURE_LIMIT": 0,
        "SERVER_TITLE": None,
        "GAME_TYPE": None,
        "QUADHOG": 0,
        "ROUND_LIMIT": 0,
        "MERCY_LIMIT": 0,
        "SCORE_LIMIT": 0,
        "MAP": None,
        "PLAYERS": {}  # I think we can live without it
    }

    def set_limits(self, fraglimit: int, timelimit: int, capturelimit: int):
        self.data['FRAG_LIMIT'] = fraglimit
        self.data['TIME_LIMIT'] = timelimit
        self.data['CAPTURE_LIMIT'] = capturelimit

    def set_game_info(self, server_title: str, map_name: str, game_type: str):
        # other modes are not yet supported
        assert game_type in ['FFA', 'CA', 'DUEL']
        self.data['SERVER_TITLE'] = server_title
        self.data['GAME_TYPE'] = game_type
        self.data['MAP'] = map_name


class PlayerConnect(QLEvent):
    name = "PLAYER_CONNECT"
    payload = {
        'NAME': None,
        'STEAM_ID': None,
    }

    def set_data(self, name: str, steam_id):
        self.data['NAME'] = name
        self.data['STEAM_ID'] = steam_id


class PlayerSwitchteam(QLEvent):
    name = 'PLAYER_SWITCHTEAM'
    payload = {
        'KILLER': {
            "STEAM_ID": None,
            "OLD_TEAM": None,
            "TEAM": None,
            "NAME": None,
        }
    }

    def set_data(
        self, steam_id, player_name: str, team_name: str, old_team_name: str
    ):
        inner = self.data['KILLER']
        inner['STEAM_ID'] = steam_id
        inner['NAME'] = player_name
        inner['TEAM'] = team_name
        inner['OLD_TEAM'] = old_team_name

    @property
    def steam_id(self):
        return self.data['KILLER']['STEAM_ID']

    @steam_id.setter
    def steam_id(self, val: str):
        self.data['KILLER']['STEAM_ID'] = val


class PlayerStats(QLEvent):
    name = "PLAYER_STATS"
    payload = {
        "TIED_TEAM_RANK": None,
        "QUIT": None,
        "WEAPONS": {},
        "MODEL": None,
        "PICKUPS": {},
        "LOSE": 0,
        "DAMAGE": {
            "DEALT": 0,
            "TAKEN": 0
        },
        "RED_FLAG_PICKUPS": 0,
        "SCORE": 0,
        "MAX_STREAK": 0,
        "DEATHS": 0,  # not implemented
        "PLAY_TIME": 0,  # not implemented
        "BLUE_FLAG_PICKUPS": 0,
        "NAME": None,
        "ABORTED": False,
        "HOLY_SHITS": 0,
        "TEAM_RANK": None,
        "KILLS": 0,  # not implemented
        "MEDALS": {},
        "NEUTRAL_FLAG_PICKUPS": 0,
        "TIED_RANK": None,
        "WIN": 0,
        "TEAM_JOIN_TIME": 0,
        "TEAM": None,  # not implemented
        "RANK": 0,
        "STEAM_ID": None
    }
    """
    Many of not implemented fields are determined later
    during game analysis (e.g. total kills or play time)
    """

    def __init__(self, time: int, match_guid: str, warmup: bool = False):
        super().__init__(time, match_guid, warmup)

        # init pickups
        for key in entities.PICKUPS:
            self.data['PICKUPS'][key] = 0

        # init medals
        for key in entities.MEDALS:
            self.data['MEDALS'][key] = 0

        for key in entities.WEAPONS:
            self.data['WEAPONS'][key] = {
                'K': 0, 'P': 0, 'DR': 0, 'H': 0,
                'D': 0, 'DG': 0, 'T': 0, 'S': 0,
            }

    def set_data(self, name: str, steam_id):
        self.data['NAME'] = name
        self.data['STEAM_ID'] = steam_id

    def add_weapon(self, weapon: str, shots: int, hits: int):
        if weapon not in self.data['WEAPONS']:
            raise ValueError(f"Invalid weapon '{weapon}'")

        self.data['WEAPONS'][weapon]['H'] = hits
        self.data['WEAPONS'][weapon]['S'] = shots
