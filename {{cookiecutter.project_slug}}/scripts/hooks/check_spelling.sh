#!/bin/bash

# scripts/hooks/check_spelling.sh
# Run aspell on the commit content using a personal dictionary.

# Container Only:  Please use this hook inside a PIB container.

set -eo pipefail

DEFAULT_USER_DICTIONARY="$(git rev-parse --show-toplevel)/.aspell.pws"
COMMIT_MESSAGE_HEADER="Please enter the commit message for your changes."

spell_check() {

  USER_DICTIONARY=${USER_DICTIONARY:-"${DEFAULT_USER_DICTIONARY}"}
  COMMIT_MESSAGE=$(sed "/${COMMIT_MESSAGE_HEADER}/q" "${1}" | grep -v "${COMMIT_MESSAGE_HEADER}") # Linux or Mac
  ERRORS=$(echo "${COMMIT_MESSAGE}" | aspell --encoding="${GIT_HOOKS_ASPELL_ENCODING}" --personal="${USER_DICTIONARY}" --lang="${GIT_HOOKS_ASPELL_LANG}" -t --list)

  if [ -n "${ERRORS}" ]; then
    echo "YOUR COMMIT MESSAGE:"
    echo "${COMMIT_MESSAGE}"
    echo -e "\\nWARNING: possible spelling error in commit message:\\n"
    echo -e "${ERRORS}\\n"
    echo -e "(You may wish to add these words to the local '.aspell.pws' file.)\\n"
    exit 127
  fi

}

main() {

  spell_check "$@"

}

main "$@"
