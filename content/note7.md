Title: GPG the Easy Way
Date: 2025-07-14 12:55
Modified: 2025-07-14 12:55
Category: Crytpography
Tags: gpg, cryptography, linux, command line, encryption 
Slug: gpg-the-easy-way
Authors: Craig Derington
Summary: Use GPG to Encrypt your Private Communications the Easy Way

#### GPG HowTo

Generate a key-pair and answer the prompts

```gpg --gen-key```

To list your public keys:

```gpg --list-keys```

Now, let’s say your name is John Doe, and you want to send a message to Jane Doe. 
This is how you would do it (note that all names used must be the names you see when listing the keys).

First, export your public key:

```gpg --export --armor youremail@example.com > publickey.asc```

Send this file to Jane Doe. Get her to do the same.

To import someone else’s public key:

```gpg --import publickey.asc```

Now that you’ve imported Jane Doe’s key, let’s send her an encrypted message.

To encrypt a file to send to Jane Doe:

```gpg --encrypt --recipient receiversname filename.txt```


```gpg --encrypt --recipient Jane Doe secretmessage.txt```

or, if the previous command doesn’t work:

```gpg -e -u “sender’s name (you)” -r “name of the receiver’s key” filename.txt```

Example:

```gpg -e -u “John Doe” -r “Jane Doe” secretmessage.txt```

This will create a file called secretmessage.txt.pgp. Send this to Jane Doe.

Now Jane has received your file. This is how she decrypts it:

To decrypt to command line (meaning that you’ll only see the message in the command line, and it won’t be saved decrypted to your hard drive):

```gpg --decrypt filename.txt.gpg```

To decrypt to disk:

```gpg filename.txt.gpg```

#### Digital Signatures
##### A digital signature certifies and timestamps a document.

If the document is subsequently modified in any way, a verification of the signature will fail. A digital signature can serve the same purpose as a hand-written signature with the additional benefit of being tamper-resistant.

Creating and verifying signatures uses the public/private keypair in an operation different from encryption and decryption. A signature is created using the private key of the signer. The signature is verified using the corresponding public key.

To sign a document with PGP, run this in the command-line:

```gpg --output document.sig --sign document.pdf```

To verify a document that has been signed with PGP, run this in the command line:

```gpg --output document.pdf --decrypt document.sig```

Create a detached signature file

```gpg --output classifiedinfo.sig --sign /path/to-file/classifiedinfo.docx```

Verify the signature against the document that was signed

```gpg --output classifiedinfo.docx --decrypt /path/to/file/classifiedinfo.sig```

```gpg: Signature made 02/12/2016 15:39:05 Central African Time using DSA key ID A657BC83 gpg: Good signature from "Bob < bob@pgp.com >" ```

##### Create a Digital Signature with a specific private key

```gpg --local-user [fingerprint] --sign --armor --output somefile.tar.xz.asc --detach-sig somefile.tar.xz```


