# Advanced Graph Visualizations for Clustering Methodology

This repository contains comprehensive implementations of advanced clustering algorithms with sophisticated graph visualizations for methodology research and practical applications.

## 🎯 Overview

This project enhances clustering methodology with visual analysis tools for three major algorithms:
- **K-means Clustering** with convergence analysis and quality metrics
- **Spectral Clustering** with graph structure and eigenvalue analysis  
- **Louvain Method** with network visualization and community detection
- **Comparative Analysis** tools for algorithm selection and evaluation

## 📁 Repository Structure

```
pfe/
├── notebooks/                     # Jupyter notebooks with implementations
│   ├── k_means_advanced.ipynb     # Enhanced K-means with visualizations
│   ├── spectral_clustering.ipynb  # Spectral clustering analysis
│   ├── louvain_method.ipynb      # Network community detection
│   └── comparative_analysis.ipynb # Multi-algorithm comparison
├── src/                          # Python modules (future expansion)
├── examples/                     # Usage examples and demos
├── docs/                         # Documentation
├── requirements.txt              # Python dependencies
├── imagetest.jpg                # Sample test image
└── Untitled0.ipynb             # Original basic implementation

```

## 🚀 Features

### K-means Advanced Visualizations
- **Convergence Analysis**: Track inertia and centroid movement over iterations
- **Cluster Quality Metrics**: Silhouette scores and cluster size distributions
- **2D/3D Scatter Plots**: Pixel clusters in RGB/HSV color space
- **Parameter Optimization**: Elbow method for optimal k selection
- **Interactive Visualizations**: Plotly-based 3D scatter plots with hover details

### Spectral Clustering Graph Visualizations
- **Affinity Matrix Heatmaps**: Show pixel/point similarity relationships
- **Graph Structure Visualization**: K-nearest neighbor connectivity graphs
- **Eigenvalue Analysis**: Plot eigenvalues of Laplacian matrix
- **Cluster Boundary Visualization**: Show non-convex cluster shapes
- **Parameter Sensitivity**: Gamma and neighbor count impact analysis

### Louvain Method Network Visualizations
- **Network Layout Graphs**: Force-directed layouts showing community structure
- **Modularity Evolution**: Track modularity optimization over iterations
- **Community Size Distribution**: Histogram of detected communities
- **Hierarchical Community Structure**: Multi-level community detection
- **Interactive Network Graphs**: Zoom, pan, and hover capabilities

### Comparative Analysis Tools
- **Algorithm Performance Dashboard**: Side-by-side comparison of all methods
- **Evaluation Metrics Visualization**: Comprehensive scoring across metrics
- **Processing Time Analysis**: Performance benchmarking graphs
- **Quality vs Speed Trade-offs**: Algorithm characteristics analysis

## 📋 Requirements

### Core Dependencies
```bash
numpy>=1.21.0
scipy>=1.7.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.5.0
seaborn>=0.11.0
plotly>=5.0.0
networkx>=2.6.0
opencv-python>=4.5.0
python-louvain
```

### Installation
```bash
# Clone the repository
git clone https://github.com/Aamii16/pfe.git
cd pfe

# Install dependencies
pip install -r requirements.txt

# For Google Colab users (additional step)
!pip install python-louvain
```

## 🔧 Usage

### Quick Start
```python
# Import the enhanced clustering modules
from notebooks.k_means_advanced import EnhancedKMeans
from notebooks.spectral_clustering import EnhancedSpectralClustering
from notebooks.louvain_method import EnhancedLouvain

# Load your data
import numpy as np
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.5, random_state=42)

# Enhanced K-means with tracking
kmeans = EnhancedKMeans(n_clusters=4)
kmeans.fit(X)

# Visualize convergence
plot_convergence_analysis(kmeans)
plot_cluster_quality_metrics(X, kmeans.labels_, kmeans.centroids_)
```

### Notebook Usage
1. **Open in Google Colab**: Each notebook is designed for Google Colab compatibility
2. **Run Sequentially**: Execute cells in order for proper initialization
3. **Interactive Exploration**: Use Plotly visualizations for detailed analysis
4. **Parameter Tuning**: Modify parameters to see real-time effects

### Example Workflows

#### Image Clustering
```python
# Load and process image
import cv2
image = cv2.imread('imagetest.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_values = image.reshape(-1, 3).astype(np.float32)

# Find optimal k
optimal_k, _, _ = elbow_method_analysis(pixel_values, range(2, 8))

# Enhanced clustering with visualizations
enhanced_kmeans = EnhancedKMeans(n_clusters=optimal_k)
enhanced_kmeans.fit(pixel_values)

# RGB/HSV color space visualization
create_rgb_hsv_visualization(pixel_values, enhanced_kmeans.labels_, 
                           enhanced_kmeans.centroids_)
```

