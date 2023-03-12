#include <iostream>
#include <fstream>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <vector>

void sign(const BIGNUM *m, const BIGNUM *e, const BIGNUM *n, BIGNUM *s){
  BN_CTX* ctx = BN_CTX_new();
  BIGNUM* temp = BN_new();
  BN_mod_exp(temp, m, e, n, ctx);
  BN_copy(s, temp);
  BN_free(temp);
  BN_CTX_free(ctx);
}

int main(int argc,char ** argv) {
  if (argc < 2 || argc > 4) {
    std::cerr << "Usage of" << argv[0] << std::endl;
    std::cerr << "Sign message: " << argv[0] << " <hex>message" << std::endl;
    std::cerr << "Verify signature: " << argv[0] << " <hex>message <hex>signature" << std::endl;
    return 1;
  }
  const std::string privateKeyPath = "private.key";
  const std::string publicKeyPath = "public.key";
  const std::string previousSignedMessage = "signedHist.txt";
  BIGNUM *m = BN_new();
  BIGNUM *e = BN_new();
  BIGNUM *d = BN_new();
  BIGNUM *n = BN_new();
  BIGNUM *s = BN_new();
  retrieveRSAKey(privateKeyPath, true, d, n);
  retrieveRSAKey(publicKeyPath, false, e, n);
  const char * plaintext_str = argv[1];
  BN_hex2bn(&m, plaintext_str);
  sign(m, d, n, s);
  if (argc == 3) {
    BIGNUM *v = BN_new();
    BIGNUM *si = BN_new();
    const char * singedPlaintext_str = argv[2];
    BN_hex2bn(&si, singedPlaintext_str);
    sign(si, e, n, v);
    std::vector<BIGNUM*> previousSinged_vector = readBignumsFromFile(previousSignedMessage);
    bool isPrensent = isBignumInFile(si, previousSignedMessage);
    if (isBignumEqual(s, v)) {
      std::cout << "This is a valid singature for message: " << plaintext_str << std::endl;
    } else {
      std::cout << "This is not a valid singature for message: " << plaintext_str << std::endl;
    }
    if (isPrensent){
      std::cout << "Message already submited" << std::endl;
      exit(0);
    }

    if (!isPrensent && isBignumEqual(s, si)) {
      std::cout << "Great, here's your flag:" << std::endl;
      getFlag();
    } 
    BN_free(v);
    BN_free(si);
  }else {
      writeBignumToFile(s, previousSignedMessage);
      std::cout << "Singed message: " << BN_bn2hex(s) << std::endl;
  }
  BN_free(e);
  BN_free(d);
  BN_free(n);
  BN_free(m);
  BN_free(s);
  return 0;
}

