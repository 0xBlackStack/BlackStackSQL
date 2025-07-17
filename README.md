# 🛡️ BlackStackSQL

**Advanced Python-based SQL Injection Automation Tool**
Terminal-first. Modular. Obfuscated. Legal. Powerful.

---

## 🚀 Features

- ✅ GET/POST/Cookie SQL injection detection
- ✅ Union-based, error-based, boolean/time blind
- ✅ Auto DBMS detection (MySQL, MSSQL, etc.)
- ✅ WAF evasion, form crawling, payload obfuscation
- ✅ Multi-threaded & session-based scanning
- ✅ Export results as .txt / .json / .csv

---

## 📂 Folder Structure

```
blackstacksql/
├── core/         # Injection engine, DBMS detector
├── modules/      # Dumper, WAF bypass, admin finder
├── utils/         # Logger, encoder, proxy manager
├── ui/            # CLI interface
├── payloads/      # All SQLi payloads
├── sessions/      # Session logs and data
├── main.py         # Entry point
├── setup.py        # Installer
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/0xBlackStack/blackstacksql.git
cd blackstacksql
python setup.py install
```

---

## 📈 Usage Examples

```bash
python3 main.py --url http://target.com?id=1 --scan
python3 main.py --url http://site.com/page.php --dump --columns users,password
python3 main.py --form --waf-bypass --save-json
```

---

## 🎛 CLI Flags

| Flag         | Description                          |
|--------------|--------------------------------------|
| `--url`      | Target URL to scan                  |
| `--scan`     | Detection-only mode                  |
| `--dump`     | Dump DB structure and data           |
| `--columns`  | Dump specific columns               |
| `--form`     | Scan HTML forms                      |
| `--proxy`    | Use proxy from file or Tor           |
| `--cookie`   | Send cookies with request            |
| `--header`   | Add custom headers                  |
| `--waf-bypass` | Enable payload evasions             |
| `--resume`   | Resume previous session             |
| `--save-json` | Save results in JSON                |
| `--html-log` | Save report as HTML                  |

---

## 🤝 Contributing

PRs welcome. Create new modules in `/modules/`, add payloads in `/payloads/`, or improve the CLI.

---

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized penetration testing purposes only.
The developer is not responsible for misuse or illegal activity.

---

## 📜 License

MIT License © 2025 - BlackStackSQL Team
