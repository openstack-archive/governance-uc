=============================
 HOWTO - Running UC Election
=============================

    **User committee elections should be run twice a year, typically in February and August. It is suggested to start the steps within this document at least 60 days before election.**

1. Start by adding a patch to the `governance-uc <https://git.openstack.org/openstack/governance-uc>`_ repository similar to this `patch <https://review.openstack.org/#/c/627575/>`_; **be sure to modify the content like dates and number of seats**.

2. Follow up with an email to the User Committee asking for their action items:

  - Decision: dates - for nomination period and voting period.
  - Writing: Posts to Mailing list to announce the election
  - Selection: Election officials, who don't vote and manage the process in a neutral way (inc setting up the CIVS tools)
  - Action: pull the updated AUC list and make the voting links for all of them
  - Writing: Post-election ML and superuser post to announce the results and declare the UC awesome

Example resources from February 2017 (copy/paste but remember to update):

  - https://governance.openstack.org/uc/reference/uc-election-feb2017.html
  - http://lists.openstack.org/pipermail/openstack-operators/2017-January/012530.html
  - http://superuser.openstack.org/articles/user-committee-elections/
  - https://wiki.openstack.org/wiki/Governance/Foundation/UserCommittee/UC-Election-Feb17
  - http://lists.openstack.org/pipermail/openstack-operators/2017-February/012647.html

3. Send email to `openstack-discuss <openstack-discuss@lists.openstack.org>`_ mailing list asking for election officials

**Remember to note that election officials will not be able to vote or run for the election and are expected to be neutral in managing the process; including setting up the CIVS tools**

Election Officials and Electorate
---------------------------------

An early AUC list should be procured and provided to election inspectors to verify the AUC status of candidates. This can be done by downloading the CSV export from https://www.openstack.org/admin/auc/ (requires Foundation staff access). [Alternately. a system could be implemented that places a 'badge' on Foundation member profiles if a member qualifies for AUC.]

In addition to the CSV export, the UC may provide lists of manually calculated AUC qualifications under their current criteria and process (eg working groups that do not meet on IRC).
*#TODO Reasonable way to collect that is not manual; extra-auc is available but move to SIGs happened after; should revisit.*

A final AUC CSV export, with the list of manual additions, should be provided to the election inspectors just before the start of the voting period. The inspectors will then upload it into the voting system, which sends out the voting links.

Additional Considerations
-------------------------

| **SuperUser Article:**
|
| The Superuser magazine has published articles around the time of the election such as http://superuser.openstack.org/articles/user-committee-elections/. The editable text is available at https://docs.google.com/document/d/14CkEnrI_YLvkzx14JukfxSQcNSYYg0Xwa-yLMks1oJY/edit.

| **Sample eMail Announcement:**
|
| The announcement mail can follow the template below. Sending to `openstack-discuss <openstack-discuss@lists.openstack.org>`_ list is sufficient even though it has been sent in the past to `user-committee <user-committee@lists.openstack.org>`_, `OpenStack Operators <openstack-operators@lists.openstack.org>`_, and `women-of-openstack@lists.openstack.org <women-of-openstack@lists.openstack.org>`_ mailing lists.
|
|

.. note::
  | Hello Everyone,
  |
  | The OpenStack User Committee will be holding an election in February, per the (UC) bylaws and charter.
  | The current UC will serve until the elections in February, and at that point, the current three UC members who still have 6 months to serve get a 6-month seat, and an election is run to determine the other two members. Candidates ranking 1st, and 2nd will get a one-year seat. Voting for the 2018 UC members will be granted to the Active User Contributors (AUC).
  | Open candidacy for the UC positions will be from January 29th - February 11th, 05:59 UTC. Voting for the User Committee (UC) members will be open on February 12th and will remain open until February 18, 11:59 UTC.
  |
  | As a reminder, please see the community code of conduct (http://www.openstack.org/legal/community-code-of-conduct/)
  |
  | The details of candidate submission and process are available at here and we look forward to receiving your submissions
  | Please let me, or anyone from the UC know if you have any questions, comments or concerns.
  |
  | Thank you,
