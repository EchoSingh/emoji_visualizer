import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from emoji import EMOJI_DATA

def visualize_emojis():
    """Visualize all emojis in a grid."""
    emojis = list(EMOJI_DATA.keys())
    num_emojis = len(emojis)
    grid_size = int(num_emojis**0.5) + 1

    font_path = "C:\\Users\\adity\\Downloads\\Noto_Color_Emoji\\NotoColorEmoji-Regular.ttf"  # Change to your font path
    prop = FontProperties(fname=font_path)

    fig, ax = plt.subplots(grid_size, grid_size, figsize=(10, 10))
    ax = ax.flatten()

    for i in range(num_emojis):
        ax[i].text(0.5, 0.5, emojis[i], fontsize=12, ha='center', va='center', fontproperties=prop)
        ax[i].axis('off')

    for i in range(num_emojis, len(ax)):
        ax[i].axis('off')

    plt.tight_layout()
    plt.show()
