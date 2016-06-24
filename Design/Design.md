# Design

## Corral URL Repository

The Corral URL Repository is a public repository hosted on a forge. It contains a list of URLs to other repositories in a file named urls.md. These are stored in a public forge, rather than in a local database so that others can publish their repository by contributing a URL to their repository using a standard software development workflow (e.g., fork-pull-request).

urls.md is a Markdown file. Markdown is used because modern forges rendering them as HTML, thus making the URLs in the list navigable when the list is viewed in a browser. However, to make it easy to parse, urls.md has a very specific syntax. Each line has the following format: a dash (-), followed by a space, followed by a URL, followed by a newline character. Each URL identifies a repository, starts with http: or https:, and ends with .git.

## Corral Harvester

The Corral Harvester gathers metadata about each repository registered with the Corral URL Repository, and generates a nicely formatted web page that educators can use to find materials appropriate for their courses. The Harverster is ran at regular intervals by a tool like chron.

The Corral Harvester generates three files: urls.json, meta.json, and index.html. Below is the structure of the first two.


__urls.json__

```json
{
  "ETag" : "686897696a7c876b7e",
  "URLs" :
  [
    "https://github.com/StoneyJackson/git-intro-activity.git",
    "https://github.com/StoneyJackson/github-workflow-activity.git"
  ]
}
```


__meta.json__

```json
{
  "https://github.com/StoneyJackson/git-intro-activity.git" :
  {
      "ETag" : "686897696a7c876b7e",
      "Data" :
      {
        ...
      }
    }
  },
  ...
}
```


When run, the Harvester does the following:

1. Update urls.md as follows:
  1. If urls.md doesn't exist
    1. Create it with an empty list and an empty ETag
  2. Use ETag to conditionally fetch urls.md from the Repository
  3. If there are no changes, the Harvester halts
  4. Parse urls.md and organize its URLs and the ETag sent in the response header into appropriate structure
  5. Write urls.json
2. Update meta.json as follows:
  1. If meta.json doesn't exist create it with empty data
  2. Delete entries in meta.json that are not in urls.json
  3. Create new empty entries in meta.json that are in urls.json but not in meta.json
  4. For each entry in meta.json
    1. Use ETag for entry to conditionally fetch its metadata from forge
    2. If there are no changes, continue to the next entry
    3. Replace metadata and ETag for entry
  5. Write new meta.json
3. Generate index.html from meta.json
