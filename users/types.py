import enum

class UserStatus(enum.Enum):
   REGISTERED = 'registered'
   REQUESTED_TO_DRIVER = 'requested_to_driver'
   ALLOWED_DRIVE = 'allowed_drive'
   DISSALLOWED_DRIVE = 'disallowed_drive'