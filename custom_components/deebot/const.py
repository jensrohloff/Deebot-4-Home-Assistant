"""Const module."""
from collections.abc import Mapping
from typing import Literal
from deebot_client.events import (
    BatteryEvent,
    CleanLogEvent,
    ErrorEvent,
    Event,
    FanSpeedEvent,
    LifeSpanEvent,
    GoatLifeSpanEvent,
    RoomsEvent,
    StateEvent,
    StatsEvent,
    WaterInfoEvent,
)
from deebot_client.models import VacuumState
from homeassistant.components.vacuum import (
    STATE_CLEANING,
    STATE_DOCKED,
    STATE_ERROR,
    STATE_IDLE,
    STATE_PAUSED,
    STATE_RETURNING,
)
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, CONF_VERIFY_SSL

################################
# Do not change! Will be set by release workflow
INTEGRATION_VERSION = "dev"  # git tag will be used
MIN_REQUIRED_HA_VERSION = "2022.10.0b0"  # set min required version in hacs.json
################################

# Values below can be changed
DOMAIN = "deebot"
ISSUE_URL = "https://github.com/DeebotUniverse/Deebot-4-Home-Assistant/issues"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{DOMAIN}
Version: {INTEGRATION_VERSION}
This is a custom component
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

CONF_COUNTRY = "country"
CONF_CONTINENT = "continent"
CONF_BUMPER = "Bumper"
CONF_MODE_BUMPER = CONF_BUMPER
CONF_MODE_CLOUD = "Cloud (recommended)"
CONF_CLIENT_DEVICE_ID = "client_device_id"

# Bumper has no auth and serves the urls for all countries/continents
BUMPER_CONFIGURATION = {
    CONF_CONTINENT: "eu",
    CONF_COUNTRY: "it",
    CONF_PASSWORD: CONF_BUMPER,
    CONF_USERNAME: CONF_BUMPER,
    CONF_VERIFY_SSL: False,  # required as bumper is using self signed certificates
}

DEEBOT_DEVICES = f"{DOMAIN}_devices"

VACUUMSTATE_TO_STATE = {
    VacuumState.IDLE: STATE_IDLE,
    VacuumState.CLEANING: STATE_CLEANING,
    VacuumState.RETURNING: STATE_RETURNING,
    VacuumState.DOCKED: STATE_DOCKED,
    VacuumState.ERROR: STATE_ERROR,
    VacuumState.PAUSED: STATE_PAUSED,
}


LAST_ERROR = "last_error"


REFRESH_STR_TO_EVENT_DTO: Mapping[str, type[Event]] = {
    "battery": BatteryEvent,
    "clean_logs": CleanLogEvent,
    "error": ErrorEvent,
    "fan_speed": FanSpeedEvent,
    "life_spans": LifeSpanEvent,
    "goat_life_spans": GoatLifeSpanEvent,
    "rooms": RoomsEvent,
    "stats": StatsEvent,
    "status": StateEvent,
    "water": WaterInfoEvent,
}
REFRESH_MAP = "map"

EVENT_CLEANING_JOB = "deebot_cleaning_job"
EVENT_CUSTOM_COMMAND = "deebot_custom_command"
