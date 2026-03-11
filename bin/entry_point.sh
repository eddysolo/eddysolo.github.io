#!/bin/bash
set -euo pipefail

echo "Entry point script running"

CONFIG_FILE=_config.yml
DEV_DESTINATION=/tmp/jekyll-site

ensure_writable_dir() {
    local dir="$1"

    mkdir -p "$dir" 2>/dev/null || true

    if [ -e "$dir" ] && [ ! -w "$dir" ]; then
        echo "Directory '$dir' is not writable by $(id -un). Attempting ownership fix..."

        if command -v sudo &> /dev/null && sudo -n true 2>/dev/null; then
            sudo chown -R "$(id -u):$(id -g)" "$dir" 2>/dev/null || true
        fi
    fi

    if [ -e "$dir" ] && [ ! -w "$dir" ]; then
        echo "Warning: '$dir' is still not writable. Falling back away from repository output/cache for this run."
        return 1
    fi

    return 0
}

# Function to manage Gemfile.lock
manage_gemfile_lock() {
    git config --global --add safe.directory '*'
    if command -v git &> /dev/null && [ -f Gemfile.lock ]; then
        if git ls-files --error-unmatch Gemfile.lock &> /dev/null; then
            echo "Gemfile.lock is tracked by git, keeping it intact"
            git restore Gemfile.lock 2>/dev/null || true
        else
            echo "Gemfile.lock is not tracked by git, removing it"
            rm Gemfile.lock
        fi
    fi
}

start_jekyll() {
    manage_gemfile_lock

    local extra_args=()

    # Keep development output outside the repository to avoid cross-tool ownership conflicts.
    extra_args+=(--destination="$DEV_DESTINATION")

    if ! ensure_writable_dir .jekyll-cache; then
        extra_args+=(--disable-disk-cache)
    fi

    if ! ensure_writable_dir "$DEV_DESTINATION"; then
        echo "Failed to prepare writable destination '$DEV_DESTINATION'."
        exit 1
    fi

    bundle exec jekyll serve --watch --port=8080 --host=0.0.0.0 --livereload --verbose --trace --force_polling "${extra_args[@]}" &
}

start_jekyll

while true; do
    inotifywait -q -e modify,move,create,delete $CONFIG_FILE
    if [ $? -eq 0 ]; then
        echo "Change detected to $CONFIG_FILE, restarting Jekyll"
        jekyll_pid=$(pgrep -f jekyll)
        kill -KILL $jekyll_pid
        start_jekyll
    fi
done
