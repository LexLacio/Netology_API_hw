import requests


def int_check(hero_1, hero_2, hero_3):
    link = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    resp = requests.get(url=link)
    if resp.status_code != 200:
        print(f'Error code: {resp.status_code}')
        return
    else:
        all_heroes_list = resp.json()
        heroes_list = {}
        for hero in all_heroes_list:
            if hero['name'] == hero_1:
                heroes_list[hero['name']] = int(hero["powerstats"]["intelligence"])
            if hero['name'] == hero_2:
                heroes_list[hero['name']] = int(hero["powerstats"]["intelligence"])
            if hero['name'] == hero_3:
                heroes_list[hero['name']] = int(hero["powerstats"]["intelligence"])

        sorted_heroes_tuple = sorted(heroes_list.items(), key=lambda x: x[1])
        print(f'{sorted_heroes_tuple[-1]} - самый умный персонаж среди {hero_1}, {hero_2}, {hero_3}')
        return sorted_heroes_tuple


if __name__ == '__main__':
    int_check("Captain America", "Hulk", "Thanos")
