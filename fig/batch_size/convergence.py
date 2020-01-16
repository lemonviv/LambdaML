import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np


#matplotlib.rcParams['font.family'] = "sans-serif"
#matplotlib.rcParams['font.sans-serif'] = "Comic Sans MS"
#matplotlib.rcParams['font.sans-serif'] = "Helvetica"
matplotlib.rcParams['font.style'] = "italic"
matplotlib.rcParams['font.weight'] = "bold"

matplotlib.rcParams['lines.linewidth'] = 3

#matplotlib.rcParams['axes.linewidth'] = 2
#matplotlib.rcParams['axes.edgecolor'] = 'Grey'
matplotlib.rcParams['axes.titlesize'] = 10
matplotlib.rcParams['figure.titleweight'] = 'bold'

matplotlib.rcParams['axes.labelsize'] = 12
matplotlib.rcParams['xtick.labelsize'] = 7
matplotlib.rcParams['ytick.labelsize'] = 6

#matplotlib.rcParams['hatch.linewidth'] = 0.1

matplotlib.rcParams['legend.fontsize'] = 6
matplotlib.rcParams['legend.edgecolor'] = 'Black'


hatches = ('', '**', '++', 'oo', '', '*', 'o', '.', 'O')
colors = ['Red', 'Skyblue', 'Orange', 'LightGrey', 'MediumSlateBlue', 'Tomato', 'Palegreen', 'Azure']

# SketchML, Adam, ZipML
methods = ['batch=10K', 'batch=1K', 'batch=100']

batch10K_time = [11.0693, 24.0635, 37.4493, 50.3778, 63.0248, 76.9139, 91.5786, 104.9062, 118.8242, 133.6197, 146.8182, 160.1805, 173.3149, 186.8998, 199.7228, 213.5177, 226.2654, 240.2631, 253.6133, 266.6198, 279.6308, 293.8732, 307.044, 321.1432, 334.8375, 347.7972, 361.0746, 374.6305, 388.228, 402.7437, 415.9754, 427.9176, 441.3588, 454.589, 468.0321, 481.6141, 494.9695, 508.7619, 522.42, 536.2503, 550.5886, 563.6938, 576.8008, 590.2048, 603.9208, 617.8739, 632.1903, 645.8492, 659.8199, 675.2341, 690.3464, 704.6822, 719.2336, 733.0605, 747.9558, 761.9374, 776.5032, 790.3845, 804.0336, 817.6056, 832.2836, 845.5774, 859.2567, 873.1643]
batch10K_loss = [3.408051, 3.374608, 3.349239, 3.333841, 3.317036, 3.304748, 3.293512, 3.28597, 3.277847, 3.275613, 3.269871, 3.264814, 3.260914, 3.254884, 3.253005, 3.253499, 3.247252, 3.248328, 3.245541, 3.245125, 3.244374, 3.244656, 3.238484, 3.241946, 3.240275, 3.239615, 3.237707, 3.230612, 3.239058, 3.23948, 3.234013, 3.231568, 3.230653, 3.231289, 3.229683, 3.229654, 3.231871, 3.229378, 3.232246, 3.22671, 3.228266, 3.227122, 3.229104, 3.225784, 3.225956, 3.225816, 3.225937, 3.224368, 3.22629, 3.223989, 3.224967, 3.221926, 3.220918, 3.223558, 3.223958, 3.222336, 3.224216, 3.222418, 3.219663, 3.220976, 3.222634, 3.220595, 3.218138, 3.219301]

