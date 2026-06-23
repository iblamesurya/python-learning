# Day 15 - *args, **kwargs, and Unpacking

# --- *args: variable positional arguments ---
print("=== *args ===")

def add_all(*args):
    """Takes any number of arguments and returns their sum"""
    print(f"  Received {len(args)} args: {args}")
    return sum(args)

print(f"add_all(1, 2): {add_all(1, 2)}")
print(f"add_all(1, 2, 3, 4, 5): {add_all(1, 2, 3, 4, 5)}")

# --- **kwargs: variable keyword arguments ---
print("\n=== **kwargs ===")

def build_profile(name, **kwargs):
    """Build a user profile from keyword arguments"""
    profile = {"name": name}
    profile.update(kwargs)
    return profile

surya = build_profile("Surya", age=22, city="Hyderabad", skill="Python")
print(f"Profile: {surya}")

# --- combining *args and **kwargs ---
print("\n=== Combined ===")

def log_message(level, *args, **kwargs):
    message = " ".join(str(a) for a in args)
    extras = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    print(f"[{level.upper()}] {message}" + (f" ({extras})" if extras else ""))

log_message("info", "Server started", "on port", 8080, host="localhost")
log_message("error", "Connection failed", retries=3, timeout=30)

# --- unpacking ---
print("\n=== Unpacking ===")

# list unpacking
coords = [10, 20, 30]
x, y, z = coords
print(f"x={x}, y={y}, z={z}")

# star unpacking
first, *middle, last = [1, 2, 3, 4, 5, 6, 7]
print(f"first={first}, middle={middle}, last={last}")

# unpack into function call
def greet(name, greeting, punctuation):
    return f"{greeting}, {name}{punctuation}"

args_list = ["Surya", "Hey", "!"]
print(greet(*args_list))

kwargs_dict = {"name": "Surya", "greeting": "Namaste", "punctuation": "!!"}
print(greet(**kwargs_dict))

# --- practical: flexible config builder ---
print("\n=== Practical: Config Builder ===")

def create_config(app_name, *, debug=False, version="1.0", **extra):
    """Keyword-only args after * plus extra kwargs"""
    config = {
        "app": app_name,
        "debug": debug,
        "version": version,
        **extra
    }
    return config

cfg = create_config("MyApp", debug=True, version="2.1", port=3000, db="postgres")
for key, val in cfg.items():
    print(f"  {key}: {val}")
