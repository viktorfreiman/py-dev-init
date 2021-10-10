#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# Initialize work From: https://github.com/Azure/azure-functions-docker/blob/master/host/3.0/buster/amd64/python/python38/python38-core-tools.Dockerfile
# V: expanded and fixed the .bashrc and more
# MIT License
#
# Copyright (c) 2020 Viktor Freiman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM mcr.microsoft.com/vscode/devcontainers/python:3.8

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# https://github.com/microsoft/vscode-dev-containers/blob/main/CONTRIBUTING.md#why-do-dockerfiles-in-this-repository-use-run-statements-with-commands-separated-by-

# Configure apt and install packages
RUN apt update && apt install -y vim jq bash-completion

# get vanila bash
# use zsh (already installed) if you want a 'better' shell
# remove old .bashrc and reset bashrc to default
RUN cp /etc/skel/.bashrc /home/$USERNAME/.bashrc \
    && echo "\n\
alias l='ls -alh' \n\
alias p='python'" >> /home/$USERNAME/.bashrc

# Clean up
RUN apt autoremove -y \
    && apt clean -y \
    && mkdir -p /home/$USERNAME/.local/share \
    && chown -R $USERNAME /home/$USERNAME

ENV XDG_DATA_HOME=/home/$USERNAME/.local/share

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog