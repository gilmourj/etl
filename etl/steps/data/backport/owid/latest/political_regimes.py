from etl.backport_helpers import create_dataset


def run(dest_dir: str) -> None:
    create_dataset(dest_dir, "5426_political_regimes").save()


if __name__ == "__main__":
    run("/tmp/5426_political_regimes")
