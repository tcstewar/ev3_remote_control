import subprocess
import threading

class XBox(object):
    def __init__(self, wireless_index=0):
        self.wireless_index = wireless_index
        self.value = dict(X1=0, Y1=0, X2=0, Y2=0, LT=0, RT=0,
                          du=0, dd=0, dl=0, dr=0, 
                          back=0, guide=0, start=0, 
                          A=0, B=0, X=0, Y=0, LB=0, RB=0)

    def start(self):
        threading.Thread(target=self.run, args=()).start()

    def run(self):
        p = subprocess.Popen(['xboxdrv', '-w', '%d' % self.wireless_index], 
                             stdout=subprocess.PIPE)
        while True:
            line = p.stdout.readline().strip().decode('utf-8')
            #print(line)
            if line.startswith('X1'):
                self.parse(line)

    def parse(self, line):
        data = line.replace(':', ': ').split()

        tag = None
        for item in data:
            if item.endswith(':'):
                tag = item[:-1]
            else:
                value = int(item)
                self.value[tag] = value


if __name__ == '__main__':
    import time
    x = XBox()
    x.start()
    while True:
        print(x.value)
        time.sleep(0.01)

