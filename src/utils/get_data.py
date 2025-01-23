import gdown


def from_gdrive(url: str, filename: str) -> None:
    gdown.download(url=url, output=filename, quiet=False)
