from matplotlib import pyplot as plt
import calliope
import pandas as pd
from pathlib import Path


NAME_MODEL = "model_2"

# define path to load results from and to save plots to
path_results = Path(__file__).parent.parent / NAME_MODEL / "results" / "results.nc"
path_plots = Path(__file__).parent.parent / NAME_MODEL / "plots"

# load and prepare results
model = calliope.read_netcdf(path_results)
flow_out = model.results.flow_out.sel(nodes="CHE").to_dataframe().dropna().reset_index()
flow_out = flow_out.drop(columns=["nodes", "carriers"])
flow_out = pd.pivot(flow_out, index=["timesteps"], values="flow_out", columns="techs")

flow_in = model.results.flow_in.sel(nodes="CHE").to_dataframe().dropna().reset_index()
flow_in = flow_in.drop(columns=["nodes", "carriers"])
flow_in = pd.pivot(flow_in, index=["timesteps"], values="flow_in", columns="techs")
color = model.inputs.color.to_series().to_dict()

# plot and save
fig, ax = plt.subplots(figsize=(8, 3), dpi=120)
ax = flow_in.plot(
    ax=ax,
    kind="line",
    color=color,
    linewidth=4,
    linestyle="",
    marker="_",
    mew=2,
    markersize=15,
    use_index=False,
)
ax = flow_out.plot(ax=ax, kind="bar", color=color, stacked=True, width=1)
ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5))
ax.set_xlabel("Time")
ax.set_ylabel("Power generation and demand")
ax.set_title("Dispatch plot for CHE")

plt.savefig(path_plots / "dispatch.png", bbox_inches="tight")
