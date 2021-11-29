import requests as req


class SuperHeroApi:

	TOKEN = '2619421814940190'
	URL = 'https://superheroapi.com/api/'

	def get_heros_stats(self, name):
		query_url = self.URL + self.TOKEN + '/search/' + name.lower()
		return req.get(query_url).json()['results'][0]['powerstats']

	def get_smartest_one(self, heroes_lst):
		intelligence_lst = []
		for hero in heroes_lst:
			intelligence = self.get_heros_stats(hero)['intelligence']
			intelligence_lst.append((hero, int(intelligence)))
		intelligence_lst.sort(key=lambda elem: elem[1], reverse=True)
		return intelligence_lst[0][0]


if __name__ == '__main__':
	heroes_lst = ['Hulk', 'Captain America', 'Thanos']
	sh = SuperHeroApi()
	smartest_one = sh.get_smartest_one(heroes_lst)
	print(f'{smartest_one} is the smartest of the given characters!')