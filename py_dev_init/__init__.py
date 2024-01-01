"""This is a docstring.

`Docs how to write docstring
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_
"""
import requests

__version__ = "1.0.2"


def main():
    """Make a requests to "https://example.com/" and print the status code."""
    url = "https://example.com/"
    r = requests.head(url, timeout=5)

    print(f"{url} returned {r.status_code}")


if __name__ == "__main__":
    main()
