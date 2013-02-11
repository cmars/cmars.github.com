Improved fulltext search in Hockeypuck
######################################
:date: 2013-02-11 16:30

I've fixed a `full-text search issue`_ in Hockeypuck and deployed to http://keyserver.gazzang.net. Name search is tokenized and case-insensitive, so searches like `'casey marshall'`_ and `'Marshall Casey'`_ will now work.

The fix was easy enough to make and test on a local MongoDB instance, but what about the 3M+ keys on keyserver.gazzang.net? The fulltext search is implemented on MongoDB as an indexed array. Each element of this array would need to be lowercased. And, I improved the tokenization, so really, it would need to be rewritten.

I made a `little MongoDB Javascript`_ patch script that modifies an existing Hockeypuck database with comparable changes, kicked it off late last night. It was done in the morning, so I know it took less than 10 hours. Not bad, Mongo.

I've decided that SKS reconciliation is probably too much work to ship in February with other things I've got going on. I'm going to address smaller issues that have come up in the meantime to deliver a solid `0.9 release`_ for Raring Ringtail.

SKS reconciliation will get a nice, solid 1.0 release number. I'm thinking late March/early April at this point.

.. _`full-text search issue`: https://bugs.launchpad.net/hockeypuck/+bug/1108416
.. _`little MongoDB Javascript`: https://bazaar.launchpad.net/~hockeypuck/hockeypuck/trunk/view/head:/instroot/usr/share/hockeypuck-mgo/scripts/fix-keywords.js
.. _`0.9 release`: https://launchpad.net/hockeypuck/+milestone/0.9
.. _`'casey marshall'`: http://keyserver.gazzang.net/pks/lookup?op=index&search=casey+marshall
.. _`'Marshall Casey'`: http://keyserver.gazzang.net/pks/lookup?op=index&search=Marshall%20Casey
