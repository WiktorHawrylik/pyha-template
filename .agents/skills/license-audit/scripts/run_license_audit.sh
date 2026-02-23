#!/usr/bin/env bash
set -u -o pipefail

usage() {
  cat <<'EOF'
Run AGPL license compliance audit workflow.

Usage:
  run_license_audit.sh [options]

Options:
  --repo-root <path>     Repository root to audit (default: current directory)
  --roots <csv>          Comma-separated roots (default: src,tests,scripts)
  --output-dir <path>    Artifact output directory (default: build/license-compliance)
  --skip-sync            Skip `uv sync --extra all`
  --help                 Show this help
EOF
}

repo_root="$(pwd)"
roots_csv="src,tests,scripts"
output_dir="build/license-compliance"
skip_sync="false"
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="$2"
      shift 2
      ;;
    --roots)
      roots_csv="$2"
      shift 2
      ;;
    --output-dir)
      output_dir="$2"
      shift 2
      ;;
    --skip-sync)
      skip_sync="true"
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "[ERROR] Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if ! command -v uv >/dev/null 2>&1; then
  echo "[ERROR] Missing required command: uv" >&2
  exit 1
fi
if ! command -v grep >/dev/null 2>&1; then
  echo "[ERROR] Missing required command: grep" >&2
  exit 1
fi

IFS=',' read -r -a roots <<< "$roots_csv"
if [[ ${#roots[@]} -eq 0 ]]; then
  echo "[ERROR] No roots provided." >&2
  exit 1
fi

cd "$repo_root" || {
  echo "[ERROR] Cannot enter repository root: $repo_root" >&2
  exit 1
}

if [[ ! -f "scripts/license_audit_headers.py" ]]; then
  echo "[ERROR] Missing script: scripts/license_audit_headers.py" >&2
  exit 1
fi
if [[ ! -f "scripts/license_audit_dependencies.py" ]]; then
  echo "[ERROR] Missing script: scripts/license_audit_dependencies.py" >&2
  exit 1
fi

mkdir -p "$output_dir"
overall_status=0

run_step() {
  local label="$1"
  shift
  echo
  echo "==> ${label}"
  if "$@"; then
    echo "[OK] ${label}"
  else
    local step_status=$?
    echo "[WARN] ${label} failed with exit code ${step_status}."
    overall_status=1
  fi
}

if [[ "$skip_sync" == "false" ]]; then
  run_step "Sync environment" uv sync --extra all
else
  echo "[INFO] Skipping environment sync."
fi

header_cmd=(uv run python scripts/license_audit_headers.py --roots)
for root in "${roots[@]}"; do
  if [[ -n "$root" ]]; then
    header_cmd+=("$root")
  fi
done
header_cmd+=(--output "${output_dir}/header-audit.csv")
run_step "Validate license headers" "${header_cmd[@]}"

echo
echo "==> Extract dependency licenses"
if uv run pip-licenses \
  --with-urls \
  --with-authors \
  --from=mixed \
  --format=csv \
  > "${output_dir}/dependency-licenses.csv"; then
  echo "[OK] Extract dependency licenses"
else
  step_status=$?
  echo "[WARN] Extract dependency licenses failed with exit code ${step_status}."
  overall_status=1
fi

run_step "Categorize dependency licenses" \
  uv run python scripts/license_audit_dependencies.py \
    --input-csv "${output_dir}/dependency-licenses.csv" \
    --output-csv "${output_dir}/dependency-license-audit.csv"

echo
echo "==> Verify third-party attribution markers"
: > "${output_dir}/third-party-attribution-grep.txt"
for root in "${roots[@]}"; do
  [[ -d "$root" ]] || continue
  grep -R -n -E "Source:|License:|Copyright" "$root" \
    >> "${output_dir}/third-party-attribution-grep.txt" || true
done
echo "[OK] Verify third-party attribution markers"

run_step "Summarize audit results" \
  uv run python "${script_dir}/summarize_license_audit.py" \
    --artifacts-dir "${output_dir}"

if [[ $overall_status -ne 0 ]]; then
  echo
  echo "[FAIL] License compliance audit reported failures."
  exit 1
fi

echo
echo "[PASS] License compliance audit completed successfully."
