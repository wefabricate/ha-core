"""Base entity for Weheat."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER
from .coordinator import WeheatDataUpdateCoordinator
from . import HeatPumpInfo


class WeheatEntity(CoordinatorEntity[WeheatDataUpdateCoordinator]):
    """Defines a base Weheat entity."""

    _attr_has_entity_name = True

    def __init__(
        self,
        heat_pump_info: HeatPumpInfo,
        coordinator: CoordinatorEntity,
    ) -> None:
        """Initialize the Weheat entity."""
        super().__init__(coordinator)
        self.heat_pump_info = heat_pump_info

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, heat_pump_info.heatpump_id)},
            name=heat_pump_info.readable_name,
            manufacturer=MANUFACTURER,
            model=heat_pump_info.model,
        )
