#!/usr/bin/env bash
# =============================================================================
# DreamBoard Pulse — Core Library
# Inspired by .openclaw heartbeat + memory system
# =============================================================================

set -euo pipefail

# Colors
C_RESET='\033[0m'
C_BOLD='\033[1m'
C_DIM='\033[2m'
C_RED='\033[31m'
C_GREEN='\033[32m'
C_YELLOW='\033[33m'
C_BLUE='\033[34m'
C_MAGENTA='\033[35m'
C_CYAN='\033[36m'

# Paths
DBPULSE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IDEAS_DIR="$DBPULSE_ROOT/ideas"
MEMORY_DIR="$DBPULSE_ROOT/memory"
DAILY_DIR="$MEMORY_DIR/daily"
INDEX_FILE="$DBPULSE_ROOT/IDEA-INDEX.md"
HEARTBEAT_STATE="$MEMORY_DIR/heartbeat-state.json"

# Date helpers
_today() { date +%Y-%m-%d; }
_now() { date +%Y-%m-%dT%H:%M:%S; }
_days_since() {
    local file="$1"
    if [[ ! -f "$file" ]]; then echo "9999"; return; fi
    local mtime
    mtime=$(stat -c %Y "$file" 2>/dev/null || stat -f %m "$file" 2>/dev/null)
    local now
    now=$(date +%s)
    echo $(( (now - mtime) / 86400 ))
}

# File helpers
_idea_date() {
    local basename
    basename=$(basename "$1")
    echo "${basename:0:10}"
}

_idea_title() {
    local file="$1"
    grep -m1 '^# ' "$file" 2>/dev/null | sed 's/^# //' || echo "Untitled"
}

_idea_spark() {
    local file="$1"
    grep -m1 '^\*\*Spark:' "$file" 2>/dev/null | sed 's/^\*\*Spark:\*\*[[:space:]]*//' || echo "?"
}

_idea_tags() {
    local file="$1"
    grep -m1 '^\*\*Tags:' "$file" 2>/dev/null | sed 's/^\*\*Tags:\*\*[[:space:]]*//' || echo ""
}

# Logging helpers
_log_info() { echo -e "${C_BLUE}ℹ${C_RESET}  $*"; }
_log_ok()   { echo -e "${C_GREEN}✔${C_RESET}  $*"; }
_log_warn() { echo -e "${C_YELLOW}⚠${C_RESET}  $*"; }
_log_err()  { echo -e "${C_RED}✖${C_RESET}  $*"; }
_log_section() { echo -e "\n${C_BOLD}${C_CYAN}$*${C_RESET}\n"; }

# Ensure state file exists
_ensure_state() {
    if [[ ! -f "$HEARTBEAT_STATE" ]]; then
        mkdir -p "$(dirname "$HEARTBEAT_STATE")"
        echo '{"lastChecks":{"health":null,"index":null,"digest":null},"alerts":[]}' > "$HEARTBEAT_STATE"
    fi
}

# Update state field
_update_state() {
    local key="$1"
    local val="$2"
    _ensure_state
    python3 -c "
import json, sys
with open('$HEARTBEAT_STATE','r') as f: d=json.load(f)
d['$key'] = $val
with open('$HEARTBEAT_STATE','w') as f: json.dump(d,f,indent=2)
" 2>/dev/null || true
}

_update_state_str() {
    local key="$1"
    local val="$2"
    _ensure_state
    python3 -c "
import json, sys
with open('$HEARTBEAT_STATE','r') as f: d=json.load(f)
d['$key'] = '$val'
with open('$HEARTBEAT_STATE','w') as f: json.dump(d,f,indent=2)
" 2>/dev/null || true
}

# Get state field
_get_state() {
    local key="$1"
    _ensure_state
    python3 -c "
import json
with open('$HEARTBEAT_STATE','r') as f: d=json.load(f)
print(d.get('$key',''))
" 2>/dev/null || echo ""
}

# Count ideas
count_ideas() {
    local dir="$1"
    if [[ -d "$dir" ]]; then
        find "$dir" -maxdepth 1 -name '*.md' -type f | wc -l | tr -d ' '
    else
        echo "0"
    fi
}

# List ideas with metadata
list_ideas() {
    local dir="$1"
    if [[ ! -d "$dir" ]]; then return; fi
    for f in "$dir"/*.md; do
        [[ -f "$f" ]] || continue
        local date slug title spark tags age
        date=$(basename "$f" | cut -d'-' -f1-3)
        slug=$(basename "$f" .md | cut -d'-' -f4-)
        title=$(_idea_title "$f")
        spark=$(_idea_spark "$f")
        tags=$(_idea_tags "$f")
        age=$(_days_since "$f")
        printf '%s\t%s\t%s\t%s\t%s\t%d\n' "$date" "$slug" "$title" "$spark" "$tags" "$age"
    done
}

# Find stale ideas
find_stale() {
    local dir="$1"
    local threshold="$2"
    local label="$3"
    while IFS=$'\t' read -r date slug title spark tags age; do
        if [[ "$age" -ge "$threshold" ]]; then
            printf '%s\t%s\t%d\t%s\n' "$title" "$date" "$age" "$label"
        fi
    done < <(list_ideas "$dir")
}

# Find developing ideas missing lean canvas
find_missing_lean_canvas() {
    for f in "$IDEAS_DIR"/developing/*.md; do
        [[ -f "$f" ]] || continue
        local slug
        slug=$(basename "$f" .md)
        # Check if a lean canvas exists linking to this idea
        if ! grep -rl "$slug" "$DBPULSE_ROOT"/docs/lean-canvas/ >/dev/null 2>&1; then
            _idea_title "$f"
        fi
    done
}

# Find developing ideas missing experiments
find_missing_experiments() {
    for f in "$IDEAS_DIR"/developing/*.md; do
        [[ -f "$f" ]] || continue
        local slug
        slug=$(basename "$f" .md)
        if ! grep -rl "$slug" "$DBPULSE_ROOT"/plans/experiments/ >/dev/null 2>&1; then
            _idea_title "$f"
        fi
    done
}
