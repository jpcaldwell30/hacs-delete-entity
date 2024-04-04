# Delete-Entity

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This integration allows deleting specific entities from home assistant. Useful in the case where you get the error message about an entity not having an unique identifier.

The entegration adds a service to home asssistant called delete_entity that you can be called through the developer tools service tab. You can then specify the entity to be deleted.

## Installation instructions

- Install using [HACS](https://hacs.xyz) (Or copy the contents of `custom_components/tuya/` to `<your config dir>/custom_components/delete_entity/`.)

- Restart Home Assistant