from matplotlib import pyplot as plt
import calliope
import pandas as pd
from pathlib import Path

plt.rcParams["font.size"] = "16"

NAME_MODEL = "model_1"
ORDER = ["pv", "wind", "gas_pp"]

# define path to load results from and to save plots to
path_results = Path(__file__).parent.parent / NAME_MODEL / "results" / "results.nc"
path_plots = Path(__file__).parent.parent / NAME_MODEL / "plots"

# # load and prepare results
model = calliope.read_netcdf(path_results)
flow_out = model.results.flow_out.to_dataframe().dropna().reset_index()
flow_out = flow_out.drop(columns="carriers")
flow_out = pd.pivot(
    flow_out, index=["timesteps"], values="flow_out", columns=["nodes", "techs"]
)

flow_in = model.results.flow_in.to_dataframe().dropna().reset_index()
flow_in = flow_in.drop(columns="carriers")
flow_in = pd.pivot(
    flow_in, index=["timesteps"], values="flow_in", columns=["nodes", "techs"]
)

nodes = list(model.inputs.nodes.to_series())
color = model.inputs.color.to_series().to_dict()

# plot and save
fig, axs = plt.subplots(len(nodes), 1, figsize=(12, 5 * len(nodes)), dpi=120)
axs = axs if len(nodes) > 1 else [axs]
for node, ax in zip(nodes, axs):
    flow_in_node = flow_in.loc[:, node]
    flow_out_node = flow_out.loc[:, node][ORDER]

    ax = flow_in_node.plot(
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
    ax = flow_out_node.plot(ax=ax, kind="bar", color=color, stacked=True, width=1)
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5))
    ax.set_ylabel("Power generation and demand")
    ax.set_title(node)
    # switch off xticks and xlabel
    ax.set_xticks([])
    ax.set_xlabel("")

# ax.set_xticks(flow_in_node.index)
ax.set_xlabel("Time")
ax.set_xticks(range(len(flow_in_node.index)))
ax.set_xticklabels(flow_in_node.index, rotation=45, ha="right")
fig.suptitle("Dispatch plot")

plt.savefig(path_plots / "dispatch.png", bbox_inches="tight")
