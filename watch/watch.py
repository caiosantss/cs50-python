import re
import sys


def main():
    print(parse(input("HTML: "))).strip()


def parse(s):

    pattern = r"^<iframe(?:.+)?src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/(?P<video_id>[\w-]+)\"(?:.+)?</iframe>$"

    match = re.search(pattern, s)

    if match:
        video_id = match.group("video_id")
        link = f'https://youtu.be/{video_id}'
        return link
    else:
        return None


if __name__ == "__main__":
    main()
