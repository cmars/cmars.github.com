Now with GnuPG signage
######################
:date: 2013-02-09 19:26

When I publish my blog to Github, I create new post files, make whatever changes, and then I use a Makefile that the pelican-quickstart generated for me: ``make html serve`` to compile the site and view on localhost:8000, ``make github`` to publish on Github.

This evening I added GnuPG_ signatures to all my posts. Each HTML page now has a detached signature. So, for example, to get the detached signature for this page, you'd fetch https://cmars.github.com/now-with-gnupg-signage.html.sig.

Right now, it's not very easy to verify these signatures. Your browser doesn't know how to check them yet. You'd have to save them separately and use GnuPG_ to verify them. Save this HTML page, then save the .sig file, then do ``gpg --verify now-with-gnupg-signage.html.sig now-with-gnupg-signage.html``. I don't expect anyone to go to all this trouble under normal circumstances.

Still, I think PGP-signing content is interesting and profound and relevant as the web and new applications for it evolve. Take this Github hosting arrangement I have. You're reading a blog that is hosted in what is essentially a `distributed version control`_ system (DVCS), git_. With git_, anyone can clone this entire site and host it themselves. You could pull my blog updates with git directly and view them locally, instead of reading them off of Github's web servers (like you're probably doing now).

Now, let's imagine there is a distributed social networking platform -- like Facebook or Twitter, but instead of being hosted and controlled by a single company, it is a mesh of content that gets synchronized between your devices. Perhaps you are tired of Facebook privacy changes, `location tracking`_, etc. and you would like to share with your family and friends without creepy corporations harvesting and selling your data and habits. Fair enough... let's say the problem of copying all these baby and kitty pictures, funny links, meetups, drama and jokes all around are technically solved and you can share content like this. Let's even assume that the app is cute enough and easy enough to use, that mainstream users adopt it. You would have this problem of authenticity -- how can you know who really sent what? If such a system became popular enough to have some trusting users, someone would figure out how to 'shop a photo in the application's storage, and create some shenanigans. This creates lulz for some, hurt feelings for others, distrust for all, and pretty soon your family and friends go back to Facebook.

But, if this "sharing app" made cryptographic signatures -- signatures much like the ones I've created on my posts -- and the app could check them -- well, then you could prevent this kind of tampering.

This is how I envision making PGP more usable. Keys are exchanged in person, typically on mobile devices, very easily. Content is signed, optionally encrypted, and no one gets to snoop, forge content, or exploit people going about their daily lives. Some ideas I have, I want to make money with, but this, I believe it should just *exist*, whether or not I profit from it. It is more of creating a world in which I want to live.

Yeah, they're a pain in the ass to check right now, but my blog has digital signatures. Copying not only permitted, but encouraged.

.. _`location tracking`: http://arstechnica.com/business/2013/02/facebook-may-create-a-passive-location-logging-app/
.. _GnuPG: http://www.gnupg.org/
.. _`distributed version control`: https://en.wikipedia.org/wiki/Distributed_revision_control
.. _git: http://git-scm.com/
