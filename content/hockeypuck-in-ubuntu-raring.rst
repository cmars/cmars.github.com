Hockeypuck in Ubuntu Raring
###########################
:date: 2013-02-08 18:00

My Hockeypuck_ project was `accepted into Ubuntu Raring`__ earlier this week. Thanks Dustin_ for sponsoring!

Hockeypuck_ is a PGP_ public key server -- kind of like an open directory
or phonebook for looking up someone's key to verify their digital signatures or encrypt e-mail messages or other files to them. For example, with PGP_, you
could ask a keyserver the public key for my email address.

(The name "PGP" was trademarked at some point, so we should really say "OpenPGP", because that is the name of the open standard. And GnuPG, or "GPG", is the free and open-source program that you'll probably end up using to "do PGP".)

A search for my key in Hockeypuck_ looks like this:
https://hockeypuck.gazzang.net/pks/lookup?op=vindex&search=0x44A2D1DB. On other keyservers, such as SKS, it looks like this: http://keyserver.ubuntu.com/pks/lookup?op=vindex&search=0x44A2D1DB.

Before the public key fingerprint linked above, you need to confirm that the key is actually owned by me. There are many ways to do this, but one of the simplest would be to send me a test encrypted mail, and then confirm it with me through some other means (a second factor). Asking me in-person or via phone call to confirm the contents (a good joke would work) would give you confidence that I am the owner of the key.

It might be surprising to find that there is no approval process for submitting a key to a public key server like Hockeypuck_ -- anyone may do it, anytime. In fact, anyone may register any name or email address they want! There is no account to create, no password to log on. The key itself contains some proof that whomever made it can decrypt messages, but that's it. Keys are authenticated by other keys vouching for their authenticity -- by digitally signing them. However, there is some certainty you can depend on. One cannot forge the fingerprint (a unique string) of a key or signatures made by a key -- that is protected by the strong encryption. Once a key is created, only the owner of the private part of that key can modify it, or sign with it.

It seems dangerous and reckless that anyone can register a key, using whatever name and address. Yet at the same time, it is refreshing in this age of Facebook and other corporate curated social networks. Cryptographically-protected confidential social networking is there for those who can wield it responsibly. When communicating and collaborating online, whom else could people from all over the world really trust, but... each other?

The global pool of public keys is fascinating. There are over 4GB of public keys and signatures that have been created and shared. Some of the names and addresses appear personal, others corporate, government, academic or military. There are mysterious pseudonyms, signed snippets of identifiers that aren't even email addresses. Any of them could be real or forgeries, without being introduced to their owners through some other means. Some may be active, others long abandoned. In many cases, the original key creator has lost the secret, private key that would be necessary in order to receive a confidential message with it.

It is like what you might get if Wikipedia made a phone book.

Besides email, OpenPGP is used in many other applications.
The software packages in a Linux distribution such as Ubuntu or
RedHat are certified as officially packaged by their authors or maintainers using
these same type of signatures. When you update packages on such a Linux installation, a PGP keyserver would be queried to obtain the keys used to sign these packages. What else could a vast global, distributed volunteer development effort use to certify software packages?

The significance of software such as Hockeypuck_ going into
Ubuntu is that it has been accepted into the community-curated
collection of software known as "Ubuntu" -- meaning that it is
considered relevant enough, and of sufficient quality to become a part
of this collection. As a PGP keyserver, Hockeypuck_ may one day support this community's collaboration, through the distribution of public keys. That would be an honor :)

.. _Dustin: http://blog.dustinkirkland.com
.. _Hockeypuck: https://launchpad.net/hockeypuck
.. _PGP: https://en.wikipedia.org/wiki/Pretty_Good_Privacy
__ https://launchpad.net/ubuntu/raring/+source/hockeypuck
