#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Interface for Attack Surface Management Tool
Developer: SayerLinux
Email: SaudiLinux1@gmail.com
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime
from attack_surface_manager import AttackSurfaceManager
import threading
import time

app = Flask(__name__)

# Global variables to store scan results and status
scan_results = {}
scan_status = "idle"
current_scan = None
scan_progress = 0
scan_logs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def start_scan():
    global scan_status, scan_results, current_scan, scan_progress, scan_logs
    
    target_url = request.form.get('target_url')
    scan_type = request.form.get('scan_type', 'stealth')  # stealth or normal
    
    if not target_url:
        return jsonify({'error': 'Target URL is required'}), 400
    
    scan_status = "scanning"
    scan_progress = 0
    scan_logs = []
    
    def run_scan():
        global scan_status, scan_results, scan_progress, scan_logs
        try:
            scanner = AttackSurfaceManager(target_url)
            
            # Add logging function
            def log_progress(message):
                global scan_logs
                timestamp = datetime.now().strftime('%H:%M:%S')
                scan_logs.append(f"[{timestamp}] {message}")
            
            # Override the print function in scanner to capture logs
            scanner.log_function = log_progress
            
            if scan_type == 'stealth':
                log_progress("🎭 بدء فحص التخفي المتقدم...")
                scan_results = scanner.run_stealth_scan()
            else:
                log_progress("🔍 بدء الفحص العادي...")
                scan_results = scanner.run_comprehensive_scan()
            
            scan_status = "completed"
            log_progress("✅ تم إكمال الفحص بنجاح")
            
        except Exception as e:
            scan_status = "failed"
            scan_results = {'error': str(e)}
            log_progress(f"❌ فشل الفحص: {str(e)}")
    
    # Start scan in background thread
    scan_thread = threading.Thread(target=run_scan)
    scan_thread.start()
    
    return jsonify({'status': 'Scan started', 'target': target_url, 'scan_type': scan_type})

@app.route('/status')
def get_status():
    return jsonify({
        'status': scan_status,
        'progress': scan_progress,
        'logs': scan_logs[-20:],  # Last 20 log entries
        'results': scan_results if scan_status == 'completed' else None
    })

@app.route('/reports')
def list_reports():
    reports = []
    for file in os.listdir('.'):
        if file.startswith('security_report_') and file.endswith('.json'):
            reports.append({
                'filename': file,
                'date': file.replace('security_report_', '').replace('.json', '')
            })
    return render_template('reports.html', reports=reports)

@app.route('/report/<filename>')
def view_report(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            report = json.load(f)
        return render_template('report_detail.html', report=report)
    except FileNotFoundError:
        return "Report not found", 404

@app.route('/api/vulnerabilities')
def api_vulnerabilities():
    if scan_status == 'completed' and scan_results:
        return jsonify(scan_results.get('vulnerabilities', []))
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)