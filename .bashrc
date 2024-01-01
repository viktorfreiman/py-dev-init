
. <(pdm completion bash)
alias l='ls -alh'
alias p='python'
alias fast-html-docs='./sws --root _build/html/'
alias build-pdf='sphinx-build -b rinoh . _build/rinoh -t pdf'
alias autobuild-html-docs='sphinx-autobuild . _build/html/ --watch ../.'
# pdm is updated by devcontainer features
export PDM_CHECK_UPDATE=False