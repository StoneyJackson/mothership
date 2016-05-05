# The Mothership

[The name The Mothership is a placeholder until a better name is thought of.]

The Mothership will be a website that supports a community of educators developing a curriculum of course materials for teaching open-source development using open-source tools and practices. The website will allow community members to find, request, share, organize, and improve open educational materials that are published in various forges. The website will help the community members stay motivated, connected, and engaged by raising its members awareness of members' activities.

## Users

The Mothership users are primarily faculty with masters and doctorates in computer science, mathematics, or other related disciplines. Their experience with open source tools and practices will vary from none to a lot. But most will be closer to the "none" end of the spectrum. They have very limited time, as their primary responsibility is to teach their courses, conduct research, and dispatch other faculty duties.

Community members are motivated to develop course materials in an open-source way for the following reasons:

- To learn the tools and practices that they intend to teach.
- To benefit from contributions to their work by community members.
- To benefit from the collection of materials created by the community.
- To feel good about contributing to a larger community.

## User Goals Supported by The Mothership

- __Find__ educational resources to use in their classes.
- __Request__ educational resources to use in their classes.
- __Share__ educational resources for others to use in their classes.
- __Improve__ educational resources shared by others.
- __Update__ educational resources
- __Organize__ the development of educational resources.
- __Moderate__ registered resources to reduce spam and other untoward behavior.
- __Remain aware__ of new and updated resources of interest.
- __Communicate__ with other members of the community.

## User Requirements

- __Find__
  - Search that searches keywords, titles, and descriptions
  - Results provide information to help evaluate the quality of a resources
  - Returned resources and metadata is up-to-date
  - Can sort results by various statistics (downloads, last updated date, posted date, stars, activity)
  - Can list all resources
  - Can find resources associated with pathways and their steps
  - Can find what's missing (based on pathways) and most wanted
  - Can list reported resources/pathways/etc.
  - Can list quarantined resources/pathways/etc.
- __Request__
  - Can request new materials
  - Can vote up requests
- __Share__
  - Can share resources by submitting a URL to publicly hosted repository and providing some basic information about the resource
- __Improve__
  - Can provide feedback on resources (stars, comments, up/down votes)
- __Update__
  - Can update resources that you have registered (keywords, url, title, etc)
- __Organize__
  - Can manage pathways and their steps
  - Steps provide keywords that can be referenced by resources
- __Moderate__
  - Can report/pull/delete inappropriate resources/pathways/etc.
- __Remain Aware__
  - Can register for changes on particular resources.
  - Can register to be notified when new resources are registered for particular keywords.
  - Can register to be notified when any new resources are registered.
  - Can be notified ...
- __Communicate__
  - Support public asynchronous communication.
  - Support private asynchronous communication.
  - Support public synchronous communication.
  - Support private synchronous communication.

## Features

### Core Features

If we don't have these, we have nothing.

- User accounts
- Post repository URLs with title, keywords, and license
- Search repositories by title, keywords, and/or license

### Crawler Feature

- Verifies URLs to repositories; invalid repositories are marked invalid
- Collects and updates metadata about repositories
- Metadata examples: number of downloads, developers, contributors, release number, release date, last updated date, average commits per unit time, etc.
- Repositories now display metadata
- List invalid resources
- Searches can be sorted by metadata

### Moderate Feature

- Allow users to report repositories
- Automatically pulls a repository with N or more reports and notifies admin.
- List reported repositories
- List pulled repositories

### Notification Feature

- Register for notifications for
  - Changes to a particular repository
  - New repositories
  - New repositories that match keywords
