import os


def create_file(latex_file_name, metric, folder, collection, constraint_set, caption, table_counter,
                fontsize=r'\tiny', tabcolsep='3pt'):
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
        f.write(r'\input{' + '../tbls/{:s}/tbl_{:s}_comparison_{:s}_{:g}'.format(folder, metric, collection,
                                                                                 constraint_set) + '}' + '\n')
        f.write(r'\caption{' + caption + '}' + '\n')
        f.write(r'\end{table}' + '\n')

        f.write('\n\n')

        f.write(r'\end{document}' + '\n')

constraint_sets = [0, 0.5, 1, 5]
table_counter = 99
collection = 'COL4'


# %% ARI

metric_abbreviation = 'ARI'
metric = 'Average Adjusted Rand Index (ARI) values'
algorithms = 'of the versions of the PCCC algorithm and the four state-of-the-art algorithms (COPKM, CSC, DILS, LCC)'
interpretation = 'Higher values indicate more overlap with the ground truth assignment.'
meaning_bold = 'The highest values are stated in bold.'
k_means = 'The column KMEANS reports the average ARI values that were obtained with the unconstrained k-means algorithm.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 1,800 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'obtained with constraint sets of size {:g}\% CS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                           algorithms,
                                                           constraint_set_str,
                                                           interpretation,
                                                           meaning_bold,
                                                           k_means,
                                                           meaning_hyphen))

    create_file(latex_file_name, metric='ari', folder='revision_experiment5', collection='col4',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')

# %% Inertia

metric_abbreviation = 'Inertia'
metric = 'Minimum Inertia values'
algorithms = 'of the versions of the PCCC algorithm and the four state-of-the-art algorithms (COPKM, CSC, DILS, LCC)'
interpretation = 'Lower values indicate more coherent clusters.'
meaning_bold = 'The lowest values are stated in bold.'
k_means = 'The column KMEANS reports the minimum inertia value obtained with the k-means algorithm.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 3,600 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'for the constraint sets of size {:g}\% CS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                           algorithms,
                                                           constraint_set_str,
                                                           interpretation,
                                                           meaning_bold,
                                                           k_means,
                                                           meaning_hyphen))

    create_file(latex_file_name, metric='inertia', folder='revision_experiment5', collection='col4',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')

# %% Silhouette

metric_abbreviation = 'Silhouette'
metric = 'Average Silhouette coefficients'
algorithms = 'of the versions of the PCCC algorithm and the four state-of-the-art algorithms (COPKM, CSC, DILS, LCC)'
interpretation = 'Higher values indicate better separated clusters.'
meaning_bold = 'The highest values are stated in bold.'
k_means = 'The column KMEANS reports the average Silhouette coefficients that were obtained with the unconstrained k-means algorithm.'
ground_truth = 'The column GT reports the Silhouette coefficients of the ground truth assignment.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 1,800 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'obtained with constraint sets of size {:g}\% CS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                                algorithms,
                                                                constraint_set_str,
                                                                interpretation,
                                                                meaning_bold,
                                                                k_means,
                                                                ground_truth,
                                                                meaning_hyphen))

    create_file(latex_file_name, metric='silhouette', folder='revision_experiment5', collection='col4',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')

# %% Violations

metric_abbreviation = 'Violations'
metric = 'Average number of cannot-link constraint violations'
algorithms = 'of the versions of the PCCC algorithm and the four state-of-the-art algorithms (COPKM, CSC, DILS, LCC)'
meaning_bold = 'The lowest values are stated in bold.'
k_means = 'The column KMEANS reports the average number of cannot-link constraint violations obtained with the k-means algorithm.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 1,800 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'for the constraint sets of size {:g}\% CS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                           algorithms,
                                                           constraint_set_str,
                                                           meaning_bold,
                                                           k_means,
                                                           meaning_hyphen))

    create_file(latex_file_name, metric='n_cl_violations', folder='revision_experiment5', collection='col4',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')

# %% CPU

metric_abbreviation = 'CPU'
metric = 'Average running times (in seconds)'
algorithms = 'of the versions of the PCCC algorithm and the four state-of-the-art algorithms (COPKM, CSC, DILS, LCC)'
interpretation = 'Higher values indicate better separated clusters.'
meaning_bold = 'The lowest values are stated in bold.'
k_means = 'The column KMEANS reports the average running time of the unconstrained k-means algorithm.'
meaning_hyphen = 'The hyphen indicates that the respective algorithm returned no solution within the time limit of 1,800 seconds.'

for constraint_set in constraint_sets:
    latex_file_name = '{:s}-{:s}-{:g}.tex'.format(metric_abbreviation, collection, constraint_set)
    constraint_set_str = 'for the constraint sets of size {:g}\% CS.'.format(constraint_set)
    caption = ('{:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format(metric,
                                                           algorithms,
                                                           constraint_set_str,
                                                           interpretation,
                                                           meaning_bold,
                                                           k_means,
                                                           meaning_hyphen))

    create_file(latex_file_name, metric='cpu', folder='revision_experiment5', collection='col4',
                constraint_set=constraint_set, caption=caption, table_counter=table_counter)

    table_counter += 1

    # Compile latex file W1-W4.tex
    os.system('pdflatex latex_files/' + latex_file_name + ' -output-directory=tables')

    # Delete auxiliary files
    os.system('rm tables/*.aux')
    os.system('rm tables/*.log')


# %%

# Open file
table_counter = 100
collection = 'COL4'
metrics = ['ARI', 'Inertia', 'Silhouette', 'Violations', 'CPU']

with open('markdown_table_col4.txt', 'w') as f:

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
            row_str = row_str + ' [Table W{:d}](tables/'.format(table_counter) + metric + '-' + collection + '-' + str(i) + '.pdf)|'
            table_counter += 1
        row_str += '|\n'

        f.write(row_str)