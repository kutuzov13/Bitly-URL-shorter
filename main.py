import argparse
import os

import dotenv
import requests

from urllib.parse import urlparse


def is_link_bitlink(token, bitlink):
    parsed_link = urlparse(bitlink)
    headers = {'Authorization': token}
    bitlink_info = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}'
    response = requests.get(bitlink_info, headers=headers)
    return response.ok


def get_shorten_link(token, link):
    create_bitlink_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {'long_url': link}
    headers = {'Authorization': token}
    response = requests.post(create_bitlink_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get('link')


def get_count_clicks(token, bitlink):
    parsed_link = urlparse(bitlink)
    params = {'unit': 'day',
              'units': '-1'}
    headers = {'Authorization': token}
    count_bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}/clicks/summary'
    response = requests.get(count_bitlink, params=params, headers=headers)
    response.raise_for_status()
    return response.json().get('total_clicks')


def main():
    dotenv.load_dotenv()
    bitlink_token = os.getenv('BITLINK_TOKEN')

    parser = argparse.ArgumentParser(
        description='Shortens the link, if the link is already shortened, the number of clicks on it will be shown'
    )
    parser.add_argument('link', help='You link')
    args = parser.parse_args()
    try:
        if is_link_bitlink(bitlink_token, args.link):
            print(f'Counting clicks on a link: {get_count_clicks(bitlink_token, args.link)}')
        else:
            print(f'Short link: {get_shorten_link(bitlink_token, args.link)}')
    except requests.exceptions.HTTPError as error:
        print(f'Error in request! {error}')


if __name__ == '__main__':
    main()
