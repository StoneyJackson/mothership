# Requirements

## 1. Overview

We want to support a community of educators who want to create, share, find, and use open educational materials. This community needs an infrastructure to support the following activities:

- Coordination
  - Direction
  - What needs doing
  - Who is doing what
  - Deadlines
  - Events
- Communication
  - Establish culture and norms
  - Getting help
  - Making decisions
  - Discourse about direction
  - Moderate
  - All combinations of
    - Synchronous and asynchronous
    - Permanent and transient
    - Public and private
- Awareness
  - Active, opt-in (or opt-out?) notification of news/events/changes
- Management of materials
  - Find
  - Share
  - Update
  - Contribute
  - Moderate

This list may be incomplete. And each activity may not be disjoint. For example, awareness probably overlaps with everything.

The Mothership Project aims to solve only one activity: management of materials. The other activities are likely best solved using other well-known, tried-and-true solutions: e.g., issue trackers for suggestions and discussion of direction, wikis for coordination, discussion boards and list serves for persistent asynchronous communication, IRC for transient and permanent synchronous communication, and so on.

## 2. Assumptions

The Mothership Project assumes that faculty will develop open course materials in the same way that open-source developers develop open-source projects. Specifically, faculty will

- Use git to maintain their materials
- Attach an appropriate open license to their materials
- Publish their materials using a popular forge
- Follow common workflows to contribute to other faculty's materials and receive contributions from other faculty.

Normally this would probably be an unrealistic assumption. It still might be. But the community of educators that The Mothership Project is intended to serve is dedicated to teaching students how to contribute to humanitarian free and open source projects. As such, these faculty themselves need to be (or become) familiar with the tools and practices that humanitarian free and open source projects use. What better way than to use the open-source way when developing educational materials to teach the open-source way.

## 3. Requirements

### 3.1 Functional Requirements

#### 3.1.1 Find materials

The primary goal of The Mothership is to allow faculty to find repositories containing materials they are interested in. To that end, The Mothership should allow faculty to answer the following questions:

- What materials are available for class X?
- What materials are available for topic X?
- What material has the most/least downloads?
- Which material has the most/least contributors?
- Which material has most/least recently been updated?
- Which material has the most/least commits in the last T units of time?
- Which material was most/least recently posted?
- Who maintains this material?
- Where is the repository for this material?
- How is this material licensed?

Priority: this is initially low priority since initial volume of submissions is expected to be low. As submissions increase, this will become increasingly important.

#### 3.1.2 Share materials

Sharing work consists of the following:

- Faculty will maintain their materials and metadata in git repositories.
- Faculty will publicly publish their materials in a forge (e.g., GitHub).
- Faculty will attach an appropriate open license to their work.
- Faculty will register their repositories with The Mothership.
- Metadata
  - Should be useful to the maintainer as well as community
  - Mothership should provide instructions on how to include metadata
  - Mothership should incentivize inclusion of metadata (e.g., badges, stars, searching benifits, etc.)
  - Mothership should be minimally restrictive about what metadata must be included
  - Mothership should handle malformed metadata safely (e.g., prevent injections) and gracefully "fail"

#### 3.1.3 Update materials and metadata

- Maintainers update the contents of their repositories, which includes metadata, and does not update The Mothership directly.
- The Mothership will automatically update statistics and metadata about each repository.

#### 3.1.4 Contribute to materials by others

- Faculty may contribute to other faculty's repositories using git and forges outside of The Mothership.

#### 3.1.5 Moderate posted materials

- Faculty may report registrations that are off-topic, inappropriate, spam, does not meet community guidelines, etc.
- After M such reports, the registration removed from standard searches and an administrator is notified.

### 3.2 Non-functional Requirements

#### 3.2.1 FOSS

The Mothership and the technologies it depends on must be FOSS.

#### 3.2.2 The Open-Source Way

As much as possible, the Mothership must support the open-source way/
- https://opensource.com/open-source-way
- http://www.theopensourceway.org/
