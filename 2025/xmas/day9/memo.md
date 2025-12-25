In two steps:

Use `bkcrack` with a known plaintext on the zip file. A png in it was in `store` format (not (compressed + encrypted))

Use `exiftool -all *` and `steghide` to extract flag.txt
