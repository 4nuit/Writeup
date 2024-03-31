## APK 1/2

On utilise **jadx-gui** et https://appetize.io

Le `AndroidManifest.xml` lance directement le main avec LAUNCHER:

```xml
   <activity android:name="com.hsr.paranoidandroid.MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
```

`onCreate` appelle le Main qui vérifie si le sha256 du mot de passe est correct:

```java
    public /* synthetic */ void m143lambda$onCreate$0$comhsrparanoidandroidMainActivity(EditText passwordEditText, View view) {
        String password = passwordEditText.getText().toString();
        try {
            if (sha256(password).equals("8479e87382ed107fcf53a247914112a62ba57bc5ab25b05b89436d1e718bcf12")) {
                Toast.makeText(this, getResources().getString(R.string.flag1) + getResources().getString(R.string.flag2) + getResources().getString(R.string.flag3) + getResources().getString(R.string.flag4) + getResources().getString(R.string.flag5), 0).show();
            } else {
                Toast.makeText(this, "Fail", 0).show();
            }
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
```

N'arrivant pas à le casser, on peut tout simplement inspecter les R-String formant le flag à afficher.
Pour cela sélectionner `Navigation -> Text Search ,cocher "Resources"` et rechercher `flag1`:

Tout simplement, dans `res/values/strings.xml`:
```xml
   <string name="flag1">HSR{</string>
    <string name="flag2">l0w_h</string>
    <string name="flag3">anging_fruit</string>
    <string name="flag4">s_in_str</string>
    <string name="flag5">ings}</string>
```

## APK 2/2

L'application est en tout point similaire mais utilise cette fois un (dé)chiffrement **AES-ECB** si le SHA256 est correct.

```java
   public /* synthetic */ void m49lambda$onCreate$0$comexampleparanoidandroid2MainActivity(EditText passwordEditText, View view) {
        String password = passwordEditText.getText().toString();
        try {
            if (sha256(password).equals("8479e87382ed107fcf53a247914112a62ba57bc5ab25b05b89436d1e718bcf12")) {
                Toast.makeText(this, d("rkU/dVyLx9Uy0YPhcikatdACBEioM11yjNQvG/nAmls=", K()), 0).show();
            } else {
                Toast.makeText(this, "Fail", 0).show();
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static String d(String input, String key) throws Exception {
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(2, secretKeySpec);
        byte[] decodedBytes = Base64.decode(input, 0);
        byte[] decryptedBytes = cipher.doFinal(decodedBytes);
        return new String(decryptedBytes);
    }
```

On dispose du chiffré en base64 à décoder , et de la clé `K()` chargée à partir d'une bibliothèque native, chargée dynamiquement à l'éxécution du programme:

```java
public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;

    public native String K();

    static {
        System.loadLibrary("paranoidandroid2");
    }
....
}
```

On ouvre alors dans Ghidra une version de cette lib (shared object), code C chargée à partir de la **Java Native Interface**:

```bash
┌─[night@night-20b7s2ex01]─[~/hsr/reverse/ParanoidAndroid2/resources]
└──╼ 10 fichiers, 9,9Mb)─$ ls -R lib/
lib/:
arm64-v8a  armeabi-v7a  x86  x86_64

lib/arm64-v8a:
libparanoidandroid2.so

lib/armeabi-v7a:
libparanoidandroid2.so

lib/x86:
libparanoidandroid2.so

lib/x86_64:
libparanoidandroid2.so
```

Et voici donc la clé:

```c

undefined8 Java_com_example_paranoidandroid2_MainActivity_K(_JNIEnv *param_1)

{
  long lVar1;
  char *pcVar2;
  undefined8 uVar3;
  basic_string<> abStack_30 [24];
  long local_18;
  
  lVar1 = tpidr_el0;
  local_18 = *(long *)(lVar1 + 0x28);
  std::__ndk1::basic_string<>::basic_string<>(abStack_30,"OMGth3k3ySOs3cr3T!!plzNoShare:((");
  pcVar2 = (char *)FUN_0011dcac(abStack_30);
                    /* try { // try from 0011db9c to 0011db9f has its CatchHandler @ 0011dbd8 */
  uVar3 = _JNIEnv::NewStringUTF(param_1,pcVar2);
  std::__ndk1::basic_string<>::~basic_string(abStack_30);
  lVar1 = tpidr_el0;
  lVar1 = *(long *)(lVar1 + 0x28) - local_18;
  if (lVar1 == 0) {
    return uVar3;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(lVar1);
}
```

Plus qu'à déchiffrer le flag:

```python
from Crypto.Cipher import AES
from base64 import b64decode

ct =b64decode(b"rkU/dVyLx9Uy0YPhcikatdACBEioM11yjNQvG/nAmls=")
key = b"OMGth3k3ySOs3cr3T!!plzNoShare:(("
cipher = AES.new(key, AES.MODE_ECB)
pt= cipher.decrypt(ct)

print(pt)
```

`HSR{dont_forget_JNI!}`