batch1K_time = [10.7656, 23.0353, 35.7769, 48.8614, 61.9519, 76.0143, 89.3327, 102.2814, 116.1417, 129.476, 142.7478, 155.5572, 168.6885, 182.9242, 195.7, 209.1339, 222.0161, 235.0002, 248.7476, 262.0491, 275.5897, 287.7908, 300.5268, 313.5902, 326.6244, 339.4267, 351.854, 364.6096, 377.8159, 390.8479, 403.6571, 416.2572, 428.3848, 440.983, 453.7203, 466.5825, 479.704, 493.063, 506.2342, 518.5809, 533.1485, 546.1626, 559.7204, 572.9462, 585.4099]
batch1K_loss = [28.827799, 28.572247, 28.471628, 28.414715, 28.374197, 28.340593, 28.314724, 28.291559, 28.274738, 28.258236, 28.244158, 28.233717, 28.224983, 28.215149, 28.208134, 28.200823, 28.19813, 28.19047, 28.18709, 28.184732, 28.18157, 28.179512, 28.175558, 28.17433, 28.172171, 28.171978, 28.169296, 28.169016, 28.168543, 28.171112, 28.166723, 28.16659, 28.16514, 28.164896, 28.164944, 28.16501, 28.164804, 28.166132, 28.164625, 28.165161, 28.165316, 28.167576, 28.16378, 28.164831, 28.164146]
batch1K_loss = [i / 10 for i in batch1K_loss]

batch100_time = [11.504, 26.0882, 40.6063, 55.0805, 68.5784, 81.7444, 95.1633, 109.2805, 121.7582, 137.3232, 150.8277, 164.2213, 177.6039, 190.7803, 204.7005, 217.6576, 231.4659, 244.8824, 259.9039, 275.0842, 290.123, 304.7653, 318.8805, 332.4619, 346.8233, 360.3361, 374.1805, 388.0607, 402.4872, 416.3786, 430.6238, 445.5464, 459.5617, 472.6858, 487.6183, 501.1187, 515.0184, 528.6822, 541.9178, 556.1797, 569.4864, 582.5185, 595.8995, 609.5192, 622.8806, 636.6416, 649.8032, 663.2036, 677.7642, 692.0789, 706.2828, 719.7953, 733.1204, 769.7009, 783.4648, 797.0185, 810.4212, 823.799, 836.8969, 850.1364, 865.0153, 878.2574]
batch100_loss = [282.669952, 281.897614, 281.69754, 281.667969, 281.682587, 281.696564, 281.734863, 281.700714, 281.714935, 281.699097, 281.730194, 281.700928, 281.72226, 281.802673, 281.714386, 281.701202, 281.697784, 281.854828, 281.779175, 281.726288, 281.767487, 281.724823, 281.802155, 281.817017, 281.732208, 281.723877, 281.726166, 281.78476, 281.71048, 281.71344, 281.714661, 281.695343, 281.75058, 282.263062, 281.732056, 281.742889, 281.843048, 281.729156, 281.760742, 281.725403, 281.701874, 281.726654, 281.753967, 281.776764, 281.680847, 281.733032, 281.79483, 281.729004, 281.956543, 281.673767, 281.721252, 281.854523, 281.714722, 281.772919, 281.663239, 281.723541, 281.742279, 281.693909, 281.777069, 281.695923, 281.731537, 281.698761]
batch100_loss = [i / 100 for i in batch100_loss]

plt.figure(figsize=(4, 2.7))

plt.plot(batch10K_time, batch10K_loss, ".-", color=colors[0],  label=methods[0])
plt.plot(batch1K_time, batch1K_loss, "x-", color=colors[1],  label=methods[1])
plt.plot(batch100_time, batch100_loss, "x-", color=colors[2],  label=methods[2])

plt.title("Convergence (Model Average)", fontweight="bold")
plt.ylabel("loss")
plt.xlabel("seconds")
plt.yscale("log")
plt.xlim(0, 1000)
plt.ylim(2.6, 2.8, 3.6)
plt.xticks((0, 500, 1000), ('0', '500', '1000'))
plt.yticks((2.6, 2.8, 3, 3.2, 3.4, 3.6), ('2.6', '2.8', '3', '3.2', '3.4', '3.6'))
plt.legend(bbox_to_anchor=(0, 1), loc=2, ncol=3, shadow=False)

plt.tight_layout()

plt.savefig("convergence.pdf")
#plt.show()