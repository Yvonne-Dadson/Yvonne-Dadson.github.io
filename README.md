# Website Template

A static website template for researchers, students, and labs. You can fork this repository, edit a few files directly in the GitHub browser, and publish a website with GitHub Pages.

No local download is required.

## What You Edit

Most users only need to edit these files:

- `site.json`: site name, title, tagline, images, footer, pages, and layouts
- `content/home.md`: home page text
- `content/now.md`: current work or current focus
- `content/research.md`: research themes
- `content/projects.md`: projects
- `content/cv.md`: CV page
- `content/contact.md`: contact links

The website is built automatically by GitHub Actions using `build_site.py`. The generated website is published from the `dist` folder.

## Browser-Only Setup

### 1. Fork This Repository

Open this repository on GitHub and click **Fork**.

GitHub will create your own copy of the template under your account.

### 2. Choose Your Website URL

You have two choices.

#### Option A: Personal Website

Use this if you want your website at:

```text
https://YOUR-USERNAME.github.io/
```

After forking, rename the repository to:

```text
YOUR-USERNAME.github.io
```

For example, if your GitHub username is `pkjr002`, the repository must be named:

```text
pkjr002.github.io
```

#### Option B: Project Website

Use this if you want your website at:

```text
https://YOUR-USERNAME.github.io/REPOSITORY-NAME/
```

In this case, you can keep any repository name, such as:

```text
researcher-website
```

### 3. Turn On GitHub Pages

In your forked repository:

1. Go to **Settings**
2. Go to **Pages**
3. Under **Build and deployment**, set **Source** to **GitHub Actions**

The workflow in `.github/workflows/deploy.yml` will build and publish the site.

### 4. Edit Site Settings

Open `site.json` in GitHub.

Click the pencil icon to edit the file.

Change these fields:

```json
{
  "site_name": "Your Name",
  "site_type": "Your Title",
  "tagline": "Your research topics",
  "footer_text": "© 2026 Your Name"
}
```

You can also change:

```json
"profile_image": "assets/images/profile-placeholder.svg",
"hero_image": "assets/images/hero-ocean.svg"
```

When finished, click **Commit changes**.

### 5. Edit Page Content

Open files in the `content` folder and edit them in the browser.

For example:

- Edit `content/home.md` for your homepage
- Edit `content/research.md` for your research areas
- Edit `content/projects.md` for your projects
- Edit `content/contact.md` for your email and links
- Edit `content/cv.md` for your CV information

Each time you finish editing a file, click **Commit changes**.

### 6. Upload a Profile Image

To add your own profile image:

1. Go to `assets/images`
2. Click **Add file**
3. Click **Upload files**
4. Upload your image, for example `profile.jpg`
5. Commit the upload
6. Open `site.json`
7. Set:

```json
"profile_image": "assets/images/profile.jpg"
```

Commit the change.

### 7. Upload a CV PDF

To add a downloadable CV:

1. Go to `assets/files`
2. Click **Add file**
3. Click **Upload files**
4. Upload your PDF, for example `cv.pdf`
5. Commit the upload
6. Open `content/cv.md`
7. Add or update this line:

```md
[Download my CV](assets/files/cv.pdf)
```

Commit the change.

If you do not want a downloadable CV, remove the download section from `content/cv.md`.

## Publishing

Every time you commit a change, GitHub Actions rebuilds the website.

To check progress:

1. Go to the **Actions** tab
2. Open the latest workflow run
3. Wait for it to finish successfully

When the workflow is complete, your site will be available at one of these URLs:

```text
https://YOUR-USERNAME.github.io/
```

or:

```text
https://YOUR-USERNAME.github.io/REPOSITORY-NAME/
```

## Editing Layouts

Each page can use a different layout. Layouts are set in `site.json`.

Available layouts:

- `classic`
- `sidebar`
- `split`
- `cards`
- `minimal`
- `lab`

Example:

```json
{
  "slug": "research",
  "title": "Research",
  "source": "research.md",
  "nav": "Research",
  "layout": "cards"
}
```

## Changing Navigation

Navigation is controlled by the `pages` list in `site.json`.

To rename a navigation item, change the `nav` field:

```json
"nav": "Research"
```

To change the browser page title, change the `title` field:

```json
"title": "Research"
```

To remove a page from the website, remove that page object from the `pages` list.

## Troubleshooting

### My Site Is Not Online

Check these items:

- In **Settings → Pages**, make sure **Source** is set to **GitHub Actions**
- In the **Actions** tab, make sure the latest workflow finished successfully
- Make sure your repository is public, or that your GitHub plan supports Pages for private repositories

### My Personal Website URL Does Not Work

For a personal GitHub Pages website, the repository name must exactly match:

```text
YOUR-USERNAME.github.io
```

For example:

```text
janedoe.github.io
```

### My Project Website URL Does Not Work

For a normal project repository, use:

```text
https://YOUR-USERNAME.github.io/REPOSITORY-NAME/
```

Do not use the personal-site URL unless the repository is named `YOUR-USERNAME.github.io`.

### My CV Link Does Not Work

Make sure the PDF exists at the path used in `content/cv.md`.

For example, this markdown:

```md
[Download my CV](assets/files/cv.pdf)
```

requires this file:

```text
assets/files/cv.pdf
```

### My Image Does Not Show

Make sure the image path in `site.json` matches the uploaded file exactly.

Example:

```json
"profile_image": "assets/images/profile.jpg"
```

The file must exist at:

```text
assets/images/profile.jpg
```

## Advanced Local Use

This template is designed for browser-only editing, but it can also be built locally.

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the site:

```bash
python build_site.py
```

Serve the generated site:

```bash
cd dist
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

You can also use Docker:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8080
```
