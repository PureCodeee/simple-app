#!/usr/bin/env bash

set -euo pipefail

LOG_FILE="server-info.log"

show_help() {
cat <<EOF
Usage:
    server-info.sh [URL...]

Examples:
    server-info.sh
    server-info.sh http://localhost:5000/health
EOF
}

log() {
    echo "[$(date '+%F %T')] $1" | tee -a "$LOG_FILE"
}

check_dependency() {
    if ! command -v "$1" >/dev/null 2>&1; then
        log "[WARN] $1 is not installed."
        return 1
    fi
}

print_header() {
    echo "=== Server Diagnostics ==="
    echo "Date:     $(date)"
}

print_system_info() {
    echo
    echo "=== System ==="
    echo "Hostname: $(hostname)"
    echo "Kernel:   $(uname -r)"
    echo "OS:       $(grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')"
    echo "Uptime:   $(uptime -p)"
}

print_resources() {
    echo
    echo "=== Resources ==="
    echo "CPU cores: $(nproc)"
    free -h
    echo
    df -h /
}

print_docker() {
    echo
    echo "=== Docker ==="

    if command -v docker >/dev/null 2>&1; then
        docker ps || true
    else
        echo "Docker is not installed."
    fi
}

check_services() {
    local failed=0

    if [ "$#" -eq 0 ]; then
        return
    fi

    echo
    echo "=== Service Health Checks ==="

    for url in "$@"; do
        if curl -fs "$url" >/dev/null; then
            echo "[OK]   $url"
        else
            echo "[FAIL] $url"
            failed=1
        fi
    done

    return "$failed"
}

main() {

    if [[ "${1:-}" == "--help" ]]; then
        show_help
        exit 0
    fi

    : > "$LOG_FILE"

    check_dependency curl || true
    check_dependency docker || true

    print_header | tee -a "$LOG_FILE"
    print_system_info | tee -a "$LOG_FILE"
    print_resources | tee -a "$LOG_FILE"
    print_docker | tee -a "$LOG_FILE"

    if ! check_services "$@" | tee -a "$LOG_FILE"; then
        exit 1
    fi
}

main "$@"