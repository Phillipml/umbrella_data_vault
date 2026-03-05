# %%
from config import cookies, headers
import requests

res = requests.get(
    "https://www.residentevildatabase.com/personagens/ada-wong/",
    cookies=cookies,
    headers=headers,
)
# %%
res.status_code
# %%
html = res.text
