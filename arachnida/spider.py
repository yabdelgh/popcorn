#!/usr/bin/env python3
import argparse
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def ft_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r',
                        type=int,         # ensure it gets parsed as an integer
                        nargs='?',        # means the argument is optional
                        const=5,          # value to use if -r is provided without a value
                        default=None,        # default value if -r is not provided
                        help='Recursively downloads the images in a URL received as a parameter.')
    parser.add_argument('-l',
                        type=int,         # ensure it gets parsed as an integer
                        default=None,        # default value if -r is not provided
                        help='Recursively downloads the images in a URL received as a parameter.')
    parser.add_argument('-p',
                        type=str,
                        default='./data/',
                        help='Recursively downloads the images in a URL received as a parameter.')
    parser.add_argument('url', help="The URL or last positional argument", default=None)

    args = parser.parse_args()
    print(args)
    if args.r is None and args.l is not None:
        parser.error('Argument -l can only be provided if -r is specified.')
    if args.l is not None:
        args.r = args.l
    return args

def ft_spider(depth: int, url: str):
    if (depth is not 0):
        return ft_spider(depth-1, url)

def ft_extract_images(url, response):
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')  # Finds all <img> tags
    image_urls = []
    for img in images:
        img_url = img.get('src')
        if img_url:
            if img_url.startswith('http'):
                image_urls.append(img_url)
            else:
                image_urls.append(url + img_url)
    return image_urls

def main():
    args = ft_parser()

    
    folder_path = Path(args.p)
    folder_path.mkdir(parents=True, exist_ok=True)
    response = requests.get(args.url)
    if response.status_code == 200:
        image_urls = ft_extract_images(url=args.url, response=response)
        print(image_urls)
        print(len(image_urls))
    return 0

if __name__ == "__main__":
    main()