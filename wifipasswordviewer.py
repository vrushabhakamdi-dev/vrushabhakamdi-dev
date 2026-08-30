import subprocess

names = [
    line.split(":")[1].strip()
    for line in subprocess.check_output(
        "netsh wlan show profiles",
        shell=True
    ).decode().split("\n")
    if "All User Profile" in line
]

for i, name in enumerate(names):
    print(f"{i}: {name}")

ch = int(input("\nChoose WiFi number: "))

wifi = names[ch]

result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear',
    shell=True
).decode()

print("\n" + result)