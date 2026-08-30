"""
CODE WITH VRUSHABH
Password Security Simulator
Educational / Local Simulation Only

Requirements:
    Python 3.x

Run:
    python democracker.py
"""

import itertools
import string
import time


# ============================================================
# CONFIGURATION
# ============================================================

# Strict limit for the small educational demonstration
MAX_ATTEMPTS = 2_000_000

# Demo mode supports only lowercase letters and numbers
DEMO_CHARSET = string.ascii_lowercase + string.digits


# ============================================================
# PASSWORD STRENGTH ANALYZER
# ============================================================

def analyze_password(password):
    length = len(password)
    score = 0

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if length >= 8:
        score += 20

    if length >= 12:
        score += 20

    if length >= 16:
        score += 20

    if has_lower:
        score += 10

    if has_upper:
        score += 10

    if has_digit:
        score += 10

    if has_symbol:
        score += 10

    score = min(score, 100)

    if score < 30:
        level = "VERY WEAK"
    elif score < 50:
        level = "WEAK"
    elif score < 70:
        level = "MODERATE"
    elif score < 85:
        level = "STRONG"
    else:
        level = "VERY STRONG"

    return {
        "score": score,
        "level": level,
        "length": length,
        "lower": has_lower,
        "upper": has_upper,
        "digit": has_digit,
        "symbol": has_symbol
    }


# ============================================================
# CHARACTER SET ANALYSIS
# ============================================================

def get_charset_size(password):

    size = 0

    if any(c.islower() for c in password):
        size += 26

    if any(c.isupper() for c in password):
        size += 26

    if any(c.isdigit() for c in password):
        size += 10

    if any(c in string.punctuation for c in password):
        size += len(string.punctuation)

    return size


# ============================================================
# FORMAT LARGE NUMBERS
# ============================================================

def format_number(number):

    if number < 1_000:
        return f"{number:,}"

    if number < 1_000_000:
        return f"{number / 1_000:.2f} Thousand"

    if number < 1_000_000_000:
        return f"{number / 1_000_000:.2f} Million"

    if number < 1_000_000_000_000:
        return f"{number / 1_000_000_000:.2f} Billion"

    if number < 1_000_000_000_000_000:
        return f"{number / 1_000_000_000_000:.2f} Trillion"

    return f"{number:.2e}"


# ============================================================
# FORMAT TIME
# ============================================================

def format_time(seconds):

    if seconds < 1:
        return "Less than 1 second"

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    minutes = seconds / 60

    if minutes < 60:
        return f"{minutes:.2f} minutes"

    hours = minutes / 60

    if hours < 24:
        return f"{hours:.2f} hours"

    days = hours / 24

    if days < 365:
        return f"{days:.2f} days"

    years = days / 365

    if years < 1_000_000:
        return f"{years:,.2f} years"

    return f"{years:.2e} years"


# ============================================================
# THEORETICAL DIFFICULTY ESTIMATOR
# ============================================================

def estimate_difficulty(password):

    charset_size = get_charset_size(password)

    if charset_size == 0:
        return None

    combinations = charset_size ** len(password)
    average_attempts = combinations / 2

    return {
        "charset_size": charset_size,
        "combinations": combinations,
        "average_attempts": average_attempts
    }


# ============================================================
# SECURITY RECOMMENDATIONS
# ============================================================

def get_recommendations(data):

    recommendations = []

    if data["length"] < 12:
        recommendations.append(
            "Use at least 12 characters for better security."
        )

    if not data["upper"]:
        recommendations.append(
            "Add uppercase letters."
        )

    if not data["lower"]:
        recommendations.append(
            "Add lowercase letters."
        )

    if not data["digit"]:
        recommendations.append(
            "Add numbers."
        )

    if not data["symbol"]:
        recommendations.append(
            "Consider adding special characters."
        )

    if not recommendations:
        recommendations.append(
            "Good password length and character variety."
        )

    return recommendations


# ============================================================
# DISPLAY SECURITY ANALYSIS
# ============================================================

