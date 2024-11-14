// import { bitcoin } from 'bitcoinjs-lib/src/networks';
//bs58
//bs64
//bs128

const bitcoin = require('bitcoinjs-lib');
const base58 = require('bs58');

const publicKeyHex = "0224d93bd9418ad1a295662b693ced26f0b98cf5ab6f9af1c794da6d06ebc3d7bc";
const expectedAddress = "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9";
const publicKeyBuffer = Buffer.from(publicKeyHex, 'hex');


function generateAddress(pubKeyBuffer) {
    const { address } = bitcoin.payments.p2pkh({ pubkey: pubKeyBuffer });
    return address;
}

function bruteForce() {
    let attempts = 0;
    let addressFound = false;

    while (!addressFound) {
        attempts++;
        const address = generateAddress(publicKeyBuffer);
        
        if (address === expectedAddress) {
            addressFound = true;
            console.log(`Alamat ditemukan setelah ${attempts} percobaan: ${address}`);
        }

        if (attempts >= 100000) {
            console.log('Tidak dapat menemukan alamat setelah 100000 percobaan.');
            break;
        }
    }
}

bruteForce();
