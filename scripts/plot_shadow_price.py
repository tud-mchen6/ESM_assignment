from matplotlib import pyplot as plt
import calliope
from pathlib import Path
from matplotlib.dates import DateFormatter, DayLocator, HourLocator
import sys


name_model = sys.argv[1]

MODELS = ["model_1", "model_2"]
if name_model not in MODELS:
    raise ValueError(f"Model name must be one of {MODELS}")

# define path to load results from and to save plots to
path_results = Path(__file__).parent.parent / name_model / "results" / "results.nc"
path_plots = Path(__file__).parent.parent / name_model / "plots"

# load and prepare results
model = calliope.read_netcdf(path_results)
df = model.results.shadow_price_system_balance.to_dataframe()
df = df.reset_index()
df = df.drop(columns="carriers")

# plot results
fig, ax = plt.subplots(figsize=(8, 3), dpi=120)

for node in df["nodes"].unique():
    df_node = df.loc[df["nodes"] == node]
    ax.step(df_node["timesteps"], df_node["shadow_price_system_balance"], label=node)

ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5))
ax.set_xlabel("Time")
ax.set_ylabel("Shadow price")
ax.set_title("Shadow price of system balance constraint")

ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator())  # by_hour
ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
ax.xaxis.set_tick_params(which="major", pad=15)
ax.xaxis.set_minor_formatter(DateFormatter("%H"))

plt.savefig(path_plots / "shadow_price.png", bbox_inches="tight")
