# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:36:14 2018

@author: QJ
"""
import numpy as np
import scanpy.api as sc
sc.settings.verbosity = 3  # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.settings.set_figure_params(dpi=80)  # low dpi (dots per inch) yields small inline figures
sc.logging.print_version_and_date()
sc.logging.print_versions_dependencies_numerics()
results_file = 'F:/zuoye/wanglab/data/filtered_gene_bc_matrices/hg19/write/pmbc3k.h5ad'
path = 'F:/zuoye/wanglab/data/filtered_gene_bc_matrices/hg19/'
adata = sc.read(path + 'matrix.mtx', cache=False).transpose()         #change True to False
adata.var_names = np.genfromtxt(path + 'genes.tsv', dtype=str)[:, 1]
adata.obs_names = np.genfromtxt(path + 'barcodes.tsv', dtype=str)
adata.var_names_make_unique()
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
mito_genes = [name for name in adata.var_names if name.startswith('MT-')]
# for each cell compute fraction of counts in mito genes vs. all genes
# the ".A1" is only necessary, as X is sparse - it transform to a dense array after summing
adata.obs['percent_mito'] = np.sum(
    adata[:, mito_genes].X, axis=1).A1 / np.sum(adata.X, axis=1).A1
# add the total counts per cell as observations-annotation to adata
adata.obs['n_counts'] = np.sum(adata.X, axis=1).A1
sc.pl.violin(adata, ['n_genes', 'n_counts', 'percent_mito'],
             jitter=0.4, multi_panel=True)
sc.pl.scatter(adata, x='n_counts', y='percent_mito')
sc.pl.scatter(adata, x='n_counts', y='n_genes')
adata = adata[adata.obs['n_genes'] < 2500, :]
adata = adata[adata.obs['percent_mito'] < 0.05, :]
adata_raw = sc.pp.log1p(adata, copy=True)
adata.raw = adata_raw
sc.pp.normalize_per_cell(adata, counts_per_cell_after=1e4)
filter_result = sc.pp.filter_genes_dispersion(
    adata.X, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.filter_genes_dispersion(filter_result)
adata = adata[:, filter_result.gene_subset]
sc.pp.log1p(adata)
sc.pp.regress_out(adata, ['n_counts', 'percent_mito'])
sc.pp.scale(adata, max_value=10)
adata.write(results_file)
sc.tl.pca(adata)
adata.obsm['X_pca'] *= -1  # multiply by -1 to match Seurat R
sc.pl.pca_scatter(adata, color='CST3', right_margin=0.2)
sc.pl.pca_variance_ratio(adata, log=True)
adata = sc.read(results_file)
sc.tl.tsne(adata, n_pcs=10, random_state=2)
adata.write(results_file)
ax = sc.pl.tsne(adata, color=['CST3', 'NKG7'], color_map='RdBu_r')
sc.pl.tsne(adata, color=['CST3', 'NKG7'], color_map='RdBu_r', use_raw=False)
adata = sc.read(results_file)
sc.tl.louvain(adata, n_neighbors=10, resolution=1, recompute_graph=True)
sc.pl.tsne(adata, color='louvain_groups')
adata.write(results_file)
adata = sc.read(results_file)
sc.tl.rank_genes_groups(adata, 'louvain_groups')
sc.pl.rank_genes_groups(adata, n_genes=20, save='.pdf')
adata.write(results_file)
import pandas as pd
pd.DataFrame(adata.uns['rank_genes_groups_gene_names']).loc[:20]
adata = sc.read(results_file)
sc.tl.rank_genes_groups(adata, 'louvain_groups', groups=['0'], reference='1')
sc.pl.rank_genes_groups(adata, groups=['0'], n_genes=20)
sc.pl.rank_genes_groups_violin(adata, groups='0', n_genes=8)
adata = sc.read(results_file)
sc.pl.rank_genes_groups_violin(adata, groups='0', n_genes=8)
sc.pl.violin(adata, 'NKG7', group_by='louvain_groups')
adata = sc.read(results_file)
adata.obs['louvain_groups'].cat.categories = [
    'CD4 T cells', 'CD14+ Monocytes',
    'B cells', 'CD8 T cells', 
    'NK cells', 'FCGR3A+ Monocytes',
    'Dendritic cells', 'Megakaryocytes']
adata.write(results_file)
adata = sc.read(results_file)
sc.pl.tsne(adata, size=10,
           legend_fontsize=12, legend_fontweight='bold',
           color='louvain_groups',
           legend_loc='on data')
adata.write(results_file)
# Export single fields of the annotation of observations
adata.obs[['n_counts', 'louvain_groups']].to_csv(
    './write/pbmc3k_corrected_louvain_groups.csv')
# Export single columns of the multidimensional annotation
adata.obsm.to_df()[['X_pca1', 'X_pca2']].to_csv(
    './write/pbmc3k_corrected_X_pca.csv')
# Or export everything except the data using `.write_csvs`.
adata.write_csvs(results_file[:-5])