#### Network Community Detection
```python
# Create network from data
G = create_network_from_data(X, method='knn', k=10)

# Louvain community detection
louvain = EnhancedLouvain(resolution=1.0)
louvain.fit(G)

# Interactive network visualization
create_interactive_network_visualization(G, louvain.best_partition_)
```

## 📊 Visualization Examples

### K-means Convergence Analysis
- Inertia reduction over iterations
- Centroid movement tracking  
- Processing time per iteration
- Convergence rate analysis

### Spectral Clustering Eigenanalysis
- Eigenvalue spectrum plots
- Spectral gap identification
- Eigenvector visualization
- Parameter sensitivity heatmaps

### Louvain Modularity Evolution
- Modularity optimization tracking
- Community hierarchy visualization
- Network layout comparisons
- Interactive graph exploration

### Comparative Dashboards
- Multi-algorithm performance metrics
- Quality vs speed trade-off analysis
- Dataset-specific recommendations
- Statistical significance testing

## 🎓 Educational Content

### Learning Objectives
- Understand clustering algorithm internals through visualization
- Compare algorithm performance across different data types
- Learn parameter tuning through interactive exploration
- Develop intuition for algorithm selection

### Research Applications
- **Computer Vision**: Image segmentation and object recognition
- **Social Network Analysis**: Community detection and influence mapping
- **Bioinformatics**: Gene expression clustering and pathway analysis
- **Market Research**: Customer segmentation and behavior analysis

## 🔬 Technical Specifications

### Performance Optimization
- Efficient implementations for large datasets (up to 500x500 images)
- Memory-optimized algorithms for network analysis (up to 10,000 nodes)
- Parallel processing support where applicable
- Progressive rendering for large visualizations

### Compatibility
- **Python**: 3.8+ (tested on 3.8, 3.9, 3.10, 3.12)
- **Google Colab**: Full compatibility with GPU acceleration
- **Jupyter**: Local and cloud environments
- **Operating Systems**: Windows, macOS, Linux

### File Formats
- **Notebooks**: `.ipynb` for interactive analysis
- **Modules**: `.py` for production code
- **Visualizations**: `.png`, `.pdf` for static plots, `.html` for interactive
- **Data**: Support for common image formats (JPG, PNG, BMP)

## 🤝 Contributing

### Development Setup
```bash
# Fork the repository
git fork https://github.com/Aamii16/pfe.git

# Create feature branch
git checkout -b feature/new-visualization

# Make changes and test
python -m pytest tests/

# Submit pull request
```

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for all functions
- Include unit tests for new features
- Update documentation as needed
- Ensure Google Colab compatibility

## 📚 Documentation

### API Reference
- [K-means Advanced API](docs/kmeans_api.md)
- [Spectral Clustering API](docs/spectral_api.md)
- [Louvain Method API](docs/louvain_api.md)
- [Visualization API](docs/visualization_api.md)

### Tutorials
- [Getting Started Guide](docs/getting_started.md)
- [Parameter Tuning Best Practices](docs/parameter_tuning.md)
- [Performance Optimization](docs/performance_tips.md)
- [Custom Visualization Development](docs/custom_viz.md)

## 🔍 Troubleshooting

### Common Issues
1. **Memory Issues**: Reduce dataset size or use sampling
2. **Slow Performance**: Enable GPU acceleration in Colab
3. **Import Errors**: Ensure all dependencies are installed
4. **Visualization Problems**: Update browser or use different renderer

### Support
- **Issues**: Report bugs via GitHub Issues
- **Questions**: Use GitHub Discussions
- **Feature Requests**: Submit via Issues with enhancement label

## 📈 Future Enhancements

### Planned Features
- [ ] DBSCAN implementation with density visualization
- [ ] Hierarchical clustering with dendrogram analysis
- [ ] GPU-accelerated implementations
- [ ] Real-time clustering for streaming data
- [ ] Web-based interactive dashboard
- [ ] Additional evaluation metrics
- [ ] Automated parameter optimization
- [ ] Integration with MLflow for experiment tracking

### Research Extensions
- [ ] Deep clustering methods
- [ ] Multi-view clustering
- [ ] Ensemble clustering techniques
- [ ] Uncertainty quantification
- [ ] Fairness-aware clustering

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **scikit-learn** community for excellent clustering implementations
- **NetworkX** developers for graph analysis tools
- **Plotly** team for interactive visualization capabilities
- **Google Colab** for providing accessible computational resources

## 📞 Contact

- **Author**: Aamii16
- **Repository**: [https://github.com/Aamii16/pfe](https://github.com/Aamii16/pfe)
- **Issues**: [GitHub Issues](https://github.com/Aamii16/pfe/issues)

---

*This project transforms theoretical clustering methodology into practical, visual frameworks that researchers and practitioners can immediately apply to their problems.*
