"""This script has been autogenerated by `walkthrough walden`."""

from pathlib import Path

import click
from owid.walden import Dataset


@click.command()
@click.option(
    "--upload/--skip-upload",
    default=True,
    type=bool,
    help="Upload dataset to Walden",
)
def main(upload: bool) -> None:
    metadata = Dataset.from_yaml(
        Path(__file__).parent / "{{cookiecutter.short_name}}.meta.yml"
    )

    # download dataset from source_data_url and add the local file to Walden's cache in ~/.owid/walden
    dataset = Dataset.download_and_create(metadata)

    # upload it to S3
    if upload:
        dataset.upload(public=True)

    # update PUBLIC walden index with metadata
    dataset.save()


if __name__ == "__main__":
    main()