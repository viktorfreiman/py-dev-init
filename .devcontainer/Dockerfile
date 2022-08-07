FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG HOME=/home/$USERNAME

ENV PATH=$HOME/.local/bin:${PATH}
ENV XDG_DATA_HOME=$HOME/.local/share
# https://github.com/microsoft/vscode-dev-containers/blob/main/CONTRIBUTING.md#why-do-dockerfiles-in-this-repository-use-run-statements-with-commands-separated-by-

# Configure apt and install packages
RUN apt update && apt install -y vim jq bash-completion \
    # install Poetry
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - \
    # get vanila bash
    # use zsh (already installed) if you want a 'better' shell
    # remove old .bashrc and reset bashrc to default
    # all docs commands need to run from the docs folder
    && cp /etc/skel/.bashrc $HOME/.bashrc \
    && echo "\n\
alias l='ls -alh' \n\
alias p='python' \n\
export PATH='$HOME/.local/bin:$PATH' \n\
alias build-pdf='sphinx-build -b rinoh . _build/rinoh -t pdf' \n\
alias autobuild-html-docs='sphinx-autobuild . _build/html/ --watch ../.'">> $HOME/.bashrc \
    #
    # https://stackoverflow.com/a/54763270
    && poetry config virtualenvs.create false \
    #
    # https://python-poetry.org/docs/master#enable-tab-completion-for-bash-fish-or-zsh
    && poetry completions bash > /etc/bash_completion.d/poetry.bash-completion \
    #
    # Clean up
    && apt autoremove -y \
    && apt clean -y \
    && mkdir -p $HOME/.local/share \
    && chown -R $USERNAME $HOME


# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog