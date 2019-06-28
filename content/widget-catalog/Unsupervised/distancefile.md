+++
"title" = "Distance File"
"icon" = "icons/distance-file.png"
"keywords" = "[]"
"category" = "Unsupervised"
+++
Distance File
=============

Loads an existing distance file.

**Outputs**

- Distance File: distance matrix

![](/images/unsupervised/DistanceFile-stamped.png)

1. Choose from a list of previously saved distance files.
2. Browse for saved distance files.
3. Reload the selected distance file.
4. Information about the distance file (number of points,
    labelled/unlabelled).
5. Browse documentation datasets.
6. Produce a report.

Example
-------

When you want to use a custom-set distance file that you've saved before, open the **Distance File** widget and select the desired file with the *Browse* icon. This widget loads the existing distance file. In the snapshot below, we loaded the transformed *Iris* distance matrix from the [Save Distance Matrix](/widget-catalog/unsupervised/savedistancematrix) example. We displayed the transformed data matrix in the [Distance Map](/widget-catalog/unsupervised/distancemap) widget. We also decided to display a distance map of the original *Iris* dataset for comparison.

![](/images/unsupervised/DistanceFile-Example.png)
