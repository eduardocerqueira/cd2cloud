from cd2cloud.core.CDRipper import Worker

rip_workdir = '/tmp'
cd2cloud_cfg = '/home/ecerquei/git/cd2cloud/conf/abcde.conf'

ripper = Worker()
cmd = '/usr/bin/abcde -c %s -N' % cd2cloud_cfg
ripper.worker(cmd=cmd, cwd=rip_workdir)
