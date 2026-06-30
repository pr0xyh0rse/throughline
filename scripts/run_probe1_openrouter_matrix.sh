#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="${ENV_FILE:-config/openrouter.local.env}"
MODEL_FILE="${MODEL_FILE:-config/model_matrix_openrouter.txt}"
TEMPERATURE_VALUE="${TEMPERATURE:-0.7}"
MAX_TOKENS_VALUE="${MAX_TOKENS:-1800}"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing env file: $ENV_FILE" >&2
  echo "Copy config/openrouter.env.example to config/openrouter.local.env and add your key." >&2
  exit 1
fi

if [[ ! -f "$MODEL_FILE" ]]; then
  echo "Missing model matrix file: $MODEL_FILE" >&2
  exit 1
fi

limit_args=()
if [[ "${LIMIT:-}" != "" ]]; then
  limit_args=(--limit "$LIMIT")
fi

while IFS= read -r raw_model || [[ -n "$raw_model" ]]; do
  model="${raw_model%%#*}"
  model="$(printf '%s' "$model" | xargs)"
  if [[ -z "$model" ]]; then
    continue
  fi

  echo "=== Probe 1 / $model ==="
  python3 scripts/run_probe1_openai_compatible.py \
    --env-file "$ENV_FILE" \
    --env-override \
    --model "$model" \
    --temperature "$TEMPERATURE_VALUE" \
    --max-tokens "$MAX_TOKENS_VALUE" \
    "${limit_args[@]}"
done < "$MODEL_FILE"
