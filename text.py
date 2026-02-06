import subprocess, sys, time, os

# --- 1. SETUP & DEPENDENCIES ---
# Added 'opencv-python' (Required for confidence parameter in locateCenterOnScreen)
pkgs = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui', 'Pillow', 'opencv-python']
try:
    print("Checking dependencies...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + pkgs)
    import pyautogui
except Exception as e:
    sys.exit(f"Setup failed: {e}")

SCREEN_DIR = "screenshots"
os.makedirs(SCREEN_DIR, exist_ok=True)

# --- 2. HELPER FUNCTIONS ---
def run_action(action, val, wait=0, shot=None, **kwargs):
    """Handles key presses, writing text, and screenshots."""
    if action == 'press': pyautogui.press(val, **kwargs)
    elif action == 'write': pyautogui.write(val)
    
    if wait > 0: time.sleep(wait)
    
    if shot:
        path = os.path.join(SCREEN_DIR, shot)
        pyautogui.screenshot(path)
        print(f"Screenshot: {path}")

def find_and_click(image, wait=0, clicks=1):
    """Locates an image and clicks it. Returns True if found."""
    try:
        loc = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if loc:
            print(f"Clicked {image} at {loc}")
            # interval=1 ensures 1 second pause between double clicks if clicks=2
            pyautogui.click(loc, clicks=clicks, interval=1) 
            time.sleep(wait)
            return True
    except Exception:
        print(f"Exception in finding image {image}: e ")
    return False

def launch_app(name):
    """Launches an exe and waits."""
    path = os.path.abspath(name)
    print(f"Launching: {path}")
    if os.path.exists(path):
        subprocess.Popen(path, shell=True)
        time.sleep(10)
    else:
        print(f"Error: {path} not found.")

# --- 3. AUTOMATION SEQUENCE ---

# === PART 1: SECOND APP ===
launch_app("install-3.exe")
run_action(None, None, wait=0, shot="1.png")
first_steps = [
    ('press', 'tab', 1, None),
    ('press', 'up', 1, None),
    ('press', 'enter', 1, None),
    ('press', 'enter', 1, None),
    ('press', 'enter', 10, "1a.png"),
    ('press', 'tab', 1, None),
    ('press', 'space', 1, None),
    ('press', 'enter', 10, None),
    ('press', 'right', 1, "1b.png"),
    ('press', 'right', 1, "1c.png"),
    ('press', 'tab', 1, "1d.png"),
    ('press', 'space', 1, "1e.png"),
    ('press', 'tab', 1, "1f.png"),
    ('write', 'AkshayKumarPandey', 1, None),
    ('press', 'tab', 1, "1g.png")
]

# Run the sequence
for step in first_steps: run_action(*step)

# === PART 3: Third APP ===
launch_app("install-1.exe")

third_steps = [
    ('press', 'enter', 10, None, {'presses': 3, 'interval': 0.5}),
    ('press', 'enter', 1, None, {}),
    ('press', 'tab', 1, None, {}),
    ('press', 'enter', 1, None, {}),
    ('press', 'tab', 0, None, {'presses': 3, 'interval': 0.5}),
    ('write', "newsletter0718"+"@"+"gmail.com", 0, None, {}),
    ('press', 'tab', 0, None, {}),
    ('write', "NewsEarn"+"@"+"23#", 1, None, {}),
    ('press', 'tab', 1, None, {}),
    ('press', 'enter', 10, "3.png", {}),
]

for action, val, wait, shot, kwargs in third_steps:
    run_action(action, val, wait, shot, **kwargs)

# Image Check for First App (Clicks twice with 1s interval)
find_and_click("install-10.png", wait=10, clicks=1)
run_action(None, None, wait=0, shot="3b.png")
find_and_click("install-11.png", wait=10, clicks=1)
run_action(None, None, wait=0, shot="3c.png")
find_and_click("install-11.png", wait=10, clicks=1)
run_action(None, None, wait=0, shot="3d.png")

# === PART 2: Second APP ===
launch_app("install-2.exe")
# Steps: (Action, Value, Wait, Screenshot, OptionalArgs)
second_steps = [
    ('press', 'tab', 1, None),
    ('write', 'zPeYuQdg5Dj0UsxrGv038ARbngn+Tnwo8y6Y7S8iJ3w=', 0, "2a.png")
]

for step in second_steps: run_action(*step)

# Image Check for Second App
if find_and_click("install-21.png", wait=10):
    pass 
run_action(None, None, wait=0, shot="2b.png")

print("Automation completed successfully!")
