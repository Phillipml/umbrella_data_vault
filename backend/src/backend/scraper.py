# %%
from config import url
import requests

resp = requests.get(url)

resp.status_code
# %%
