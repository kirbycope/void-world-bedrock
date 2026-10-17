"""Builds build/void-world-bedrock.mcworld from the world committed in the repository, so nothing is zipped by hand.

The world is the void-world-bedrock.mcworld committed at the root of the repository, which this reads and never writes. Its
level.dat is packed with every experiment turned off, since nothing in the world needs one, and db/CURRENT with a
bare LF ending, which LevelDB requires. The build goes to build/, which git ignores.

    python tools/build_world.py            # writes build/void-world-bedrock.mcworld

What Minecraft requires of the zip: entries at the root (no wrapping folder), forward slashes, Deflate or Store, no zip64.
"""
import io
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from level_dat import without_experiments  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "void-world-bedrock.mcworld")
OUTPUT = os.path.join(ROOT, "build", "void-world-bedrock.mcworld")
STAMP = (2026, 1, 1, 0, 0, 0)


def build() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(SOURCE) as source, zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, allowZip64=False) as out:
        for info in sorted(source.infolist(), key=lambda i: i.filename):
            if info.is_dir(): continue
            name = info.filename.replace("\\", "/")
            data = source.read(info)
            if name == "level.dat": data = without_experiments(data)
            if name == "db/CURRENT": data = data.replace(b"\r\n", b"\n")
            entry = zipfile.ZipInfo(name, STAMP); entry.external_attr = 0o666 << 16
            out.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


if __name__ == "__main__":
    data = build()
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    open(OUTPUT, "wb").write(data)
    print(f"wrote {os.path.relpath(OUTPUT, ROOT)} ({len(data)} bytes)")
