import os


def create_file(latex_file_name, metric, folder, collection, constraint_set, caption, table_counter):
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
        f.write(r'\input{' + '../tbls/{:s}/tbl_{:s}_comparison_noisy_constraint_sets_{:g}'.format(folder, metric,
                                                                                 constraint_set) + '}' + '\n')
        f.write(r'\caption{' + caption + '}' + '\n')
        f.write(r'\end{table}' + '\n')

        f.write('\n\n')

        f.write(r'\end{document}' + '\n')


constraint_sets = [5, 10, 15, 20]
table_counter = 119
collection = 'COL1'

# %% ARI

metric_abbreviation = 'ARI'
metric = 'Average Adjusted Rand Index (ARI) values'
algorithms = 'of the PCCC algorithms and the state-of-the-art algorithm (CSC)'
interpretation = 'Higher values indicate more overlap with the ground truth assignment.'
meaning_bold = 'The highest values are stated in bold.'
k_means = 'The column KMEANS reports the average ARI values that were obtained with the unconstrained k-means algorithm.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 1,800 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}-noisy.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'obtained with noisy constraint sets of size {:g}\% NCS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                           algorithms,
                                                           constraint_set_str,
                                                           interpretation,
                                                           meaning_bold,
                                                           k_means,
                                                           meaning_hyphen))

    create_file(latex_file_name, metric='ari', folder='revision_experiment6', collection='col1',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')

# %%

metrics = ['ARI']
table_counter = 120

with open('markdown_table_noisy.txt', 'w') as f:

    # Add header
    header_str = '| Metric' + '|'
    for i in constraint_sets:
        header_str = header_str + str(i) + '% CS' + ' | '
    header_str += '\n'

    f.write(header_str)

    table_str = '|:-----|'
    for i in constraint_sets:
        table_str = table_str + '-----|'
    table_str += '\n'

    f.write(table_str)

    for metric in metrics:
        row_str = '| ' + metric + '|'
        for i in constraint_sets:
            row_str = row_str + ' [Table W{:d}](tables/'.format(table_counter) + metric + '-' + collection + '-' + str(i) + '-noisy.pdf)|'
            table_counter += 1
        row_str += '|\n'

        f.write(row_str)