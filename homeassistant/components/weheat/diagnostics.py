"""Diagnostics support for Weheat."""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.const import CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant

from . import WeheatConfigEntry
from .const import CONF_REFRESH_TOKEN

TO_REDACT = {CONF_ACCESS_TOKEN, CONF_REFRESH_TOKEN}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: WeheatConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    diag_data = {}

    for coordinator in entry.runtime_data:
        diag_data[coordinator.heatpump_id] = {
            "heat_pump_info": coordinator.heat_pump_info.__dict__,
            "heat_pump_data": coordinator.data.raw_content,
            "session_valid": coordinator.session.valid_token,
            "session_token": async_redact_data(coordinator.session.token, TO_REDACT),
        }

    return diag_data
