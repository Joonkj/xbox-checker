import requests
from colorama import init
from random import choices, choice

init(autoreset=True)

checked = []

def ello():
  proxy = choice(open('proxies.txt', 'r').read().splitlines())
  proxies = {'http': f'http://{proxy}', 'http': f'http://{proxy}'}
  while True:
    username = ''.join(choices('abcdefghijklmnopqrstuvwxyz', k=4))
    if "x" in username:
      headers = {
          'authority':
          'xboxgamertag.com',
          'accept':
          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language':
          'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
          'referer':
          'https://xboxgamertag.com/',
          'sec-ch-ua':
          '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
          'sec-ch-ua-mobile':
          '?0',
          'sec-ch-ua-platform':
          '"Windows"',
          'sec-fetch-dest':
          'document',
          'sec-fetch-mode':
          'navigate',
          'sec-fetch-site':
          'same-origin',
          'sec-fetch-user':
          '?1',
          'upgrade-insecure-requests':
          '1',
          'user-agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
      }

      try:
        response = requests.get(f'https://xboxgamertag.com/search/{username}',
                                headers=headers,
                                proxies=proxies)
        if response.status_code == 200:
          print(f"\033[91m{username} ❌\033[0m")
        elif response.status_code == 404:
          print(f"\033[92m{username} ✅\033[0m")
          with open("Available.txt", 'a') as f:
            f.write(username + '\n')
        else:
          print("\033[91m You have been rate limited ⚠️\033[0m")

      except Exception as e:
        print(e)
    else:
      pass

ello()