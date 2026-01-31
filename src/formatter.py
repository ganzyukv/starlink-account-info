"""Console output formatting."""

from typing import Dict, Any


def format_account_info(account: Dict[str, Any]) -> str:
    lines = [
        "=" * 70,
        "\033[1;32mSTARLINK ACCOUNT INFORMATION\033[0m",
        "=" * 70,
        ""
    ]
    
    for key, value in account.items():
        label = key.replace("_", " ").replace("Number", " Number").title()
        lines.append(f"  {label}: {value}")
    
    lines.append("")
    lines.append("=" * 70)
    
    return "\n".join(lines)
