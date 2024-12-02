run_script() {
    script_name=$1
    log "Starting $(basename "$script_name" .sh)"
    sh $script_name
    if [ $? -ne 0 ]; then
        log "Error: $script_name failed"
        exit 1
    fi
    log "$script_name completed successfully"
}
