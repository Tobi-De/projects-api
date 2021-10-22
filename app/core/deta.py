from deta import Deta

from .config import settings

deta = Deta(settings.DETA_PROJECT_KEY)
db = deta.Base("projects")
drive = deta.Drive("projects")
