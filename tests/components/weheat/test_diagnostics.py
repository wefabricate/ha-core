"""Tests for the diagnostics data provided by the Withings integration."""

from unittest.mock import AsyncMock

import pytest
from syrupy import SnapshotAssertion
from syrupy.filters import props
from weheat.abstractions.discovery import HeatPumpDiscovery

from homeassistant.core import HomeAssistant

from . import setup_integration

from tests.common import MockConfigEntry
from tests.components.diagnostics import get_diagnostics_for_config_entry
from tests.typing import ClientSessionGenerator


@pytest.mark.usefixtures("setup_credentials")
async def test_diagnostics_config_entry(
    hass: HomeAssistant,
    hass_client: ClientSessionGenerator,
    mock_weheat_discover: AsyncMock,
    mock_weheat_heat_pump: AsyncMock,
    mock_heat_pump_info: HeatPumpDiscovery.HeatPumpInfo,
    mock_config_entry: MockConfigEntry,
    snapshot: SnapshotAssertion,
) -> None:
    """Test the Weheat setup."""
    await setup_integration(hass, mock_config_entry)

    assert await get_diagnostics_for_config_entry(
        hass, hass_client, mock_config_entry
    ) == snapshot(exclude=props("expires_at", "modified_at", "repr"))
