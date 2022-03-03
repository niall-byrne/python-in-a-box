#!/bin/bash

# .github/scripts/notifications.sh
# Sends a notification to slack.

# 1: The branch information to display.
# 2: The notification message to send.
# WEBHOOK_URL: The slack webhook url to use.

# CI only script.

main() {

  [[ -z ${WEBHOOK_URL} ]] && exit 0
  curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"${1}: ${2}\"}" "${WEBHOOK_URL}"

}

main "$@"
