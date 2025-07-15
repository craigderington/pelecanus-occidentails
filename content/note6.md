Title: Encrypt a Single File in Linux with OpenSSL
Date: 2025-07-14 09:55
Modified: 2025-07-14 09:55
Category: Linux
Tags: linux, command line, useful commands, openssl, encryption, decryption
Slug: encrypt-a-single-file-in-ubuntu-with-openssl
Authors: Craig Derington
Summary: How to encrypt a single file in Linux using OpenSSL

#### ENCRYPT SINGLE FILE
Encrypting a Single File in Ubuntu

Encrypt:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
openssl aes-256-cdc < yourfile.txt > yourfile.txt.asc

openssl enc -d -aes-256-cbc -pass pass:the-encrypted-files-passphrase -p -in yourfile.txt -out yourfile.enc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, use -in and -out for your input and output file instead of < and >

This will prompt you for a passphrase, which you will need to enter later when decrypting the file.

Decrypt:


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
openssl aes-256-cdc -d < yourfile.txt.asc > yourfile.txt.decrypted

openssl enc -aes-256-cbc -pass pass:the-encrypted-files-passphrase -d -in yourfile.enc -out yourfile.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
