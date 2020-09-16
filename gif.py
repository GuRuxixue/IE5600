import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import yfinance as yf

import matplotlib.dates as mdate
## Compare US with SG during cov-19
df_yahoo_A=yf.Ticker("^STI")
# print(df_yahoo_A.info.keys())
df_yahoo_B=yf.Ticker("^DJI")
# print(df_yahoo_B.info.keys())
# history_A=df_yahoo_A.history(start="2019-09-01",end="2020-09-01")
# history_B=df_yahoo_B.history(start="2019-09-01",end="2020-09-01")
history_A=df_yahoo_A.history(start="2010-09-01",end="2020-09-01",interval='1wk')
history_B=df_yahoo_B.history(start="2010-09-01",end="2020-09-01",interval='1wk')
fig, axs1 = plt.subplots(figsize=(16, 9))
fig.suptitle('SG v.s.US 10-Year', fontsize=16)
axs2 = axs1.twinx()
e=[]
e1=[]
date = []
date2 = []
# for i in range(522):
#     #print(history_A['Close'][history_A['Close']==history_A['Close'][i]].index.tolist()[0].date())
#
#
#     # date2 = history_B['Close'][history_B['Close'] == history_B['Close'][i]].index.tolist()[0].date()
#
#     axs1.set_xlabel("Date")
#     axs1.set_ylabel('Close', color='tab:blue')
#     axs1.grid(b=True, which='both', axis='both')
#     axs1.tick_params(axis='y', labelcolor='tab:blue')
#     # axs[1].set_title('US')
#     # axs2.set_xlabel("Date")
#     axs1.set_xlim(history_A['Close'].index[0].date(), history_A['Close'].index[512].date())
#     axs1.set_ylim(2000,3800)
#     axs2.set_ylabel('Close', color='tab:orange')
#     axs2.set_ylim(10000, 30000)
#     axs2.tick_params(axis='y', labelcolor='tab:orange')
#     e.append(history_A['Close'][i])
#     e1.append(history_B['Close'][i])
#     date.append(history_A['Close'].index[i].date())
#     date2.append(history_B['Close'].index[i].date())
#     if i==100:
#         axs1.plot(date, e, label='SG', color='tab:blue', linestyle="-")
#         axs2.plot(date2, e1, color='tab:orange', label='US',
#                   linestyle="-")
#         fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=axs1.transAxes)
#     elif i > 100 and i % 6 == 0:
#         axs1.plot(date[i - 6:i + 1], e[i - 6:i + 1], color='tab:blue')
#         axs2.plot(date2[i - 6:i + 1], e1[i - 6:i + 1], color='tab:orange')
#
#         if i == 516:
#             axs1.annotate("", xy=(date[-1], e[-1]), xytext=(date[500], e[500]),
#                           arrowprops=dict(linewidth=3, mutation_scale=20, color='red', arrowstyle="->",
#                                           connectionstyle="arc3"))
#             axs2.annotate("", xy=(date2[-1], e1[-1]), xytext=(date2[500], e1[500]),
#                           arrowprops=dict(linewidth=3, mutation_scale=20, color='red', arrowstyle="->",
#                                           connectionstyle="arc3"))
#             axs1.annotate("", xy=(date[145], e[145]), xytext=(date[70], e[70]),
#                           arrowprops=dict(linewidth=3, mutation_scale=20, color='red', arrowstyle="->",
#                                           connectionstyle="arc3"))
#             axs1.annotate("", xy=(date[400], e[400]), xytext=(date[300], e[300]),
#                           arrowprops=dict(linewidth=3, mutation_scale=20, color='red', arrowstyle="->",
#                                           connectionstyle="arc3"))
#         plt.savefig(str(i)+'.png')
# plt.show()

import imageio
def compose_gif():
    img_paths=[]
    for i in range(102,517,6):
        img_paths.append('10yeargraph/'+str(i)+'.png')
    gif_images = []
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    for i in range(5):
        gif_images.append(imageio.imread('10yeargraph/516.png'))
    imageio.mimwrite("10year.gif",gif_images,format='GIF',loop=0,fps=100)
compose_gif()
axs1.grid(b=True,axis='both')
