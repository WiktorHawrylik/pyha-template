#!/usr/bin/env bash
# Fail if AGENTS.md is missing or empty to enforce LLM guardrails.
set -euo pipefail

if [[ ! -s "AGENTS.md" ]]; then
  echo "AGENTS.md is missing or empty."
  exit 1
fi

echo "AGENTS.md present."
