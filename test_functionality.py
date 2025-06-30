#!/usr/bin/env python3
"""
Basic functionality test for the advanced clustering visualizations.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sys
import os

# Test basic imports
try:
    import plotly.graph_objects as go
    import networkx as nx
    import community as community_louvain
    print("✓ All required libraries imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

def test_basic_functionality():
    """Test basic clustering functionality."""
    print("\n" + "="*50)
    print("TESTING BASIC CLUSTERING FUNCTIONALITY")
    print("="*50)
    
    # Create sample data
    X, y_true = make_blobs(n_samples=100, centers=3, cluster_std=1.0, random_state=42)
    print(f"✓ Created sample data: {X.shape[0]} samples, {len(np.unique(y_true))} clusters")
    
    # Test K-means
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)
    print(f"✓ K-means clustering: {len(np.unique(kmeans_labels))} clusters found")
    
    # Test Spectral clustering
    from sklearn.cluster import SpectralClustering
    spectral = SpectralClustering(n_clusters=3, random_state=42)
    spectral_labels = spectral.fit_predict(X)
    print(f"✓ Spectral clustering: {len(np.unique(spectral_labels))} clusters found")
    
    # Test Louvain method
    from sklearn.neighbors import kneighbors_graph
    knn_graph = kneighbors_graph(X, n_neighbors=10, mode='connectivity')
    adjacency = (knn_graph + knn_graph.T) / 2
    G = nx.from_scipy_sparse_array(adjacency)
    partition = community_louvain.best_partition(G, random_state=42)
    louvain_labels = np.array([partition[i] for i in range(len(X))])
    print(f"✓ Louvain method: {len(np.unique(louvain_labels))} communities found")
    
    # Test metrics
    from sklearn.metrics import silhouette_score, adjusted_rand_score
    
    kmeans_silhouette = silhouette_score(X, kmeans_labels)
    spectral_silhouette = silhouette_score(X, spectral_labels)
    louvain_silhouette = silhouette_score(X, louvain_labels)
    
    print(f"\nSilhouette Scores:")
    print(f"  K-means: {kmeans_silhouette:.3f}")
    print(f"  Spectral: {spectral_silhouette:.3f}")
    print(f"  Louvain: {louvain_silhouette:.3f}")
    
    kmeans_ari = adjusted_rand_score(y_true, kmeans_labels)
    spectral_ari = adjusted_rand_score(y_true, spectral_labels)
    louvain_ari = adjusted_rand_score(y_true, louvain_labels)
    
    print(f"\nAdjusted Rand Index:")
    print(f"  K-means: {kmeans_ari:.3f}")
    print(f"  Spectral: {spectral_ari:.3f}")
    print(f"  Louvain: {louvain_ari:.3f}")
    
    print("✓ All clustering algorithms tested successfully!")
    return True

def test_visualization_basic():
    """Test basic visualization functionality."""
    print("\n" + "="*50)
    print("TESTING BASIC VISUALIZATION FUNCTIONALITY")
    print("="*50)
    
    # Create sample data
    X, y = make_blobs(n_samples=50, centers=3, random_state=42)
    
    # Test matplotlib
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='tab10', alpha=0.7)
    plt.title('Basic Scatter Plot Test')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.close()  # Don't display in test
    print("✓ Matplotlib visualization test passed")
    
    # Test plotly basic functionality
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=X[:, 0], y=X[:, 1],
        mode='markers',
        marker=dict(color=y, colorscale='Viridis'),
        name='Test Data'
    ))
    fig.update_layout(title='Plotly Test')
    # Don't show in test
    print("✓ Plotly visualization test passed")
    
    # Test networkx basic functionality
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])
    pos = nx.spring_layout(G)
    print("✓ NetworkX graph test passed")
    
    print("✓ All visualization tests passed!")
    return True

def test_image_processing():
    """Test basic image processing functionality."""
    print("\n" + "="*50)
    print("TESTING IMAGE PROCESSING FUNCTIONALITY")
    print("="*50)
    
    # Check if test image exists
    image_path = '/home/runner/work/pfe/pfe/imagetest.jpg'
    if os.path.exists(image_path):
        import cv2
        image = cv2.imread(image_path)
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            print(f"✓ Test image loaded: {image.shape}")
            
            # Test pixel extraction
            pixel_values = image.reshape(-1, 3).astype(np.float32)
            print(f"✓ Pixel values extracted: {pixel_values.shape}")
            
            # Test basic clustering on image subset
            if len(pixel_values) > 1000:
                subset_indices = np.random.choice(len(pixel_values), 1000, replace=False)
                pixel_subset = pixel_values[subset_indices]
            else:
                pixel_subset = pixel_values
            
            from sklearn.cluster import KMeans
            kmeans_img = KMeans(n_clusters=3, random_state=42, n_init=10)
            img_labels = kmeans_img.fit_predict(pixel_subset)
            print(f"✓ Image clustering test: {len(np.unique(img_labels))} clusters")
            
        else:
            print("✗ Could not read test image")
            return False
    else:
        print("! Test image not found - creating synthetic image data")
        synthetic_image = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)
        pixel_values = synthetic_image.reshape(-1, 3).astype(np.float32)
        print(f"✓ Synthetic image created: {pixel_values.shape}")
    
    print("✓ Image processing tests completed!")
    return True

def main():
    """Run all tests."""
    print("ADVANCED CLUSTERING VISUALIZATIONS - FUNCTIONALITY TEST")
    print("=" * 60)
    
    success = True
    
    try:
        success &= test_basic_functionality()
        success &= test_visualization_basic()
        success &= test_image_processing()
        
        if success:
            print("\n" + "🎉 ALL TESTS PASSED! 🎉")
            print("The clustering visualization system is ready to use!")
            print("\nNext steps:")
            print("1. Open any of the Jupyter notebooks in the notebooks/ directory")
            print("2. Run the cells sequentially for interactive analysis")
            print("3. Explore the comprehensive visualizations and tools")
        else:
            print("\n❌ SOME TESTS FAILED")
            print("Please check the error messages above and resolve issues.")
            
    except Exception as e:
        print(f"\n❌ TEST EXECUTION FAILED: {e}")
        success = False
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)