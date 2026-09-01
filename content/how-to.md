---
title: "Reference Guide"
layout: "mod-single"
---

## Update Blowfish Tools

`npm update -g blowfish-tools`

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


