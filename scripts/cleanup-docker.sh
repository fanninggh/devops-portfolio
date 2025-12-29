#!/bin/bash

# Script: Docker Cleanup Utility
# Description: Removes unused Docker images, containers, and volumes
# Usage: ./cleanup-docker.sh [--all]

set -e

echo "🐳 Docker Cleanup Utility"
echo "------------------------"

if [ "$1" = "--all" ]; then
    echo "Removing all unused Docker resources..."
    docker system prune -a -f
    echo "✅ All unused resources removed."
else
    echo "Removing dangling images..."
    docker image prune -f
    
    echo "Removing stopped containers..."
    docker container prune -f
    
    echo "Removing unused volumes..."
    docker volume prune -f
    
    echo "✅ Cleanup completed (basic)."
fi

# Show current disk usage
echo ""
echo "📊 Current Docker disk usage:"
docker system df
