import sys

sys.path.append("../")
from pycore.tikzeng import *

SCALE_HEIGHT = 1.0 / 2
SCALE_WIDTH = 1/4 / 2
SCALE_FCNN = 3/4 / 2

# defined your arch
arch = [
    to_head(".."),
    to_cor(),
    to_begin(),
    to_input(
        "internal_map.png",
        to=f"({-5*SCALE_WIDTH*4},0,0)",
        width=SCALE_HEIGHT * 12,
        height=SCALE_HEIGHT * 12,
        name="map",
    ),
    to_Conv(
        "input",
        60,
        3,
        offset="(0,0,0)",
        to="(0,0,0)",
        height=SCALE_HEIGHT * 60,
        depth=SCALE_HEIGHT * 60,
        width=SCALE_WIDTH * 3,
        caption="Input $\\tilde{Z}_t$",
    ),
    to_Conv(
        "conv1",
        56,
        32,
        offset=f"({5.5*SCALE_WIDTH*4},0,0)",
        to="(input-east)",
        height=SCALE_HEIGHT * 56,
        depth=SCALE_HEIGHT * 56,
        width=SCALE_WIDTH * 32,
        caption="Convolution 5x5 + ReLU",
    ),
    to_connection("input", "conv1"),
    to_Pool(
        "pool1",
        offset="(0,0,0)",
        to="(conv1-east)",
        height=SCALE_HEIGHT * 28,
        depth=SCALE_HEIGHT * 28,
        width=SCALE_WIDTH * 32,
    ),
    to_Conv(
        "conv2",
        24,
        64,
        offset=f"({2.5*SCALE_WIDTH*5},0,0)",
        to="(pool1-east)",
        height=SCALE_HEIGHT * 24,
        depth=SCALE_HEIGHT * 24,
        width=SCALE_WIDTH * 64,
    ),
    to_connection("pool1", "conv2"),
    to_Pool(
        "pool2",
        offset="(0,0,0)",
        to="(conv2-east)",
        height=SCALE_HEIGHT * 12,
        depth=SCALE_HEIGHT * 12,
        width=SCALE_WIDTH * 64,
        caption="\\begin{flushright}Max-Pool\\\\2x2\\end{flushright}",
    ),
    to_Conv(
        "conv3",
        8,
        64,
        offset=f"({1*SCALE_WIDTH*8},0,0)",
        to="(pool2-east)",
        height=SCALE_HEIGHT * 8,
        depth=SCALE_HEIGHT * 8,
        width=SCALE_WIDTH * 64,
    ),
    to_connection("pool2", "conv3"),
    to_Pool(
        "pool3",
        offset="(0,0,0)",
        to="(conv3-east)",
        height=SCALE_HEIGHT * 4,
        depth=SCALE_HEIGHT * 4,
        width=SCALE_WIDTH * 64,
    ),
    to_Sum(
        "sum1",
        offset=f"({1*SCALE_WIDTH*10},0,0)",
        to="(pool3-east)",
        radius=2,
        opacity=0.6,
    ),
    to_SoftMax(
        "obs",
        4,
        offset="(-1,3,0)",
        to="(sum1-east)",
        height=1,
        depth=SCALE_FCNN * 8,
        width=1,
        caption="Input $O_t$\\newline",
    ),
    to_connection("pool3", "sum1"),
    to_connection("obs", "sum1"),
    to_SoftMax(
        "soft1",
        256,
        offset=f"({1.5*SCALE_FCNN*2},0,0)",
        to="(sum1-east)",
        height=1,
        depth=SCALE_FCNN  * 256,
        width=1,
        caption="Extracted Features",
    ),
    to_connection("sum1", "soft1"),
    to_SoftMax(
        "soft2",
        128,
        offset=f"({1.5*SCALE_FCNN*2},0,0)",
        to="(soft1-east)",
        height=1,
        depth=SCALE_FCNN  * 128,
        width=1,
        caption="Prediction Head",
    ),
    to_connection("soft1", "soft2"),
    to_SoftMax(
        "soft3",
        64,
        offset=f"({1.5*SCALE_FCNN*2},0,0)",
        to="(soft2-east)",
        height=1,
        depth=SCALE_FCNN  * 64,
        width=1,
    ),
    to_connection("soft2", "soft3"),
    to_SoftMax(
        "soft4",
        2,
        offset=f"({1.5*SCALE_FCNN*2},0,0)",
        to="(soft3-east)",
        height=1,
        depth=SCALE_FCNN * 4,
        width=1,
        caption="Output",# $\\mu, \\ln \\sigma$", #$\\hat{q}_{\\mathbf{\\phi}}$
    ),
    to_connection("soft3", "soft4"),
    to_end(),
]


def main():
    namefile = str(sys.argv[0]).split(".")[0]
    to_generate(arch, namefile + ".tex")


if __name__ == "__main__":
    main()
