#!/usr/bin/env python3
"""Build privacy-safe web images and photography metadata from local originals."""

from __future__ import annotations

import io
import json
import os
from datetime import datetime
from pathlib import Path

from PIL import ExifTags, Image, ImageCms, ImageOps


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "_photo_inbox"
OUTPUT = ROOT / "assets" / "photography"
DATA_FILE = ROOT / "_data" / "photography.json"
HEIC_PREVIEW = Path(
    os.environ.get(
        "PHOTOGRAPHY_HEIC_PREVIEW",
        "/tmp/photography-heic-preview/IMG_4999.heic.png",
    )
)

CAMERA_NAMES = {
    "ILCE-7C": "Sony α7C",
    "ILCE-7CM2": "Sony α7C II",
    "ILCE-7RM2": "Sony α7R II",
    "iPhone 16": "Apple iPhone 16",
}

LENS_NAMES = {
    "E 28-200mm F2.8-5.6 A071": "Tamron 28–200mm F2.8–5.6",
    "FE 55mm F1.8 ZA": "Sony Zeiss FE 55mm F1.8 ZA",
    "FE PZ 16-35mm F4 G": "Sony FE PZ 16–35mm F4 G",
    "45mm F2.8 DG DN | Contemporary 019": "Sigma 45mm F2.8 DG DN Contemporary",
    "iPhone 16 back dual wide camera 5.96mm f/1.6": "iPhone 16 Main Camera",
}

HEIC_METADATA = {
    "Make": "Apple",
    "Model": "iPhone 16",
    "LensModel": "iPhone 16 back dual wide camera 5.96mm f/1.6",
    "FNumber": 1.6,
    "ExposureTime": 0.0024449877750611247,
    "ISOSpeedRatings": 50,
    "FocalLength": 5.960000038146973,
    "DateTimeOriginal": "2025:06:28 20:55:00",
}

LOCATIONS = [
    {
        "slug": "bali",
        "title": "Bali Island",
        "eyebrow": "Indonesia · May 2026",
        "description": "Sea light, surf, and quiet figures along the island's southern coast.",
        "cover": "bali-01",
        "photos": [
            ("Bali Island/Bali - 1 of 4.jpeg", "bali-01", "A boat tracing a circle across turquoise water", "Bali Island"),
            ("Bali Island/Bali - 2 of 4.jpeg", "bali-02", "Surfers waiting at the shoreline in Bali", "Bali Island"),
            ("Bali Island/Bali - 3 of 4.jpeg", "bali-03", "Figures crossing a sunlit sea in Bali", "Bali Island"),
            ("Bali Island/Bali - 4 of 4.jpeg", "bali-04", "Sunset touching the horizon over Bali", "Bali Island"),
        ],
    },
    {
        "slug": "turkiye",
        "title": "Türkiye",
        "eyebrow": "Cappadocia · Antalya · Istanbul · 2025",
        "description": "Stone valleys, Mediterranean light, and Istanbul's layered skyline at blue hour.",
        "cover": "turkiye-istanbul-02",
        "photos": [
            ("Turkey/Cappadocia - 1 of 2.jpeg", "turkiye-cappadocia-01", "Looking over Cappadocia's valleys", "Cappadocia"),
            ("Turkey/Cappadocia - 2 of 2.jpeg", "turkiye-cappadocia-02", "Cappadocia framed by a rock opening", "Cappadocia"),
            ("Turkey/Antalya - 1 of 3.jpeg", "turkiye-antalya-01", "Antalya's old harbor and Mediterranean coast", "Antalya"),
            ("Turkey/Antalya - 2 of 3.jpeg", "turkiye-antalya-02", "A quiet figure beside the sunlit Mediterranean", "Antalya"),
            ("Turkey/Antalya - 3 of 3.jpeg", "turkiye-antalya-03", "A fruit stall arranged in geometric patterns", "Antalya"),
            ("Turkey/Istanbual - 1 of 3.jpeg", "turkiye-istanbul-01", "Mosques rising above the Bosphorus", "Istanbul"),
            ("Turkey/Istanbual - 2 of 3.jpeg", "turkiye-istanbul-02", "An Istanbul mosque against a glowing sky", "Istanbul"),
            ("Turkey/Istanbual - 3 of 3.jpeg", "turkiye-istanbul-03", "Istanbul's domes and minarets at blue hour", "Istanbul"),
        ],
    },
    {
        "slug": "hong-kong",
        "title": "Hong Kong",
        "eyebrow": "Hong Kong · 2023–2024",
        "description": "Mountain ridges, neighborhood light, and the city's quieter edges.",
        "cover": "hong-kong-ridge",
        "photos": [
            ("Hong Kong/IMG_0261.JPG", "hong-kong-ridge", "A hiker crossing a Hong Kong coastal ridge", "Lantau Island"),
            ("Hong Kong/IMG_0265.JPG", "hong-kong-shore", "A lone figure walking along a Hong Kong beach", "Lantau Island"),
            ("Hong Kong/DSC00530.JPEG", "hong-kong-terminal", "Movement and light inside a Hong Kong terminal", "Hong Kong"),
            ("Hong Kong/DSC00585.JPEG", "hong-kong-neon", "A neon-lit street after dusk in Hong Kong", "Hong Kong"),
        ],
    },
    {
        "slug": "boston",
        "title": "Boston",
        "eyebrow": "Massachusetts · July 2026",
        "description": "Small encounters along the water and green spaces of the city.",
        "cover": "boston-water-taxi",
        "photos": [
            ("Boston/DSC03268.JPEG", "boston-geese", "Canada geese gathering on a Boston green", "Boston"),
            ("Boston/DSC03283.JPEG", "boston-water-taxi", "A yellow water taxi waiting by the dock", "Boston Harbor"),
        ],
    },
    {
        "slug": "london",
        "title": "London",
        "eyebrow": "United Kingdom · June 2025",
        "description": "St Paul's, the Shard, and the geometry of streets and reflections.",
        "cover": "london-st-pauls-reflection",
        "photos": [
            ("London/London - 3 of 12.JPEG", "london-st-pauls-street", "St Paul's Cathedral at the end of a London street", "City of London"),
            ("London/London - 5 of 12.JPEG", "london-st-pauls-reflection", "St Paul's Cathedral framed by modern reflections", "City of London"),
            ("London/IMG_4999.heic", "london-shard", "The Shard rising between dark city walls", "London Bridge"),
        ],
    },
]


