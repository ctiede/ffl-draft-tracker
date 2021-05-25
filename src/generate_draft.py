import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os import path
from players import Player


def format_name(name):
    try_split = name.split(' ')
    if len(try_split) > 1:
        return '\n'.join(try_split)
    else:
        return name


def load_draft(args):
    draft_defs = dict()
    draft_file = './draft-files/draft_{}.py'.format(args.year)
    exec(open(draft_file).read(), draft_defs)
    players   = dict()
    positions = dict()
    for (manager, draft) in draft_defs['draft'].items():
        players  .update({manager : dict()})
        positions.update({manager : dict()})
        for (round, player) in draft.items():
            players  [manager].update({round : format_name(player.name)})
            positions[manager].update({round : player.position.value})
    return draft_defs['year'], players, positions


def build_draft_board(args, players, positions):
    num_managers = len(players)
    num_rounds   = len(players[list(players)[0]])
    player_df    = pd.DataFrame(data=players)
    position_df  = pd.DataFrame(data=positions)
    print(player_df)
    plt.figure(figsize=[9,7])
    cmap = sns.color_palette('deep', 6)
    ax = sns.heatmap(position_df, annot=player_df, cmap=cmap, linewidths=0.2, cbar=False, fmt='')
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.tick_params(left=False, bottom=False, top=False)
    plt.subplots_adjust(top=0.95, bottom=0.01, left=0.05, right=0.98)
    figname = './draft-boards/draft_board_{}.pdf'.format(int(args.year))
    if path.exists(figname) is False or args.overwrite is True:
        plt.savefig(figname)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int, help="Year to retrieve draft file of format `draft_{year}.py`")
    parser.add_argument('--draft-file', default=None, help="Specify draft file if not of regular format `draft_{year}.py` ")
    parser.add_argument('--overwrite', action='store_true', help="Overwrite exist draftboard pdf")
    args = parser.parse_args()

    year, players, positions = load_draft(args)
    print('Warmup and Technique Fantasy Draft : {}'.format(year))
    build_draft_board(args, players, positions)
