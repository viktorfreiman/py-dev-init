__doc__ = """

docs_helper.py
--------------

| Small script that makes it easier to work with intersphinx it takes config data from docs/conf.py
| :doc:`sphinx:usage/extensions/intersphinx`

:ref:`sphinx:xref-syntax`

| insted of: ``python -m sphinx.ext.intersphinx https://www.sphinx-doc.org/en/master/objects.inv``
| run ``python scripts/docs_helper.py.py`` and then pick the project you want.

Wraps also over `sphobjinv <https://github.com/bskinn/sphobjinv>`_ to make easy to search

"localhost" need to have a webserver with built html from sphinx,
have ``autobuild-html-docs`` running

.. todo::
    have better support for finding port of autobuild-html-docs
    use psutil?
"""

import sys
from pathlib import Path
import os
from urllib.parse import urljoin
import signal


def signal_SIGINT_handler(signal, frame):
    """This is to have a nicer printout on KeyboardInterrupt"""
    print("\nGOT SIGINT(Probably KeyboardInterrupt), Quitting")
    sys.exit(0)


def main():
    project_path = Path(__file__).absolute().parents[1]

    # we need this for import to work
    sys.path.insert(0, str(project_path))

    print("Intersphinx objects.inv printout")
    print("intersphinx_mapping is from docs/conf.py")

    from docs.conf import intersphinx_mapping

    # add localhost to make easy to see self
    intersphinx_mapping["localhost"] = ("http://127.0.0.1:8000/", None)

    for i, doc in enumerate(intersphinx_mapping.keys()):
        print(f"{i}) {doc}")
    int_picker = int(input("Pick a number for docs: "))

    picked_name = list(intersphinx_mapping.keys())[int_picker]
    print(f"picked: {picked_name}\n")

    type_picker = int(
        input(
            f"0) Print all from objects.inv from {picked_name}\n"
            f"1) Search and suggest object\n"
            f"Select mode: "
        )
    )

    # the extra slash if it is missing in the config data
    # and urljoin will fix the url for us
    obj_inv_url = urljoin(intersphinx_mapping[picked_name][0] + "/", "objects.inv")

    if type_picker:
        print("--- sphobjinv ---")
        search = input("Search: ")
        cli = f"sphobjinv suggest {obj_inv_url} {search} -su"

    else:
        print("--- intersphinx ---")
        cli = f"{sys.executable} -m sphinx.ext.intersphinx {obj_inv_url}"

    os.system(cli)

    # todo: Change this printout to use triple quotes insted
    print(
        "--- Note ---\n"
        "Please note the output from this tools\n"
        "need to be changed to work as a cross-references\n"
        "Exemple:\n"
        ":std:label:`thing_to_link` -> :ref:`thing_to_link`\n"
        "or\n"
        ":std:label:`thing_to_link` -> :ref:`project_name:thing_to_link`\n\n"
        ":py:function:`that_func`   -> :py:func:`that_func`\n"
        "or\n"
        ":py:function:`that_func`   -> :py:func:`project_name:that_func`\n"
        "--- Note ---\n"
    )

    print(
        "--- Links ---\n"
        "Link for intersphinx cross-referencing tags\n"
        "https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#xref-syntax\n"  # noqa b950
        "--- Links ---\n"
    )

    print(f"CLI:\n{cli}")


if __name__ == "__main__":
    # activate signal
    signal.signal(signal.SIGINT, signal_SIGINT_handler)

    main()