def read_metadata(path: Path) -> dict:
    if path.suffix.lower() == ".heic":
        return HEIC_METADATA.copy()

    with Image.open(path) as image:
        exif = image.getexif()
        values = {ExifTags.TAGS.get(key, key): value for key, value in exif.items()}
        exif_ifd = exif.get_ifd(ExifTags.IFD.Exif)
        values.update(
            {ExifTags.TAGS.get(key, key): value for key, value in exif_ifd.items()}
        )
        return values


def open_image(path: Path) -> Image.Image:
    source = HEIC_PREVIEW if path.suffix.lower() == ".heic" else path
    if not source.exists():
        raise FileNotFoundError(f"Missing image source: {source}")

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened)
        image.load()
        image = image.copy()

    icc_profile = image.info.get("icc_profile")
    if icc_profile:
        try:
            source_profile = ImageCms.ImageCmsProfile(io.BytesIO(icc_profile))
            target_profile = ImageCms.createProfile("sRGB")
            image = ImageCms.profileToProfile(
                image,
                source_profile,
                target_profile,
                outputMode="RGB",
            )
        except (OSError, ValueError):
            image = image.convert("RGB")
    else:
        image = image.convert("RGB")

    return image


def save_variant(
    image: Image.Image,
    destination: Path,
    max_size: tuple[int, int],
    quality: int,
) -> tuple[int, int]:
    variant = image.copy()
    variant.thumbnail(max_size, Image.Resampling.LANCZOS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    variant.save(
        destination,
        "JPEG",
        quality=quality,
        optimize=True,
        progressive=True,
    )
    return variant.size


def format_number(value: float) -> str:
    return str(int(round(value))) if abs(value - round(value)) < 0.01 else f"{value:.1f}"


def format_shutter(value: float) -> str:
    if value <= 0:
        return ""
    if value < 1:
        return f"1/{round(1 / value)} s"
    return f"{format_number(value)} s"


def formatted_metadata(values: dict) -> dict:
    model = str(values.get("Model", "")).strip()
    lens_model = str(values.get("LensModel", "")).strip()
    aperture = float(values.get("FNumber", 0) or 0)
    shutter = float(values.get("ExposureTime", 0) or 0)
    iso = int(values.get("ISOSpeedRatings", 0) or 0)
    focal_length = float(values.get("FocalLength", 0) or 0)
    captured = str(values.get("DateTimeOriginal", "")).strip()

    try:
        captured_date = datetime.strptime(captured, "%Y:%m:%d %H:%M:%S")
        date_label = captured_date.strftime("%b %d, %Y").replace(" 0", " ")
    except ValueError:
        date_label = captured

    return {
        "camera": CAMERA_NAMES.get(model, model),
        "lens": LENS_NAMES.get(lens_model, lens_model),
        "aperture": f"f/{format_number(aperture)}" if aperture else "",
        "shutter": format_shutter(shutter),
        "iso": f"ISO {iso}" if iso else "",
        "focal_length": f"{format_number(focal_length)} mm" if focal_length else "",
        "date": date_label,
    }


def build() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    albums = []

    for location in LOCATIONS:
        album = {
            key: location[key]
            for key in ("slug", "title", "eyebrow", "description", "cover")
        }
        album["photos"] = []

        for relative_path, photo_id, alt, sublocation in location["photos"]:
            source = INBOX / relative_path
            if not source.exists():
                raise FileNotFoundError(f"Missing original: {source}")

            image = open_image(source)
            full_path = OUTPUT / location["slug"] / "full" / f"{photo_id}.jpg"
            thumb_path = OUTPUT / location["slug"] / "thumb" / f"{photo_id}.jpg"
            full_size = save_variant(image, full_path, (2000, 2000), 84)
            thumb_size = save_variant(image, thumb_path, (900, 900), 78)
            details = formatted_metadata(read_metadata(source))

            album["photos"].append(
                {
                    "id": photo_id,
                    "src": f"/assets/photography/{location['slug']}/full/{photo_id}.jpg",
                    "thumb": f"/assets/photography/{location['slug']}/thumb/{photo_id}.jpg",
                    "alt": alt,
                    "caption": alt,
                    "sublocation": sublocation,
                    "width": full_size[0],
                    "height": full_size[1],
                    "thumb_width": thumb_size[0],
                    "thumb_height": thumb_size[1],
                    "orientation": "landscape"
                    if full_size[0] >= full_size[1]
                    else "portrait",
                    **details,
                }
            )

        cover_photo = next(
            photo for photo in album["photos"] if photo["id"] == album["cover"]
        )
        album["cover_src"] = cover_photo["src"]
        album["cover_thumb"] = cover_photo["thumb"]
        albums.append(album)

    DATA_FILE.write_text(
        json.dumps(albums, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
