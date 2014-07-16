import subprocess

list_path = subprocess.check_output(['find', '/Volumes/workspace/source/gitlab/8-0', '-name', '*vi.po'], shell=False)

sum_path = []
print '-' * 100
list_all = list_path.split('\n')

trans_path = '/Volumes/workspace/source/gitlab/8-0/translate/'

for path in list_all:
    try:
        print '----> path --> %s' % path
        path_ls = path.split('/')[6]
        print 'open --> %s' % path
        ifile = open(path, 'rb')

        path_out = trans_path + path_ls + '.po'

        print 'outfile --> %s' % path_out
        ofile = open(path_out, 'wb')
        ofile.write(ifile.read())
        ofile.close()
        ifile.close()
        #
        print 'finish --> %s' % trans_path
    except Exception, e:
        print path
        print e
        continue





