import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt
import math
import wx
from matplotlib import rcParams
import matplotlib
from method.utils import chms_logger

logger = chms_logger.set_operate_logger(__name__)
matplotlib.interactive(True)
matplotlib.use('WXAgg')
rcParams.update({'figure.autolayout': True})


class YearGraph(wx.Panel):
    def __init__(self, parent, year_accounting_list):
        wx.Panel.__init__(self, parent=parent)
        plt.style.use('bmh')
        year_list = sorted(list(set([year_accounting[0] for year_accounting in year_accounting_list])))
        dict_money = {year: 0 for year in year_list}
        for index in range(len(year_accounting_list)):
            dict_money[year_accounting_list[index][0]] += int(year_accounting_list[index][1])
        money_list = [dict_money[years] for years in year_list]
        ave_yy = [int(np.average(money_list)) for _ in range(len(year_list))]

        # matplotlib figure
        self.figure = Figure()
        self.subplot = self.figure.add_subplot(111)
        self.subplot.plot(year_list, money_list, marker='o', label=u'課金額')
        self.subplot.plot(year_list, ave_yy, marker='o', label=u'平均課金額')
        self.subplot.legend(bbox_to_anchor=(1, -0.1), loc='upper right', ncol=2)

        # canvas
        self.canvas = FigureCanvasWxAgg(self, wx.ID_ANY, self.figure)
        self.canvas.SetBackgroundColour(wx.Colour(100, 255, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, flag=wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
