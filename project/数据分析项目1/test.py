import calendar

import matplotlib.pyplot as mp
import numpy as np

mp.figure('Feature Importance', facecolor='lightgray')
mp.title('AB FI', fontsize=12)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# mp.xticks(np.arange(0, 1, step=0.2))
# mp.xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
mp.xticks(np.arange(12), calendar.month_name[1:13], rotation=90)  # rotation代表lable显示的旋转角度。
mp.colorbar()
mp.legend()
mp.tight_layout()
mp.show()
