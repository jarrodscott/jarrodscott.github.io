---
title: "Reference Guide"
layout: single # changed from mod-single
showPagination: false
draft: true
---

## Turn a Standalone HTML file into a Web Page

### Phase 1

1. Navigate to your project folder (replace with your folder's path)

`cd /path/to/your/project/folder`

2. Initialize the Git repository

`git init`

3. Rename the default branch to 'main' (matches GitHub's default)

`git branch -M main`

4. Stage all your current project files

`git add .`

5. Commit the files to your history

`git commit -m "Initial commit"`

### Phase 2: Create the Remote Repository on GitHub

1. Go to GitHub and log in.

2. Click the + icon in the upper-right corner and select **New repository**.

3. Enter your Repository name.

4. **Crucial**: Leave **Add a README file**, **Add .gitignore**, and **Choose a license** unchecked. (Since you already have a local project, initializing these on GitHub will create a conflict).

5. Click **Create repository**.

### Phase 3: Link Local to GitHub & Push

Once the GitHub page loads, copy the repository URL under the **Quick setup** section. Return to your terminal and run:

1. Link your local repo to the remote GitHub repo

*(Replace the URL with your copied GitHub repository URL)*

`git remote add origin <URL>` # e.g. https://github.com/mysite/myrepo.git

2. Push your code to GitHub and track the branch

`git push -u origin main`


### Phase 4: Turn the GitHub Repo into a Live Link 

By default, sharing a link directly to a file on GitHub just shows the raw code, not the rendered webpage. You must first use GitHub Pages to host it as a real website.

#### Step 1: Check your file naming

1. Make sure your repository is **Public**.

2. Ensure your main HTML file is named exactly `index.html` and sits in the `main/root` folder. If it has another name (like `project.html`), it can still be linked, but `index.html` must exist for the directory to load.

#### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub.

2. Click on the **Settings** tab (the gear icon on the top menu).

3. On the left sidebar, click on **Pages**.

4. Under **Build and deployment** -> **Source**, make sure **Deploy from a branch** is selected.

5. Under **Branch**, change None to `main` (or `master`) and keep the folder as `/root`.

6. Click **Save**

#### Step 3: Get your link and add it to your site

Go to the **Actions** tab and wait 1 to 2 minutes for the page to build. The URL will look like this:
https://your-username.github.io/your-repo-name/

## Deploying Quarto Projects as GitHub Pages Subpages

This tutorial explains how to deploy any Quarto document or project (Reveal.js slides, single-page documents, or multi-page websites) as a subpage of your primary GitHub Pages site. Your project will live at `https://myname.github.io/repo-name/` while keeping its source files completely separate from your main homepage repository.


### 🛠️ Step 1: Initialize Your Project Directory

Before touching GitHub, organize your local project folder depending on your project type.

**Scenario A**: Project WITH a `_quarto.yml` File (Multi-page or Slide Frameworks)

Use this option if you are building an organized website, a collection of slides, or a multi-page document.

1. Ensure your main entry file is named exactly `index.qmd`.

2. Create a` _quarto.yml` file in your root folder and define the site-url so paths do not break on GitHub:

```
project:
  type: website
  output-dir: _site

website:
  site-url: https://myname.github.io/repo-name/
```

*(Replace myname with your username and repo-name with your repository name. Remove the spaces inside the URL).*

**Scenario B**: Project WITHOUT a `_quarto.yml` File (Standalone Page)

If you only have a single `.qmd `file (e.g., a standalone report or simple slideshow) and no configuration files:

1. Rename your standalone file to `index.qmd`.

2. Because there is no `_quarto.yml` to specify the output folder, Quarto's default build behavior outputs directly to the root folder. Our automated deployment workflow will handle this structure seamlessly.

### 📂 Step 2: Create and Set Up Your GitHub Repository

1. Go to GitHub and create a **new public repository**.

2. Set the repository name to exactly what you want your URL subpage path to be (e.g., `repo-name`).

3. Leave it completely empty (do not check the boxes for a `README` or `.gitignore`).

4. Once created, go to **Settings** > **Actions** > **General**.

5. Scroll to the bottom to **Workflow permissions**, select **Read and write permissions**, and click **Save**.

### 🤖 Step 3: Add the Automated GitHub Actions Workflow

1. In your local project directory, create the following path: `.github/workflows/`

2. Create a file inside named `publish.yml`.

3. Paste the following configuration. This workflow auto-detects if your project uses an `_quarto.yml` output folder (`_site`) or outputs to the root directory, installs the R environment, and automatically updates your pages branch.

```
on:
  workflow_dispatch:
  push:
    branches: [ main, master ]

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up R
        uses: r-lib/actions/setup-r@v2

      - name: Install R Packages
        uses: r-lib/actions/setup-r-dependencies@v2
        with:
          packages: |
            knitr
            rmarkdown
            tidyverse

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render Quarto Project
        uses: quarto-dev/quarto-actions/render@v2

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # Auto-selects '_site' if it exists; otherwise deploys root files
          publish_dir: ${{ hashFiles('_quarto.yml') != '' && './_site' || './' }}
          publish_branch: gh-pages
```
*In the section on `Install R Packages` make certain that all of the packages are listed here or the build will fail.*


### 🚀 Step 4: Link and Push to GitHub

Run these commands in your local project terminal to link your repository and create the placeholder branch that GitHub Pages requires.

```
# 1. Initialize and push your main source code
git init
git add .
git commit -m "Initial commit with Quarto configuration and workflow"
git branch -M main
git remote add origin https://github.com/myname/repo-name.git
git push -u origin main

# 2. Create the blank deployment branch to initialize the pipeline
git checkout --orphan gh-pages
git rm -rf .
git commit --allow-empty -m "Initialize gh-pages branch"
git push origin gh-pages

# 3. Return to your working code branch
git checkout main

```

### 🌐 Step 5: Enable the Live Site

1. Go to your repository on GitHub.

2. Click **Settings** > **Pages**.

3. Under **Build and deployment**, ensure **Source** is set to `Deploy from a branch`, and **Branch** is set to `gh-pages` and `/(root)`. Click **Save**.

4. Go to the **Actions** tab, click your workflow, and manually trigger it or let your push finish executing.

Once the run turns green, your site will be live at `https://myname.github.io/repo-name/`!



## Guide Addendum: Deploying a Blogdown (Hugo) Site as a Subpage

> Be sure [Step #2 above is completed](/how-to/#-step-2-create-and-set-up-your-github-repository). 

### 🛠️ Step 1: Update Your `config.yaml` Path

Hugo relies heavily on its `baseURL` parameter to build correct paths for CSS, JS, and themes. If this isn't set up for a subpage folder, your layout and theme (`Ghostwriter`) will completely break on GitHub Pages.

1. Open your root `config.yaml `(or `config.toml` depending on your setup).

2. Update the `baseURL` property to include your target subpage directory:


```
baseURL: https://myname.github.io/blog-subpage/
```

you also may need to add `publishDir: public` at the top level of the file. 


*(Remember to remove the spaces when updating your file, and ensure it ends with a trailing slash `/`).*

### 🤖 Step 2: Add the Blogdown GitHub Actions Workflow

Because Blogdown needs Hugo to compile the final pages, our workflow must check out the repo, install R, install Hugo, build the site using Blogdown, and then push the generated `public` folder to the `gh-pages` branch.


In your Blogdown project folder, create `.github/workflows/publish.yml` and paste this configuration:

```
on:
  workflow_dispatch:
  push:
    branches: [ main, master ]

name: Blogdown Publish

# Grant the workflow the necessary permissions to publish to GitHub Pages
permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up R
        uses: r-lib/actions/setup-r@v2

      - name: Install R Dependencies
        uses: r-lib/actions/setup-r-dependencies@v2
        with:
          packages: |
            blogdown
            rmarkdown
            knitr
            tidyverse
            DT
            Rcpp
            htmltools

      - name: Set up Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build Blogdown Site
        run: |
          Rscript -e 'rmarkdown::render_site(encoding = "UTF-8")'
          hugo --gc --minify
          echo "=== CHECKING CURRENT DIRECTORY COMTENTS ==="
          ls -la
          echo "=== CHECKING PUBLIC DIRECTORY CONTENTS ==="
          ls -la public || echo "No public folder found!"

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          publish_branch: gh-pages
          enable_jekyll: true
```

### 🚀 Step 3: Git Initialization & Empty Branch Setup

Just like before, we need to wire up the repo and initialize the `gh-pages` target branch so the automated script doesn't fail on its first run.

Run these in your local terminal inside your Blogdown directory:

```
# 1. Push your source code
git init
git add .
git commit -m "Initial commit with Blogdown workflow"
git branch -M main
git remote add origin https://github.com/myname/blog-subpage.git
git push -u origin main

# 2. Force-initialize the empty pages deployment branch 
git checkout --orphan gh-pages
git rm -rf .
git commit --allow-empty -m "Initialize gh-pages branch for Blogdown"
git push origin gh-pages

# 3. Head right back to your code
git checkout main

```

### 🌐 Step 4: Toggle Repository Permissions & Pages Settings

1. Go to your new repository on GitHub.

2. Go to *Settings* > *Actions* > *General*, scroll to the bottom, toggle **Read and write permissions**, and click **Save**.

3. Go to **Settings** > **Pages**, make sure the *Source* is `Deploy from a branch`, and the **Branch** is set to `gh-pages` (`/(root)`). Click **Save**.


{{< cta url="/posts/quarto_and_hugo" label="Quarto+Hugo" style="outline" >}}

## Summary Reference Matrix

| Asset Scenario                 | Best Location             | Why?                                                            |
|--------------------------------|---------------------------|-----------------------------------------------------------------|
| custom.css                     | extend-head.html          | Core styles apply globally.                                     |
| Google Analytics               | extend-head.html          | Runs everywhere across the build.                               |
| Altmetric/Dimensions JS Script | extend-head-uncached.html | Only downloads the script file if the shortcode is on the page. |
| Creative Commons CSS (cc.css)  | extend-head-uncached.html | Keeps the site payload lean on pages without licenses.          |
| Math formula engines (KaTeX)   | extend-head-uncached.html | Only loaded when the page front-matter requires it.             |

## The Best Practice Decision Rule

| Approach                                   | Where to Use                                  | Why?                                                                                                            |
|--------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Direct <link> in Template                  | Custom Page Layouts (about-block-layout.html) | Executes only once; 100% self-contained with zero overhead.                                                     |
| extend-head-uncached.html + .HasShortcode  | Public/Shared Shortcodes                      | The gold-standard Hugo pattern. Guarantees all stylesheets reside in the document <head> and never duplicate.   |
| .Page.Store Deduplicated <link>            | Portable Drop-in Shortcodes                   | Great if you want a shortcode that requires zero edits to any header template or theme partial.                 |


https://www.visualcinnamon.com/

## Update Blowfish Tools

`npm update -g blowfish-tools`

## Update Blowfish Theme

### Hugo module

I used `Git submodule` to install

Simply run `git submodule update --remote --merge`

## Creating Pulication File

`conda activate academic`  
`academic import cite.bib content/publications/`

where `cite.bib` is a bibtex file for a *single* publication. I do not know if this will work with a bibtex file containing many entries. 


## GitHub Actions

A quick how-to for Deploying your website using GitHub Actions. You do not need to build the site yourself or upload the compiled `public` folder; GitHub will do all the work in the cloud automatically whenever you push code.

Because Blowfish relies on specific submodules and the Hugo Extended engine to process its Tailwind CSS styles, your workflow file needs a couple of specific settings.

Follow these steps to set up automated deployment without needing prior Actions experience:

### Step 1: Create the Workflow File

 You just need to add a single configuration file to your repository. This file acts as an automated recipe telling GitHub exactly how to install Hugo, pull your Blowfish submodule, and build the site.

1. In your local project's root folder, create a new folder structure: `.github/workflows/`.
2. Inside the workflows folder, create a file named `deploy.yml`
3. Paste the following exact configuration into `deploy.yml`:

```
name: Deploy Hugo site to Pages

on:
  push:
    branches:
      - main  # Change this to 'master' if your default branch is master
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: 'recursive' # Crucial: This pulls your Blowfish submodule
          fetch-depth: 0

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          extended: true # Crucial: Blowfish requires Hugo Extended for CSS compiling

      - name: Build with Hugo
        env:
          HUGO_ENV: production
        run: |
          hugo --gc --minify

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Step 2: Enable Actions in GitHub Settings

Before pushing your code, you must change one default setting inside your remote GitHub repository so it accepts deployments from Actions.

1. Go to your repository page on `GitHub.com`
2. Click on the `Settings` tab at the top
3. On the left sidebar, scroll down to `Code and Automation` and click `Pages`
4. Under `Build and deployment`, locate the `Source` dropdown menu and change it from `Deploy from a branch` to `GitHub Actions`.

### Step 3: Push Your Site Live

Now you just need to save your changes and upload them to GitHub.

1. Open your terminal in your local project folder.
2. Stage and commit your new workflow file:

```
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions deployment workflow"
git push origin main
```

Once pushed, go to the Actions tab on your GitHub repository page. You will see a green or yellow circle indicating that your website is building in the cloud. When it finishes (usually taking less than a minute), GitHub will provide the live link to your website right there!


