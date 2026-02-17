"""Console output formatting."""

from typing import Dict, Any

def format_user_info(user: Dict[str, Any]) -> str:
    lines = [
        "=" * 70,
        "\033[1;32mSTARLINK ACCOUNT INFORMATION\033[0m",
        "=" * 70,
        ""
    ]

    for key, value in user.items():
        # camelCase -> Title Case
        pretty_key = (
            key.replace("Id", "ID")
        )

        formatted_key = ""
        for i, ch in enumerate(pretty_key):
            if i > 0 and ch.isupper() and not pretty_key[i-1].isupper():
                formatted_key += " " + ch
            else:
                formatted_key += ch

        formatted_key = formatted_key[0].upper() + formatted_key[1:]
        lines.append(f"{formatted_key}: {value}")

    lines.append("=" * 70)

    return "\n".join(lines)
