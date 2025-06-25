# REK - RoLib Extension Kit

**REK** (RoLib Extension Kit) is a Python program designed to simplify the creation of packages for the [RoLib](https://github.com/blockguard-sf/RoLib) library. It automates the generation of a base structure for RoLib packages using information provided by the user.

## Main Features

- Automatically generates the folder and file structure of a RoLib package.
- Interactively collects package metadata:
  - Package name
  - Description
  - Author
  - License
  - Git integration (optional)
  - Target directory

---

## Installation

### Clone from GitHub

```bash
git clone https://github.com/blockguard-sf/REK
```

### Install via installer script

1. Run the `REK-Installer.sh` file:
   ```bash
   ./REK-Installer.sh
   ```

2. Follow the installer instructions.
3. Enter the directory where you want to install REK.

---

## Usage

### If you only cloned the repository:
```bash
cd YourREKDirectory/src
python rek
```

### If you used the installer:
```bash
cd YourREKDirectory/
python rek
```

### Available commands

| Command              | Description                 |
|----------------------|-----------------------------|
| `python rek`         | Launches REK in normal mode |
| `python rek -help`   | Displays help               |
| `python rek -d`      | Launches REK in debug mode  |

---

## Generated Structure

The generated template follows RoLib standards and is ready to be versioned and shared.

---

© [BlockGuard Software Foundation](https://github.com/blockguard-sf)
