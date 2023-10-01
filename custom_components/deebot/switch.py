"""Switch module."""
import logging
from typing import Any

from deebot_client.commands.json import (
    SetAdvancedMode,
    SetCarpetAutoFanBoost,
    SetCleanPreference,
    SetContinuousCleaning,
    SetTrueDetect,
    SetAnimProtect,
    SetRainDelay,
    SetSafeProtect,
    SetBorderSwitch,
    SetRecognization,
    SetChildLock,
    SetMoveupWarning,
    SetCrossMapBorderWarning,
)

from deebot_client.commands.json.common import SetEnableCommand
from deebot_client.events import (
    AdvancedModeEvent,
    CarpetAutoFanBoostEvent,
    CleanPreferenceEvent,
    ContinuousCleaningEvent,
    EnableEvent,
    TrueDetectEvent,
    AnimProtectEvent,
    RainDelayEvent,
    SafeProtectEvent,
    BorderSwitchEvent,
    RecognizationEvent,
    ChildLockEvent,
    MoveupWarningEvent,
    CrossMapBorderWarningEvent,
)
from deebot_client.vacuum_bot import VacuumBot
from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory, EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import DeebotEntity
from .hub import DeebotHub

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Add entities for passed config_entry in HA."""
    hub: DeebotHub = hass.data[DOMAIN][config_entry.entry_id]

    new_devices = []
    new_vacuum_devices = []
    new_goat_devices = []

    for vacbot in hub.vacuum_bots:

        new_vacuum_devices.extend(
            [
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="advanced_mode",
                        translation_key="advanced_mode",
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:tune",
                    ),
                    AdvancedModeEvent,
                    SetAdvancedMode,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="continuous_cleaning",
                        translation_key="continuous_cleaning",
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:refresh-auto",
                    ),
                    ContinuousCleaningEvent,
                    SetContinuousCleaning,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="carpet_auto_fan_speed_boost",
                        translation_key="carpet_auto_fan_speed_boost",
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:fan-auto",
                    ),
                    CarpetAutoFanBoostEvent,
                    SetCarpetAutoFanBoost,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="clean_preference",
                        translation_key="clean_preference",
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:broom",
                    ),
                    CleanPreferenceEvent,
                    SetCleanPreference,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="true_detect",
                        translation_key="true_detect",
                        entity_registry_enabled_default=False,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:laser-pointer",
                    ),
                    TrueDetectEvent,
                    SetTrueDetect,
                ),
            ]
        )
        
        new_goat_devices.extend(
            [
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="anim_protect",
                        name="Animal Protection",
                        translation_key="anim_protect",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:paw-off-outline",
                    ),
                    AnimProtectEvent,
                    SetAnimProtect,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="rain_protect",
                        name="Rain Protect",
                        translation_key="rain_protect",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:weather-pouring",
                    ),
                    RainDelayEvent,
                    SetRainDelay,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="safe_protect",
                        name="Charging Station Theft Protection",
                        translation_key="safe_protect",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:robber",
                    ),
                    SafeProtectEvent,
                    SetSafeProtect,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="border_switch",
                        name="Border Cut Switch",
                        translation_key="border_switch",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:border-all-variant",
                    ),
                    BorderSwitchEvent,
                    SetBorderSwitch,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="recognization",
                        name="AI Recognization",
                        translation_key="recognization",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:teddy-bear",
                    ),
                    RecognizationEvent,
                    SetRecognization,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="child_lock",
                        name="Child Lock",
                        translation_key="child_lock",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:human-male-boy",
                    ),
                    ChildLockEvent,
                    SetChildLock,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="moveup_warning",
                        name="Moveup Warning",
                        translation_key="moveup_warning",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:arrow-up-bold-box-outline",
                    ),
                    MoveupWarningEvent,
                    SetMoveupWarning,
                ),
                DeebotSwitchEntity(
                    vacbot,
                    SwitchEntityDescription(
                        key="border_warning",
                        name="Border Left Warning",
                        translation_key="border_warning",
                        entity_registry_enabled_default=True,
                        entity_category=EntityCategory.CONFIG,
                        icon="mdi:selection-marker",
                    ),
                    CrossMapBorderWarningEvent,
                    SetCrossMapBorderWarning,
                ),
            ]
        )

    if new_devices:
        async_add_entities(new_devices)
    if not vacbot.is_goat and new_vacuum_devices:
        async_add_entities(new_vacuum_devices)
    if vacbot.is_goat and new_goat_devices:
        async_add_entities(new_goat_devices)


class DeebotSwitchEntity(DeebotEntity, SwitchEntity):  # type: ignore
    """Deebot switch entity."""

    _attr_is_on = False

    def __init__(
        self,
        vacuum_bot: VacuumBot,
        entity_description: EntityDescription,
        event_type: type[EnableEvent],
        set_command: type[SetEnableCommand],
    ):
        super().__init__(vacuum_bot, entity_description)
        self._event_type = event_type
        self._set_command = set_command

    async def async_added_to_hass(self) -> None:
        """Set up the event listeners now that hass is ready."""
        await super().async_added_to_hass()

        async def on_enable(event: EnableEvent) -> None:
            self._attr_is_on = event.enable
            self.async_write_ha_state()

        self.async_on_remove(
            self._vacuum_bot.events.subscribe(self._event_type, on_enable)
        )

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        await self._vacuum_bot.execute_command(self._set_command(True))

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        await self._vacuum_bot.execute_command(self._set_command(False))
