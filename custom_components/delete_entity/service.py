import logging
from typing import Any

import homeassistant.helpers.entity_registry as er
import homeassistant.helpers.device_registry as dr
from homeassistant.core import HomeAssistant, ServiceCall

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: dict[str, Any]) -> bool:
    """Set up the Delete Entity integration."""
    _LOGGER.debug(f"Attempting setup of delete_entity integration")
    async def async_delete_entity_service(service_call: ServiceCall) -> None:
        await async_delete_entity(hass, service_call)

    hass.services.async_register("delete_entity", "delete_entity", async_delete_entity_service)
    return True


async def async_delete_entity(hass: HomeAssistant, service_call: ServiceCall) -> None:
    """Delete the specified entity."""
    entity_id = service_call.data["entity_id"]
    entity_registry = er.async_get(hass)

    entity_entry = entity_registry.async_get(entity_id)
    if entity_entry is None:
        _LOGGER.error(f"Entity '{entity_id}' not found in the entity registry.")
        return

    _LOGGER.info(f"Deleting entity '{entity_id}'")
    entity_registry.async_remove(entity_entry.entity_id)