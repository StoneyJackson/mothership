## Solution Strategies

I'm currently leaning towards

### Hosted GitLab - Index Repository

- Create a group for foss2serve
- Create a single index-repository to hold URLs to other repositories
- Authors publish their repository by forking the index-repository, add URL, and issue merge request.

_Advantages_

- Hosted
  - No setup
  - No maintenance of the underlying software
- Simple model
  - One repository to rule them all
  - Uses standard contribution model to publish
  - Finding a repository amounts to searching through the list manually
- Extensible
  - Later one could create a separate more interactive, searchable site that uses the index. It could crawl the URLs gathering meta-data, provide social ratings, etc.
- Prevents spam since human-moderated

_Disadvantages_

- Requires a human-moderators to review and merge merge-requests
- Requires clear policies for reviewing and merging to avoid chaos and provide
  sense of fairness
- Once accepted into the index, no implicit quality control thereafter
- Finding repositories may not be that easy unless meta-data is kept in the index and the index is maintained in some rational order. Although a searchable site may be added (see advantages)

#### Story Analysis

__A1:__
_As an author I want to publish my repository so that others can find it, use it, and help me improve it._

An author forks index, adds URL to their repo, and puts in a merge request.

___Moderate___ This is the same workflow that one would use to contribute to another repository. However, this is asking more of first time authors than is absolutely necessary. All a first time author needs to know is how to push to a remote repository. Now they must also know how to fork another, update it, and issue a merge request.

__E1:__
_As an educator I want to find repositories that have activities that I can use for my classes so that I can save time preparing for classes and use materials better than what I can create on my own._

Educator visits index, searches through URLs, clicks through and explores each repo.

___Bad___ This is less than ideal for finding materials. This can be improved by developing a separate site that collects metadata through GitLab's API and provides a searchable list.

__PD1:__
_As a project director I want to know how frequently repositories are being used and updated so that I know how successful the project is._

Project director clicks through each URL in the index and records their stats.

___Moderate___ Not fun. But in theory this is an infrequent task. Also, in the beginning, there should be few such repositories. But this gets worse with time. This can be improved by developing a separate site that collects metadata through GitLab's API and provides a report.

__PD2:__
_As a project director I want the site to be updated automatically so that I don't have to spend resources updating the site._

___Moderate___ Each merge request must be reviewed. Also, someone needs to make sure the URLs don't become stale. This could be improved later by a separate tool using GitLab's API. Since accepting a merge-request is all or nothing, this requires that the community set high standards for entrance to the list. If post evaluation were possible, then this could be relaxed some.

__PD3:__
_As a project director I don't want the site to become cluttered with spam so that it will be useful to its users and successful._

___Excellent___ As long as merge-requests are adequately reviewed, the list should only contain acceptable material. However, there is a risk of the indexed repositories becoming worse over time. For example, once a repository is added to the list, it could change becoming less than acceptable.

### Hosted GitLab with Group Forks

- Create a group for foss2serve
- Each repository forked by foss2serve is in the index
- Authors publish their work by asking foss2serve to fork their repository

_Advantages_

- Increased control of published activities
- Forks makes releases explicit

_Disadvantages_

- Synchronizing forks on each release of an activity

#### Story Analysis

__A1:__
_As an author I want to publish my repository so that others can find it, use it, and help me improve it._

An author would have to request that his/her repository be reviewed and forked. This might be through email, or through an issue tracker. Then a trusted user from the group would review the author's repository. If accepted, the trusted user would fork the authors repository into the groups.

___Moderate___
The process to request a fork would have to be made extremely clear since this is a fairly non-standard practice. Otherwise, the work is not much worse than accepting a merge-request.

__E1:__
_As an educator I want to find repositories that have activities that I can use for my classes so that I can save time preparing for classes and use materials better than what I can create on my own._

An educator navigates to the group and browses its projects.


___Moderate___
Assuming that naming and meta-data was clarified in the review process before forking the repository, this may be fine.


__PD1:__
_As a project director I want to know how frequently repositories are being used and updated so that I know how successful the project is._

Data is available with each of the groups repository.

___Good___


__PD2:__
_As a project director I want the site to be updated automatically so that I don't have to spend resources updating the site._

Updates to the authors repository are not reflected in the group's. Authors would need to request that the fork be updated. Assuming no changes are ever made to group forks, this is scriptable, but would require action.

___Moderate___

__PD3:__
_As a project director I don't want the site to become cluttered with spam so that it will be useful to its users and successful._



### Hosted GitLab with Group repositories

- Create a group for foss2serve
- Each repository owned by foss2serve is in the index
- Authors would transfer their repository to foss2serve
- foss2serve would assign original author as master of their transferred repository

_Advantages_

- Increased control over the activities
- Also collects authors

_Disadvantages_

- Not very searchable (although one might use GitLab's API to create a searchable site)
- Seems a little strange to transfer one's repo to the group. Although this might feel like an honor. It would be important to reconnect the author with the transferred repository and ensure they felt empowered to maintain it.

### Self-Hosted Forge

_Advantages_

- Built-in search that is not cluttered with un-related repositories (i.e., all repositories are open educational materials)
- Usually comes with a set of other tools that communities often need: wiki, discussion group, issue tracker, etc.
- Can control membership (or is this a disadvantage; it would be nice if anyone can apply; might provide OAuth against other popular services)

_Disadvantages_

- Huge up-front setup, install, etc.
- Requires upgrades
- Account management (maybe; depends on the forge)
- Dependent on hosting site (what happens when the grant runs out?)

_Unknowns_

- It would be nice if they provide an API that would allow other automatic indexes or summary pages to be generated.
