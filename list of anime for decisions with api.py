from jikanpy import Jikan
import pandas as pd
import pprint
api = "https://api.jikan.moe/v4/anime/20"

jikan = Jikan()

nar = jikan.anime(20)
pprint.pprint(nar)
print(nar['data']['episodes'])
anime = [(nar['data']['title'],nar['data']['episodes'],nar['data']['score'])]

df = pd.DataFrame(data= anime , columns=['title','number of episodes', 'rating'])
print(df)