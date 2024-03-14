## Macro World

```bash
pip install oletools
olevba invitation.docm
```

On trouve 3 macros et du js obfusqué en extrayant à l'endroit spécifié de la macro.


```bash
unzip invitation.docm > test
grep -r mailform.js
grep: word/vbaProject.bin : fichiers binaires correspondent
```

Un RC4 est utilisé sur le pass.
