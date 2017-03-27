# https://www.cyberciti.biz/faq/python-run-external-command-and-get-output/

from subprocess import Popen, PIPE
from multiprocessing import Process

def run_cmd(cmd):
    """Arguments can be passed to cmd separated by blank space"""
    print "Running cmd: %s" % cmd
    proc = Popen(cmd, stdout=PIPE, shell=True, cwd="/tmp")
    (output, err) = proc.communicate()
    p_status = proc.wait()
    if p_status != 0:
        print "\nERROR: %s \n" % err
    print "Command output : ", output

if __name__ == '__main__':
    #cmd = 'abcde -c /home/ecerquei/git/cd2cloud/conf/abcde.conf -N'
    cmd = 'abcde -v'
    cd_ripper = Process(target=run_cmd, args=(cmd,))
    cd_ripper.start()
    cd_ripper.join()
