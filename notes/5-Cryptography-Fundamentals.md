 # Cryptography Fundamentals 

Cryptography is the practice and study of techniques for secure communication in the presence of third parties. It's a critical component of information security and plays a vital role in protecting data confidentiality, integrity, and authenticity. In this section, we will cover the basics of cryptography and explore various concepts, including symmetric key cryptography, asymmetric key cryptography, hashing functions, public key infrastructure (PKI), digital signatures, and certificates.

## Cryptography Basic Concepts 

### What is Cryptography?

Cryptography is the art of encoding information to prevent unauthorized access. It enables secure communication between parties by converting plain text into ciphertext that can only be deciphered with a specific key or algorithm. In today's digital world, cryptography is essential for securing sensitive data and communications, such as online transactions, email, and file transfers.

### Encryption vs. Decryption

Encryption is the process of converting plain text into ciphertext using an encryption algorithm and a secret key, while decryption is the reverse process that transforms ciphertext back to its original plain text using the same encryption algorithm and a valid decryption key.

### Confidentiality vs. Integrity

Confidentiality ensures that information remains private, as only authorized parties can decrypt and access the data. Integrity guarantees that the data has not been modified during transmission or storage.

## Symmetric Key Cryptography 

### Definition

Symmetric key cryptography, also known as secret-key cryptography or symmetric algorithms, is a method where both the sender and receiver use the same secret key for encryption and decryption. It offers fast encryption and decryption speeds but poses challenges regarding secure key exchange.

### Example: Advanced Encryption Standard (AES)

Advanced Encryption Standard (AES), a widely used symmetric encryption algorithm, supports various key sizes (128, 192, or 256 bits). Data is divided into blocks and transformed through multiple rounds of substitution and permutation using the secret key.

## Asymmetric Key Cryptography 

### Definition

Asymmetric key cryptography, also known as public-key cryptography or asymmetric algorithms, utilizes different keys for encryption (public key) and decryption (private key). Public keys are openly shared, while private keys remain confidential. This design simplifies the process of securely exchanging keys between parties.

### Example: RSA Encryption

RSA is an asymmetric encryption algorithm based on the multiplicative properties of large prime numbers. It uses two keys: a public key for encryption and a private key for decryption. The security of RSA relies on the difficulty of factoring large prime numbers.

## Hashing Functions 

### Definition

Hashing functions take an input, called a message, and produce a fixed-length output or hash value. These functions are designed to be irreversible and fast, ensuring that even small modifications to the input result in significant differences in the output. Hashing functions are essential for verifying data integrity and password security.

### Example: SHA-256

SHA-256 is a widely used hash function from the Secure Hash Algorithm (SHA) family. It converts data into a 256-bit hash value, making it computationally infeasible to generate the same hash value from different inputs or modify the input while preserving its original hash value.

## Public Key Infrastructure (PKI) 

### Definition

Public Key Infrastructure (PKI) is a collection of hardware, software, people, policies, and procedures used to create, manage, distribute, use, store, and revoke digital certificates. It enables secure communication over public networks by establishing trust relationships between parties through the exchange of digital certificates.

### Example: SSL/TLS Certificates

Secure Sockets Layer (SSL) and its successor Transport Layer Security (TLS) are cryptographic protocols providing communication security over computer networks. Websites use SSL/TLS certificates to encrypt data and authenticate the server's identity during client-server communication.

## Digital Signatures 

### Definition

Digital signatures provide authentication, ensuring that a message or file originated from the claimed sender and has not been tampered with during transmission. They employ asymmetric key cryptography, where the sender uses their private key to sign a message, and the recipient uses the sender's public key to verify it.

### Example: Email Signing

Email signing involves creating a digital signature for an email using your private key and attaching it to the message or appending it as a PGP attachment. The recipient can then use your public key to validate the signature, ensuring that the content remains unaltered during transmission.

## Certificates 

### Definition

Certificates are digitally signed documents containing information about an entity (typically a website or individual) and its corresponding public key. They serve as proof of identity and authenticity and are issued by trusted third-party entities called Certificate Authorities (CAs).

### Example: Browser Certificates

Browser certificates, such as those used in SSL/TLS connections, are stored in the operating system's trust store or a user's web browser. They establish secure communication between the client and server by verifying the website's identity through the certificate, allowing encrypted data transmission.