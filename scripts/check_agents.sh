#!/usr/bin/env bash
# Fail if AGENTS.md is missing or empty to keep guardrails in place.
set -euo pipefail

if [[ ! -s "AGENTS.md" ]]; then
  echo "AGENTS.md is missing or empty."
  exit 1
fi

