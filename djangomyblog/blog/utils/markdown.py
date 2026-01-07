# djangomyblog\blog\utils\markdown.py

import markdown
import bleach

# Tags permitidas ao parse Markdown para HTML
ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS | {
    "p", "pre", "code", "h1", "h2", "h3",
    "h4", "h5", "h6", "table", "thead",
    "tbody", "tr", "th", "td", "img",
}

# Atributos de tags permitidos ao parse Markdown para HTML
ALLOWED_ATTRIBUTES = {
    "*": ["class"],
    "a": ["href", "title", "rel"],
    "img": ["src", "alt", "title"],
}

def render_markdown(text: str) -> str:
    html = markdown.markdown(
        text or "",
        extensions=[
            "extra",        # tabelas, listas avançadas, etc
            "codehilite",   # blocos de código
            "toc",          # headers com IDs
            "nl2br",        # quebra de linha estilo GitHub
            "sane_lists",
        ],
        extension_configs={
            "codehilite": {
                "guess_lang": False,
                "use_pygments": False,
            }
        }
    )

    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        strip=True
    )
