#!/usr/bin/env python3
"""
DevOps Log Monitor
Simulates log monitoring and alerting
"""

import re
from datetime import datetime
import sys

def analyze_logs(log_file_path, error_pattern=r'ERROR|FAILED|CRITICAL'):
    """
    Analyze logs for error patterns
    """
    error_count = 0
    errors_found = []
    
    try:
        with open(log_file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if re.search(error_pattern, line, re.IGNORECASE):
                    error_count += 1
                    errors_found.append({
                        'line': line_num,
                        'content': line.strip(),
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                    
        # Print report
        print(f"📊 Log Analysis Report")
        print(f"   File: {log_file_path}")
        print(f"   Scan time: {datetime.now()}")
        print(f"   Total errors found: {error_count}")
        
        if errors_found:
            print("\n⚠️  Errors detected:")
            for err in errors_found[:5]:  # Show first 5 errors
                print(f"   Line {err['line']}: {err['content']}")
            
            # If high errors, "alert"
            if error_count > 10:
                print(f"\n🚨 ALERT: High error count ({error_count}) detected!")
                return False  # Pipeline would fail here
        else:
            print("✅ No critical errors found.")
            
        return True
        
    except FileNotFoundError:
        print(f"❌ Log file not found: {log_file_path}")
        return False

def create_sample_log():
    """Create a sample log file for testing"""
    sample_logs = [
        "2024-01-15 10:00:00 INFO Application started successfully",
        "2024-01-15 10:00:05 INFO Database connection established",
        "2024-01-15 10:00:10 ERROR Failed to connect to Redis cache",
        "2024-01-15 10:00:15 WARNING High memory usage detected",
        "2024-01-15 10:00:20 INFO User login successful",
        "2024-01-15 10:00:25 CRITICAL Payment service timeout",
        "2024-01-15 10:00:30 INFO Request processed in 150ms",
        "2024-01-15 10:00:35 ERROR File not found: /var/www/config.json",
        "2024-01-15 10:00:40 INFO Backup completed",
        "2024-01-15 10:00:45 FAILED Email notification service unavailable"
    ]
    
    with open('sample_app.log', 'w') as f:
        f.write('\n'.join(sample_logs))
    
    print("📝 Created sample log file: sample_app.log")
    return 'sample_app.log'

if __name__ == "__main__":
    # If no log file provided, create and analyze sample
    if len(sys.argv) < 2:
        print("No log file provided. Creating sample...")
        log_file = create_sample_log()
    else:
        log_file = sys.argv[1]
    
    # Analyze the logs
    success = analyze_logs(log_file)
    
    # Exit code for CI/CD pipeline
    sys.exit(0 if success else 1)
