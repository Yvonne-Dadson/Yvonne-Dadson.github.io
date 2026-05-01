from pathlib import Path
import html
import json
import shutil

import markdown


ROOT = Path(__file__).parent.resolve()
CONTENT_DIR = ROOT / "content"
LAYOUT_DIR = ROOT / "template" / "layouts"
ASSETS_DIR = ROOT / "assets"
DIST_DIR = ROOT / "dist"


def load_config():
    with (ROOT / "site.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def clean_dist():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)


def copy_assets():
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, DIST_DIR / "assets", dirs_exist_ok=True)


def page_filename(slug):
    return "index.html" if slug == "index" else f"{slug}.html"


def render_nav(pages, current_slug):
    links = []

    for page in pages:
        slug = page["slug"]
        filename = page_filename(slug)
        label = html.escape(page.get("nav", page.get("title", slug)))
        active_class = " active" if slug == current_slug else ""

        links.append(
            f'<a class="nav-link{active_class}" href="{filename}">{label}</a>'
        )

    return "\n".join(links)


def render_profile_block(profile_image):
    if not profile_image:
        return ""

    safe_src = html.escape(profile_image, quote=True)

    return (
        f'<img class="profile-image" '
        f'src="{safe_src}" '
        f'alt="Profile image" />'
    )


def render_page(config, page):
    slug = page["slug"]
    title = page["title"]
    source = page["source"]

    # This is the important line:
    # page layout overrides global layout.
    layout_name = page.get("layout", config.get("layout", "classic"))

    layout_path = LAYOUT_DIR / f"{layout_name}.html"
    markdown_path = CONTENT_DIR / source

    if not layout_path.exists():
        raise FileNotFoundError(
            f"Missing layout file: {layout_path}. "
            f"Check layout='{layout_name}' in site.json."
        )

    if not markdown_path.exists():
        raise FileNotFoundError(
            f"Missing Markdown file: {markdown_path}. "
            f"Check source='{source}' in site.json."
        )

    template = layout_path.read_text(encoding="utf-8")
    markdown_text = markdown_path.read_text(encoding="utf-8")

    html_content = markdown.markdown(
        markdown_text,
        extensions=["extra", "tables", "toc", "sane_lists"],
        output_format="html5"
    )

    replacements = {
        "{{PAGE_TITLE}}": html.escape(title),
        "{{SITE_NAME}}": html.escape(config.get("site_name", "Website")),
        "{{SITE_TYPE}}": html.escape(config.get("site_type", "Website")),
        "{{TAGLINE}}": html.escape(config.get("tagline", "")),
        "{{NAV}}": render_nav(config["pages"], slug),
        "{{PROFILE_BLOCK}}": render_profile_block(config.get("profile_image", "")),
        "{{HERO_IMAGE}}": html.escape(
            config.get("hero_image", "assets/images/hero-ocean.svg"),
            quote=True
        ),
        "{{CONTENT}}": html_content,
        "{{FOOTER_TEXT}}": html.escape(config.get("footer_text", "")),
        "{{LAYOUT_NAME}}": html.escape(layout_name)
    }

    rendered = template

    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, value)

    return rendered, layout_name


def build_site():
    config = load_config()

    clean_dist()
    copy_assets()

    for page in config["pages"]:
        rendered, layout_name = render_page(config, page)

        output_path = DIST_DIR / page_filename(page["slug"])
        output_path.write_text(rendered, encoding="utf-8")

        print(f"Built {output_path.relative_to(ROOT)} using layout: {layout_name}")


if __name__ == "__main__":
    build_site()