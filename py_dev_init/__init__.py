"""
This is a docstring

`Docs how to write docstring
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_
"""
import requests


def main():
    """Make a requests to "https://example.com/" """
    url = "https://example.com/"
    r = requests.head(url)

    print(f"{url} returned {r.status_code}")


if __name__ == "__main__":
    main()
