# ============================================================
# 🌍 IP LOCATION FINDER + NETWORK INTELLIGENCE
# 🐍 Built with Python
# ============================================================

import requests

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box


# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

API_TOKEN = "200e44eff4a3fd"

console = Console()


# ------------------------------------------------------------
# GET IP INFORMATION
# ------------------------------------------------------------

def get_ip_info(ip_address):
    """
    Fetch IP information from the IPinfo Lite API.
    """

    url = f"https://api.ipinfo.io/lite/{ip_address}"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        console.print("[red]Request timed out.[/red]")
        return None

    except requests.exceptions.RequestException as error:
        console.print(
            f"[red]API request failed: {error}[/red]"
        )
        return None


# ------------------------------------------------------------
# DISPLAY IP INFORMATION
# ------------------------------------------------------------

def display_ip_information(data):

    table = Table(
        title="🌍 IP INFORMATION",
        box=box.ROUNDED
    )

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    fields = {
        "IP Address": data.get("ip", "N/A"),
        "Country": data.get("country", "N/A"),
        "Country Code": data.get("country_code", "N/A"),
        "Continent": data.get("continent", "N/A"),
        "Continent Code": data.get("continent_code", "N/A"),
        "ASN": data.get("asn", "N/A"),
        "ASN Name": data.get("as_name", "N/A"),
        "ASN Domain": data.get("as_domain", "N/A")
    }

    for field, value in fields.items():
        table.add_row(field, str(value))

    console.print(table)


# ------------------------------------------------------------
# DISPLAY NETWORK INFORMATION
# ------------------------------------------------------------

def display_network_information(data):

    table = Table(
        title="🌐 NETWORK INFORMATION",
        box=box.ROUNDED
    )

    table.add_column("Field", style="magenta")
    table.add_column("Value", style="green")

    fields = {
        "ASN": data.get("asn", "N/A"),
        "Organization": data.get("as_name", "N/A"),
        "Domain": data.get("as_domain", "N/A"),
        "Country": data.get("country", "N/A")
    }

    for field, value in fields.items():
        table.add_row(field, str(value))

    console.print(table)


# ------------------------------------------------------------
# DISPLAY SUMMARY
# ------------------------------------------------------------

def display_summary(data):

    ip = data.get("ip", "N/A")
    country = data.get("country", "N/A")
    continent = data.get("continent", "N/A")
    organization = data.get("as_name", "N/A")

    summary = f"""
[cyan]IP Address:[/cyan] {ip}

[cyan]Approximate Region:[/cyan]
{country}, {continent}

[cyan]Network Organization:[/cyan]
{organization}

[yellow]Note:[/yellow]
IP information is approximate and depends on
the data available from the API.
"""

    console.print(
        Panel(
            summary,
            title="🔎 ANALYSIS RESULT",
            border_style="green"
        )
    )


# ------------------------------------------------------------
# GET USER'S OWN PUBLIC IP
# ------------------------------------------------------------

def get_own_ip():

    try:
        response = requests.get(
            "https://api.ipify.org",
            timeout=10
        )

        response.raise_for_status()

        return response.text.strip()

    except requests.exceptions.RequestException:

        console.print(
            "[red]Could not determine your public IP.[/red]"
        )

        return None


# ------------------------------------------------------------
# VALIDATE IP INPUT
# ------------------------------------------------------------

def validate_ip(ip_address):

    if not ip_address:
        return False

    allowed_characters = set(
        "0123456789abcdefABCDEF:."
    )

    return all(
        character in allowed_characters
        for character in ip_address
    )


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]🌍 IP LOCATION FINDER[/bold cyan]\n"
            "[bold green]+ NETWORK INTELLIGENCE[/bold green]\n\n"
            "Python-powered IP information analyzer",
            border_style="magenta"
        )
    )

    # Ask for IP address
    ip_address = input(
        "\nEnter an IP address "
        "(leave blank for your own public IP): "
    ).strip()

    # Detect public IP if blank
    if not ip_address:

        console.print(
            "\n[cyan]Detecting your public IP...[/cyan]"
        )

        ip_address = get_own_ip()

        if not ip_address:
            return

    # Validate IP address
    if not validate_ip(ip_address):

        console.print(
            "[red]Please enter a valid IPv4 or IPv6 address.[/red]"
        )

        return

    console.print(
        f"\n[cyan]Analyzing:[/cyan] {ip_address} ..."
    )

    # Get IP information
    data = get_ip_info(ip_address)

    if not data:
        return

    # Display results
    display_summary(data)

    display_ip_information(data)

    display_network_information(data)

    # Final message
    console.print(
        Panel(
            "[bold green]✓ Analysis complete[/bold green]\n\n"
            "Use this project to learn about:\n"
            "• Python APIs\n"
            "• JSON data\n"
            "• IP addressing\n"
            "• Networking\n"
            "• IP intelligence",
            title="💻 CODE WITH VRUSHABH",
            border_style="magenta"
        )
    )


# ------------------------------------------------------------
# RUN PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()