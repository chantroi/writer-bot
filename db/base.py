from deta import Deta 
from lib.env import deta_key

deta = Deta(deta_key)
v2ray_notes = deta.Base("notes")
savessh = deta.Base("ssh")