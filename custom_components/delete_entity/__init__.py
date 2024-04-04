from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .service import async_setup_entry

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    await async_setup_entry(hass, config)
    return True