def display_analysis(password):

    data = analyze_password(password)
    difficulty = estimate_difficulty(password)
    recommendations = get_recommendations(data)

    print("\n" + "=" * 65)
    print("       CODE WITH VRUSHABH — PASSWORD SECURITY ANALYSIS")
    print("=" * 65)

    print("\nPASSWORD DETAILS")
    print("-" * 65)

    print(f"Length              : {data['length']} characters")
    print(f"Strength            : {data['level']}")
    print(f"Security Score      : {data['score']}/100")

    print("\nCHARACTER TYPES")
    print("-" * 65)

    print(f"Lowercase Letters   : {'YES' if data['lower'] else 'NO'}")
    print(f"Uppercase Letters   : {'YES' if data['upper'] else 'NO'}")
    print(f"Numbers             : {'YES' if data['digit'] else 'NO'}")
    print(f"Special Characters  : {'YES' if data['symbol'] else 'NO'}")

    print("\nTHEORETICAL SEARCH SPACE")
    print("-" * 65)

    print(f"Character Pool Size : {difficulty['charset_size']}")
    print(
        f"Possible Combinations: "
        f"{format_number(difficulty['combinations'])}"
    )

    print(
        f"Average Attempts    : "
        f"{format_number(difficulty['average_attempts'])}"
    )

    print("\nHYPOTHETICAL TIME ESTIMATES")
    print("-" * 65)

    speeds = {
        "1 Thousand guesses/sec": 1_000,
        "1 Million guesses/sec": 1_000_000,
        "1 Billion guesses/sec": 1_000_000_000
    }

    for name, speed in speeds.items():
        seconds = difficulty["average_attempts"] / speed
        print(f"{name:<28}: {format_time(seconds)}")

    print("\nSECURITY RECOMMENDATIONS")
    print("-" * 65)

    for recommendation in recommendations:
        print(f"[+] {recommendation}")

    print("\nPASSWORD SECURITY FACT")
    print("-" * 65)
    print("Longer passwords + uppercase + numbers + symbols")
    print("= exponentially larger theoretical search space.")
    print()
    print("Each additional character can dramatically increase")
    print("the number of possible combinations.")

    print("\n" + "=" * 65)


# ============================================================
# LIMITED EDUCATIONAL DEMONSTRATION
# ============================================================

def demo_simulation():

    print("\n" + "=" * 65)
    print("       LIMITED LOCAL EDUCATIONAL DEMONSTRATION")
    print("=" * 65)

    print("\nDemo restrictions:")
    print("- Lowercase letters (a-z)")
    print("- Numbers (0-9)")
    print("- Maximum 6 characters")
    print("- Maximum 2,000,000 attempts")

    target = input("\nEnter a small demo value: ").strip()

    if not target:
        print("Input cannot be empty.")
        return

    if len(target) > 6:
        print("Demo values must be 6 characters or fewer.")
        return

    if any(character not in DEMO_CHARSET for character in target):
        print("Use only lowercase letters and numbers.")
        return

    attempts = 0
    start_time = time.perf_counter()

    print("\nSTATUS: DEMONSTRATION RUNNING...\n")

    for length in range(1, len(target) + 1):

        for combination in itertools.product(
            DEMO_CHARSET,
            repeat=length
        ):

            attempts += 1

            if attempts > MAX_ATTEMPTS:
                print("\nSimulation safety limit reached.")
                print(f"Attempts: {format_number(attempts)}")
                return

            guess = "".join(combination)

            if attempts % 10_000 == 0:
                elapsed = time.perf_counter() - start_time
                speed = attempts / elapsed if elapsed > 0 else 0

                print(
                    f"\rDemo Attempts: {format_number(attempts)} | "
                    f"Speed: {speed:,.0f}/sec",
                    end=""
                )

            if guess == target:

                elapsed = time.perf_counter() - start_time

                print("\n\nDEMONSTRATION COMPLETE")
                print("-" * 65)
                print(f"Demo value matched : {guess}")
                print(f"Attempts           : {format_number(attempts)}")
                print(f"Time               : {elapsed:.2f} seconds")

                return


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║                 CODE WITH VRUSHABH                       ║")
    print("║         PASSWORD SECURITY AWARENESS TOOL                 ║")
    print("╚══════════════════════════════════════════════════════════╝")

    print("\n1. Password Security Analysis")
    print("2. Limited Educational Demonstration")

    choice = input("\nChoose an option (1/2): ").strip()

    if choice == "1":

        password = input(
            "\nEnter a test password for analysis: "
        )

        if not password:
            print("Password cannot be empty.")
            return

        display_analysis(password)

    elif choice == "2":
        demo_simulation()

    else:
        print("Invalid option. Please restart and choose 1 or 2.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()