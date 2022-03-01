#!/bin/bash

# scripts/extras.sh
# Allow use of the CLI outside a containerized environment.  (Not recommended.)

# Host machine only:  Please do not use this script inside a PIB container.

halt() {
  # $1 - Message

  echo "$1"
  exit 127
}

# Release Tests

# Container
echo "Checking for container ..."
./scripts/check_container.sh

# Formatting
echo "Checking formatting ..."
./scripts/check_formatting.sh

# Add Additional Checks Here >

echo "Release Looks Good."
