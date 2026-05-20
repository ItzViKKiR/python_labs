class PropertyNotFoundError(Exception):
    """Недвижимость не найдена."""
    pass


class DuplicatePropertyError(Exception):
    """Недвижимость уже существует."""
    pass