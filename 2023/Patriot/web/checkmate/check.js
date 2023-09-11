function checkValidity(password) {
    const arr = Array.from(password).map(ok);

    function ok(e) {
        if (e.charCodeAt(0) <= 122 && e.charCodeAt(0) >= 97) {
            return e.charCodeAt(0);
        }
    }

    let sum = 0;
    for (let i = 0; i < arr.length; i += 6) {
        var add = arr[i] & arr[i + 2];
        var or = arr[i + 1] | arr[i + 4];
        var xor = arr[i + 3] ^ arr[i + 5];
        if (add === 0x60 && or === 0x61 && xor === 0x6) sum += add + or - xor;
    }
    return sum === 0xbb ? true : false; // Vous pouvez directement retourner true ou false.
}

function findAllValidPasswords() {
    const validPasswords = [];
    const targetSum = 0xbb; // Somme cible

    for (let i = 0; i <= 25; i++) {
        for (let j = 0; j <= 25; j++) {
            for (let k = 0; k <= 25; k++) {
                for (let l = 0; l <= 25; l++) {
                    for (let m = 0; m <= 25; m++) {
                        for (let n = 0; n <= 25; n++) {
                            const char1 = String.fromCharCode(97 + i);
                            const char2 = String.fromCharCode(97 + j);
                            const char3 = String.fromCharCode(97 + k);
                            const char4 = String.fromCharCode(97 + l);
                            const char5 = String.fromCharCode(97 + m);
                            const char6 = String.fromCharCode(97 + n);
                            const password = char1 + char2 + char3 + char4 + char5 + char6;

                            if (checkValidity(password)) {
                                validPasswords.push(password);
                            }
                        }
                    }
                }
            }
        }
    }

    return validPasswords;
}

const validPasswords = findAllValidPasswords();
console.log(validPasswords);
