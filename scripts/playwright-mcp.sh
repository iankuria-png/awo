#!/usr/bin/env bash
# Starts the Playwright MCP server (browser automation for Claude).
#
# - In Claude Code cloud sessions, uses the pre-installed Chromium and trusts
#   the session's egress-proxy CA by its public-key pin (TLS stays verified).
# - On a normal machine, falls back to Playwright's defaults.
set -euo pipefail

config='{"browser":{"browserName":"chromium","isolated":true,"launchOptions":{"headless":true'

chromium="$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -n 1 || true)"
if [ -n "$chromium" ]; then
  config+=",\"executablePath\":\"$chromium\""
fi

proxy_ca="/root/.ccr/agent-proxy-ca.crt"
if [ -f "$proxy_ca" ]; then
  spki="$(openssl x509 -in "$proxy_ca" -pubkey -noout \
    | openssl pkey -pubin -outform der \
    | openssl dgst -sha256 -binary | base64)"
  config+=",\"args\":[\"--ignore-certificate-errors-spki-list=$spki\"]"
fi

config+='},"contextOptions":{"viewport":{"width":1440,"height":1000}}}}'

config_file="$(mktemp -t playwright-mcp-XXXXXX.json)"
printf '%s\n' "$config" > "$config_file"

exec npx -y @playwright/mcp@latest --config "$config_file"
