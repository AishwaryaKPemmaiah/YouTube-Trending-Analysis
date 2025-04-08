def test_kmeans_clusters_shape():
    from src.clustering import cluster_videos
    df = load_sample_data()
    labels = cluster_videos(df)
    assert len(labels) == len(df)
