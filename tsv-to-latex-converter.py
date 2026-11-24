import csv
import os

def convert_tsv_to_latex(input_file, output_file):
    """
    Converts a TSV file with any number of rows into a LaTeX table.
    Columns 2 and 7 (indices 1 and 6) are preserved exactly (e.g., for \cite commands).
    Other columns have basic LaTeX special characters escaped.
    """
    
    def latex_escape(text):
        """Escapes common LaTeX special characters."""
        chars = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
        }
        return "".join(chars.get(c, c) for c in text)

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        # csv.reader handles multi-line files automatically
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)

    with open(output_file, 'w', encoding='utf-8') as f:
        # Start LaTeX table environment
        f.write(r'\begin{table}[h!]' + '\n')
        f.write(r'\centering' + '\n')
        f.write(r'\begin{tabular}{lllllll}' + '\n')
        f.write(r'\hline' + '\n')
        
        for row in rows:
            if not row or len(row) < 7:
                continue
            
            processed_row = []
            for i, col in enumerate(row):
                # Columns 2 and 7 (indices 1 and 6) remain untouched
                if i == 1 or i == 6:
                    processed_row.append(col.strip())
                else:
                    processed_row.append(latex_escape(col.strip()))
            
            # Join columns with & and end with \\
            f.write(" & ".join(processed_row) + r' \\' + '\n')
            
        f.write(r'\end{tabular}' + '\n')
        f.write(r'\caption{Converted TSV Data}' + '\n')
        f.write(r'\label{tab:tsv_data}' + '\n')
        f.write(r'\end{table}' + '\n')

if __name__ == "__main__":
    # This script will process all rows in 'input.tsv' and save to 'output.tex'
    convert_tsv_to_latex('input.tsv', 'output.tex')
    print("Conversion complete. Check output.tex")
