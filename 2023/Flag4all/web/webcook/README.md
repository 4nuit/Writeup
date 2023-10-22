## Sol

```bash
token=$(curl -v webcook 2>&1 | grep -o 'Set-Cookie: session=.*' | awk -F= '{print $2}' | awk -F';' '{print $1}')
curl -X POST -d "answer=b1fee1d5fe5e03b8d8bccf115cbbc94a" -b "session=$token" http://webcook/check_answer
```
