## Forges

These solutions use a forge (a hosted repository service like GitHub) to implement Corral.

- Index-Repository: A single repository with a file containing a list of URLs. Publishing a repository is as "simple" as adding your URL to this file using a standard contribution workflow. Finding resources entails clicking through each published link.

- Group Fork: In this solution a group/organization is created in the forge. Repositories forked by the group are considered published with the group. Others can then find repositories by exploring the repositories forked by the group.

- Group Repository: A group/organization is created in a forge. The repositories owned by the group are the published works. When an author wants to publish their work, they transfer their repository to the group. Ideally, the group would induct the author as a member of the group and assign them to the repository they transferred so that they can maintain it.

- Self-Hosted: A forge is installed and maintained for the express purpose of housing repositories that contain course materials. In this model, any repository created in the forge is a materials repository. One can find materials by using the forges built-in search mechanisms.

## Content Management Systems

In these solutions, a content management system (CMS) is configured to serve as the Corral. CMS typically support an editorial review process with users with different roles. This functionality may or may not be needed depending on the final requirements of Corral. Several CMS listed below have a collection of community maintained plugins/packages that help customize the CMS. They may also be customized by creating custom plugins. In theory, one could customize a CMS to the exact needs of Corral.

- WordPress

- Drupal

- Joomla

## Wiki

Wikis are similar to CMS. The difference is that CMS don't typically allow different authors to edit the same page, whereas wikis do.

- Tiki(Groups)

- MediaWiki

- Wagn

## Close-but-not-quite

These are existing tools that are similar to what corral wishes to be. They may need customization to get them to meet the needs of Corral. The effort needed to install, configure, and customize is unknown.

- RubyGems

- PyPI

## Build from Scratch

Sky's the limit. So is the time and effort needed.
