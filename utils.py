import subprocess


def num_lines_in_file(file_path):
    """ Calculate the number of line in a file """
    return int(subprocess.check_output('wc -l %s' % file_path, shell=True).strip().split()[0])
