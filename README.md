# TACC Reusable Scripts

This project hosts reusable utility scripts for TACC websites, like [TACC](https://www.tacc.utexas.edu) or [Frontera CMS](https://frontera-portal.tacc.utexas.edu) or [3Dem.org](https://3dem.org/).

## Usage

### Remote Load

1. Pick a script or style.
2. Get URL to the file on GitHub.
3. Construct URL to load it from a CDN e.g. [jsDelivr.net](https://cdn.jsdelivr.net).
4. Load the script witha  `<script>` tag.

#### Example

```
<script src="https://cdn.jsdelivr.net/gh/wesleyboar/tacc-web-utilities@bcec608/scripts/open-ext-link-in-new-tab.js">
```

### Copy/Paste

1. Pick a script or style.
2. Get URL to the file on GitHub.
3. Get raw file content from GitHub.
4. Paste raw file content into a file on the website that needs the code.
5. Add a comment to point to the URL to the file on GitHub.
6. Replace `main` with the latest commit hash.

#### Example

```
/* SEE: https://github.com/wesleyboar/tacc-web-utilities/blob/bcec608/scripts/open-ext-link-in-new-tab.js */
/* (the code copied from this repo) */
```
