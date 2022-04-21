import requests
from bs4 import BeautifulSoup


def get_user_input():
    start, count, text = (0, 50, 'default')
    while True:
        try:
            start = int(input('Please enter start point (number): '))
            count = int(input('Please enter amount of games (min 25, max 100): '))
            break
        except ValueError:
            print('integers only please.')
            continue
        except EOFError:
            print("Please input something....")
            continue
    while True:
        try:
            text = str(input('Please enter search request: '))
            break
        except TypeError:
            print('Letters only please.')
            continue
        except EOFError:
            print("Please input something....")
            continue

    return start, count, text


def create_url(start, count, text):
    return (
        'https://store.steampowered.com/search/results/?'
        'query&'
        f'start={start}&'
        f'count={count}&'
        'dynamic_data=&'
        'sort_by=_ASC&'
        f'term={text}&'
        'snr=1_7_7_151_7&'
        'infinite=1'
    )


if __name__ == '__main__':
    url = create_url(*get_user_input())
    response_json = requests.get(url).json()

    soup = BeautifulSoup(response_json['results_html'], 'lxml')
    games = soup.find_all('span', attrs={'class': 'title'})
    game_titles = tuple(map(lambda game_title: game_title.text, games))

    print(f'Here is your {len(game_titles)} games:')
    for title in game_titles:
        print(title)
