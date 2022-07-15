"""Depenndency ratio table"""
import pandas as pd


# Initial settings
COLUMNS_ID = {
    "location": "location",
    "time": "year",
    "variant": "variant",
    "sex": "sex",
}
COLUMNNS_METRICS = {
    "annual_total_dep__ratio__0_14__and__65plus__15_64__pct": {
        "name": "dependency_ratio_total",
    },
    "annual_child_dep__ratio__0_14__15_64__pct": {
        "name": "dependency_ratio_child",
    },
    "annual_old_age_dep__ratio__65plus__15_64__pct": {
        "name": "dependency_ratio_old",
    },
}
MAPPINNG_SEX = {
    "Both": "all",
    "Female": "female",
    "Male": "male",
}
COLUMNS_ORDER = ["location", "year", "metric", "sex", "age", "variant", "value"]


def process(df: pd.DataFrame, country_std: str) -> pd.DataFrame:
    df = df.reset_index()
    df = df.melt(COLUMNS_ID.keys(), COLUMNNS_METRICS.keys(), "metric", "value")
    # Add columns, rename columns
    df = df.rename(columns=COLUMNS_ID)
    df = df.assign(
        age="none",
        sex=df.sex.map(MAPPINNG_SEX),
        metric=df.metric.map({k: v["name"] for k, v in COLUMNNS_METRICS.items()}),
        variant=df.variant.apply(lambda x: x.lower()),
        location=df.location.map(country_std),
        value=(df.value).astype(float).round(2),
    )
    # Column order
    df = df[COLUMNS_ORDER]
    # Drop unmapped regions
    df = df.dropna(subset=["location"])
    return df
