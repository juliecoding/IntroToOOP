import glob
import numpy
import matplotlib.pyplot as plt

VT = 100
WIDTH = 50

def analyze(filename):
    #read in data from the file (store into ndarray)
    raw = numpy.loadtxt(filename, dtype=int)

    #then smooth the data (store into a new nparray)
    smoothData = smooth(raw)
    #Search for pulses in the smoothed data
    pulses = []
    i = 0
    while i < len(smoothData) - 2:
        if smoothData[i + 2] - smoothData[i] > VT: #found a pulse
            pulses.append(i)

            #skip past the rise
            i += 1
            while i < len(smoothData) - 2 and smoothData[i + 1] > smoothData[i]:
                i += 1
        i +=1
    if not pulses:
        return

    # Calculate the area of the pulses
    outputString = f'{filename}:\n'
    for i in range (len(pulses)):
        startPos = pulses[i]
        realWidth = WIDTH

        if i < len(pulses) - 1 and pulses[i] + realWidth > pulses[i + 1]:
                realWidth = pulses[i + 1] - startPos
        realWidth = min(realWidth, len(smoothData) - startPos)
        area = sum(raw[startPos : startPos + realWidth])
        outputString += f'Pulse {i + 1}: {startPos + 1} ({area})\n'

        with open(filename[:-3] + 'out', 'w') as outfile:
            print(outputString, file=outfile, end='')

    # Plot the data
    _, axes = plt.subplots(nrows=2)
    axes[0].plot(raw, linewidth=.2)
    axes[0].set(title=filename, ylabel="raw")
    axes[1].plot(smoothData, linewidth=.3)
    axes[1].set(ylabel='smooth')
    plt.savefig(filename[:-3] + 'pdf')

def smooth(data):
    res = data.copy()
    for n in range(3, len(data) - 3):
        res[n] = (data[n - 3] + 2 * data[n - 2] + 3 * data[n - 1] + 3 * data[n] + 3 * data[n + 1] + 2 * data[n + 2] + data[n + 3]) // 15
    return res

def main():
    for fname in glob.glob('*.dat'):
        print("ANALYZING FILE", fname)
        print(analyze(fname))

if __name__ == "__main__":
    main()
