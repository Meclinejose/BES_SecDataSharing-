from Main import Run
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import os, logging, warnings, numpy as np
warnings.filterwarnings("ignore")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
logging.getLogger('tensorflow').disabled = True
sg.change_look_and_feel('SystemDefault1')  # for default look and feel

# Designing layout
layout = [[sg.Text("")],
            [sg.Text("\t\t\tKey size\t\t"), sg.Combo(['64', '128'])],
          [sg.Text("\t\t\tBlock size\t"), sg.Combo(['10', '20', '30','40']),
           sg.Text("\t"), sg.Button("START", size=(10, 2))],
          [sg.Text("\t\t\t    MMSDDF\t\t   3LSAA\t\t\tPRMS\t\tFL-BETS\t\tProposed BES_SecDataSharing")],
          [sg.Text('Memory\t\t  '), sg.In(key='11', size=(20, 20)), sg.In(key='12', size=(20, 20)),
           sg.In(key='13', size=(20, 20)), sg.In(key='14', size=(20, 20)), sg.In(key='15', size=(20, 20))],
          [sg.Text('Validation Time\t  '), sg.In(key='21', size=(20, 20)), sg.In(key='22', size=(20, 20)),
           sg.In(key='23', size=(20, 20)), sg.In(key='24', size=(20, 20)), sg.In(key='25', size=(20, 20))],
          [sg.Text('Normalized variance '), sg.In(key='31', size=(20, 20)), sg.In(key='32', size=(20, 20)),
           sg.In(key='33', size=(20, 20)), sg.In(key='34', size=(20, 20)), sg.In(key='35', size=(20, 20))],
            [sg.Text('Conditional Privacy\t  '), sg.In(key='41', size=(20, 20)), sg.In(key='42', size=(20, 20)),
           sg.In(key='43', size=(20, 20)), sg.In(key='44', size=(20, 20)), sg.In(key='45', size=(20, 20))], [sg.Text("\n")],
          [sg.Text("\t\t\t\t\t\t"), sg.Button('Run graph', size=(10, 1)), sg.Text("\t\t"),
           sg.Button('Close', size=(10, 1))], [sg.Text("")]]


# to plot graph
def plot_graph(result_1, result_2, result_3,r4):
    loc, result = [], []
    result.append(result_1)  # appending the result
    result.append(result_2)
    result.append(result_3)
    result.append(r4)
    result = np.transpose(result)

    # labels
    labels = ['MMSDDF', '3LSAA', 'PRMS', 'FL-BETS', 'Proposed BES_SecDataSharing']  # x-axis labels
    tick_labels = ['Memory', 'Time', 'Search Match','Swoop Match']  # metrics
    bar_width, s = 0.12, 0.0  # bar width, space between bars

    for i in range(len(result)):  # allocating location for bars
        if i is 0:  # initial location - 1st result
            tem = []
            for j in range(len(tick_labels)):
                tem.append(j + 1)
            loc.append(tem)
        else:  # location from 2nd result
            tem = []
            for j in range(len(loc[i - 1])):
                tem.append(loc[i - 1][j] + s + bar_width)
            loc.append(tem)

    # plotting a bar chart
    for i in range(len(result)):
        plt.bar(loc[i], result[i], label=labels[i], tick_label=tick_labels, width=bar_width, )

    plt.legend()  # show a legend on the plot -- here legends are metrics
    plt.show()  # to show the plot


# Create the Window layout
window = sg.Window('BES project', layout)

# event loop
while True:
    event, value = window.read()  # displays the window

    if event == "START":
        ks,bs=int(value[0]) ,int(value[1]) # reads user input
        Mem,Val_Time,No_Va,Cond_Pri = Run.callmain(ks,bs)  # call to main code
        Mem.sort(reverse=True),Val_Time.sort(reverse=True),No_Va.sort(reverse=True),Cond_Pri.sort()


        window.element('11').Update(Mem[0])
        window.element('12').Update(Mem[1])
        window.element('13').Update(Mem[2])
        window.element('14').Update(Mem[3])
        window.element('15').Update(Mem[4])

        window.element('21').Update(Val_Time[0])
        window.element('22').Update(Val_Time[1])
        window.element('23').Update(Val_Time[2])
        window.element('24').Update(Val_Time[3])
        window.element('25').Update(Val_Time[4])

        window.element('31').Update(No_Va[0])
        window.element('32').Update(No_Va[1])
        window.element('33').Update(No_Va[2])
        window.element('34').Update(No_Va[3])
        window.element('35').Update(No_Va[4])

        window.element('41').Update(Cond_Pri[0])
        window.element('42').Update(Cond_Pri[1])
        window.element('43').Update(Cond_Pri[2])
        window.element('44').Update(Cond_Pri[3])
        window.element('45').Update(Cond_Pri[4])

        print("\nDone.!")

    if event == 'Run graph':
        plot_graph(Mem, Val_Time, No_Va,Cond_Pri)

    if event == 'Close':
        window.close()
        break
