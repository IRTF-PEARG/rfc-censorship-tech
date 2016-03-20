# draft-hall-censorship-tech

This is the working area for the draft of [draft-hall-censorship-tech](https://datatracker.ietf.org/doc/draft-hall-censorship-tech/).

## Contributing

Be aware that all contributions to this document fall under the "NOTE
WELL" terms outlined below.

1. The best way to provide feedback (editorial or design) and ask
questions is sending an e-mail to draft-hall-censorship-tech@ietf.org.
This will ensure that all authors see your input in a timely fashion.

2. If you have **editorial** suggestions (i.e., those that do not
change the meaning of the document), you can either:

  * Fork this repository and [submit a pull
  request](https://help.github.com/articles/fork-a-repo/); this is the
  lowest friction way to get editorial changes in.

  * Submit a new issue to Github, and mention that you believe it is
  editorial in the issue body. It is not necessary to notify the
  mailing list for editorial issues.

  * Make comments on individual commits in Github. Note that this
  feedback is processed only with best effort by the editors, so it
  should only be used for quick editorial suggestions or questions.

3. For non-editorial (i.e., **design**) issues, you can also create an
issue on Github. However, you **must notify the mailing list above**
when creating such issues, providing a link to the issue in the
message body.

  Note that **github issues are not for substantial discussions**; the
  only appropriate place to discuss design issues is on the mailing
  list itself.


## Building the Draft

In order to build a copy of the draft, you will need to install
xml2rfc.  This requires Python 2.7 and can be installed using `pip`:

```sh
$ pip install xml2rfc
```

(Note: if you don't have `pip` you can get it rather easily via `sudo
easy_install pip`.)

You may also need to install kramdown-xml2rfc, which requires Ruby and
can be installed using the ruby package manager, `gem`:

```sh
$ gem install kramdown-rfc2629
```

At this point, you should be able to build the draft with the
following commands:

```sh
$ make draft-hall-censorship-tech-latest.txt
$ make draft-hall-censorship-tech-latest.xml
```

Other tools can be used to produce PDF files, or to provide a
comparison.  These tools - and where to find them - are described in
the `Makefile` courtesy of Martin Thompson's [I-D
Template](https://github.com/martinthomson/i-d-template).


## NOTE WELL

Any submission to the [IETF](https://www.ietf.org/) intended by the
Contributor for publication as all or part of an IETF Internet-Draft
or RFC and any statement made within the context of an IETF activity
is considered an "IETF Contribution". Such statements include oral
statements in IETF sessions, as well as written and electronic
communications made at any time or place, which are addressed to:

 * The IETF plenary session
 * The IESG, or any member thereof on behalf of the IESG
 * Any IETF mailing list, including the IETF list itself, any working group
   or design team list, or any other list functioning under IETF auspices
 * Any IETF working group or portion thereof
 * Any Birds of a Feather (BOF) session
 * The IAB or any member thereof on behalf of the IAB
 * The RFC Editor or the Internet-Drafts function
 * All IETF Contributions are subject to the rules of
   [RFC 5378](https://tools.ietf.org/html/rfc5378) and
   [RFC 3979](https://tools.ietf.org/html/rfc3979)
   (updated by [RFC 4879](https://tools.ietf.org/html/rfc4879)).

Statements made outside of an IETF session, mailing list or other
function, that are clearly not intended to be input to an IETF
activity, group or function, are not IETF Contributions in the context
of this notice.

Please consult [RFC 5378](https://tools.ietf.org/html/rfc5378) and
[RFC 3979](https://tools.ietf.org/html/rfc3979) for details.

A participant in any IETF activity is deemed to accept all IETF rules
of process, as documented in Best Current Practices RFCs and IESG
Statements.

A participant in any IETF activity acknowledges that written, audio
and video records of meetings may be made and may be available to the
public.
