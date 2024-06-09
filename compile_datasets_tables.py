import os


def create_file(latex_file_name, caption, table_counter, fontsize=r'\normalsize',
                tabcolsep=None):

    with open('latex_files/' + latex_file_name, 'w') as f:
        f.write(r'% !TeX spellcheck = en_US' + '\n')
        f.write(r'\documentclass[twoside,11pt]{article}' + '\n')
        f.write(r'\usepackage{tabularx}' + '\n')
        f.write(r'\usepackage{booktabs}' + '\n')
        f.write(r'\usepackage[margin=50pt]{geometry}' + '\n\n')

        f.write('\makeatletter' + '\n')
        f.write('\setlength\@fptop{0\p@}' + '\n')
        f.write('\makeatother' + '\n\n')

        f.write(r'\begin{document}' + '\n')
        f.write(r'\renewcommand*\thetable{W\arabic{table}}' + '\n')

        f.write(r'\setcounter{table}{' + str(table_counter) + '}' + '\n')

        f.write(r'\begin{table}' + '\n')
        f.write(fontsize + '\n')
        if tabcolsep:
            f.write(r'\setlength{\tabcolsep}{' + str(tabcolsep) + '}' + '\n')
        f.write(fontsize + '\n')
        f.write(r'\input{' + '../tbls/tbl_{:s}_constraint_sets.tex'.format(collection) + '}' + '\n')
        f.write(r'\caption{' + caption + '}' + '\n')
        f.write(r'\end{table}' + '\n')

        f.write('\n\n')

        f.write(r'\end{document}' + '\n')


# %% Data set tables

table_counter = 0

for collection in ['COL1', 'COL2', 'COL3', 'COL4']:

    caption = ('Number of must-link (ML) and cannot-link (CL) constraints in the different '
               'constraint sets of collection {:s}.').format(collection)

    latex_file_name = 'Constraints-{:s}.tex'.format(collection)

    if collection == 'COL2':
        create_file(latex_file_name, caption, table_counter, fontsize=r'\tiny', tabcolsep='3pt')
    else:
        create_file(latex_file_name, caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')
