import paramiko
import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_mainWindow

my_hostname = 'ec2-52-25-102-252.us-west-2.compute.amazonaws.com'

my_username = 'client_user'

my_password = 'client_password'


class MainWindow(QMainWindow, ui_mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        f = open('hostDetails', 'r')
        self.hostAddress = f.readline().strip()
        self.userName = f.readline().strip()
        self.userPassword = f.readline().strip()
        f.close()

        self.statusLabel.setText('Connecting to server')
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.hostAddress, username=self.userName, password=self.userPassword)
            self.ssh.exec_command('rm -f testdata/*')
            self.ssh.exec_command('rm -f results/*')
            self.ftp = self.ssh.open_sftp()
        except Exception as e:
            print(e)
            print(e.message)
            self.statusLabel.setText('Connection error, could not connect to server, ' + e.message)
        self.statusLabel.setText('Connected')

        self.downloadButton.clicked.connect(self.download)
        self.connect(self.downloadLineEdit, SIGNAL('returnPressed()'), self.download)
        self.uploadButton.clicked.connect(self.upload)
        self.generateResultsButton.clicked.connect(self.generateResults)
        self.connect(self.uploadLineEdit, SIGNAL('returnPressed()'), self.upload)

    def upload(self):
        self.statusLabel.setText('Uploading')
        QApplication.processEvents()
        QApplication.processEvents()
        QApplication.processEvents()
        local = str(self.uploadLineEdit.text())
        filename = os.path.basename(local)
        remote = "/home/" + self.userName + "/testdata/" + filename
        self.ftp.put(local, remote)
        self.uploadedFileName = filename
        self.statusLabel.setText('Upload Finished')

    def generateResults(self):
        # TODO actually generate results
        # The way we want to do this is have an executable under root user,
        # but give client user permissions to execute it.
        resultsFolder = '/home/' + self.userName + '/results/'
        stdin, stdout, stderr = self.ssh.exec_command('sudo -u root /home/ec2-user/bin/genResults.sh ' + "'" + self.uploadedFileName + "'")
        print(stdout.readlines())
        print(stderr.readlines())
        # resultsList = [os.path.join(resultsFolder, fn) for fn in next(os.walk(resultsFolder))[2]]
        # resultsList.sort()

    def download(self):
        self.statusLabel.setText('Downloading')
        QApplication.processEvents()
        QApplication.processEvents()
        QApplication.processEvents()
        numFiles = int(str(self.numResultsSpinBox.text()))
        remotePath = '/home/' + self.userName + '/' + 'results/'
        fileNames = self.ftp.listdir(remotePath)
        fileNames.sort()
        filePaths = [remotePath + fileName for fileName in fileNames]
        localPath = str(self.downloadLineEdit.text()).strip()
        if localPath[-1] != '/':
            localPath += '/'

        # TODO Get numFiles results from results folder

        for i in range(0,numFiles*2):
            self.ftp.get(filePaths[i], localPath+fileNames[i])
        self.statusLabel.setText('Download Finished')


def upload(source, dest, host, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    ftp = ssh.open_sftp()
    ftp.put(source, dest)


def download(source, dest, host, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    ftp = ssh.open_sftp()
    ftp.get(dest, source)


def main():
    # args = sys.argv
    # if args[1] == 'upload':
    #     upload(args[2], '/home/' + my_username + '/' + args[2], my_hostname, my_username, my_password)
    # elif args[1] == 'download':
    #     download(args[2], '/home/' + my_username + '/' + args[2], my_hostname, my_username, my_password)

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()


main()
