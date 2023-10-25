+++
author = "Noah Novšak"
date = "2023-10-24"
draft = false
title = "Dask all Folks"
type = "blog"
thumbImage = "/blog_img/2023/2023-10-24-dask-all-folks.png"
frontPageImage = "/blog_img/2023/2023-10-24-dask-all-folks.png"
blog = ["dask", "development"]
shortExcerpt = "Loading datasets into Orange with Dask"
longExcerpt = "Loading datasets into Orange with Dask"
+++

Today, we will delve into the exciting world of Dask once again, and explore how to finally bring your own data into Orange. Or, more precisely, into an [experimental version of Orange that supports Dask](https://github.com/biolab/orange3/wiki/Orange-with-Dask).

If you've already set up your data as an Orange Table and you would just like to re-encode it to better support dask, then all you have to do is export it again as a `.hdf5` file. This is done either with the *Save Data* widget (choose "Orange on-disk data" as the file type) or in _python_ like so:

```python
table = Table('my_data.tab')
table.save('my_data.hdf5')
```

Simple as that, end of blog, see you next time!

Well, not quite. For everyone that has a bunch of data in some other format, it's not quite as simple. So here's a short guide on preparing your data for Orange.

First of all I'll assume your data can be read in python into something resembling a [numpy](https://numpy.org/) array. If that is not the case, your first step will be to make it so. Next, in addition to the array you will also need to make a _domain_ for your data. That is where we store all the extra information that describes the contents of your data (feature names, types, target variables, etc.).

```python
>>> table = Table('heart_disease')
>>> table.domain.attributes
(ContinuousVariable(name='age', number_of_decimals=0),
 DiscreteVariable(name='gender', values=('female', 'male')),
...
```

Usually in a `.csv` or `.tab` file we would write this information in the header (the first or first three rows). But the [HDF5](https://www.hdfgroup.org/solutions/hdf5) format is somewhat different. It is very flexible and allows information to be stored in many different ways. So we've had to come up with a consistent way to save this information that is as true to the internal structure of our table a possible and simple to implement even outside orange. What we've settled on (depicted in the diagram below) is to make separate arrays to store the raw data, and an extra group to hold the additional information.

```html
├── X (Data)
├── Y (Class Data)
├── metas (Meta Data)
│   ├── 0 (Column 1)
│   ├── 1 (Column 2)
│   └── ... (Additional columns)
└── domain
    ├── attributes/class_vars/metas (Domain)
    └── attributes_args/class_vars_args/metas_args (Optional)
```

Now let's try to apply this idea on an actual dataset! The simplest approach is to use a library like [h5py](https://www.h5py.org/), this way it boils down to just a couple lines of code. First we can save our data arrays, (note that due to data types the _metas_ array is split up and saved by columns).

```python
with h5py.File('my_data.hdf5', 'w') as f:
    f.create_dataset('X', data=x_array)
    f.create_dataset('Y', data=y_array)
    for i in data_metas.shape[1]:
        f.create_dataset(f'metas/{i}', data=metas_array[:, i])
```

The next step is to make and store our domain. We'll have to make separate arrays for each of our attributes, class variables and meta attributes, and save them with the appropriate names. These 'domain' arrays should consist of two columns, indicating the name and type of each feature (each row representing one column of data). 

```python
attributes = np.array(
    [['age', 'c'], # ContinuousVariable(name='age')
     ['gender', 'd'], # DiscreteVariable(name='gender')
     ...],
    dtype='S'
)
class_vars = ...
with h5py.File('my_data.hdf5', 'r+') as f:
    domain = f.create_group('domain')
    domain.create_dataset('attributes', data=attributes)
    domain.creat_dataset('class_vars', data=class_vars)
```

Remember the _heart-disease_ table from the example above? Well you can see that the domain contains a little bit more than just the name and type of variables. Continuous variables can specify how accurate they are and discrete variables can also represent non-numeric data by specifying values. These parameters can be saved in our domain in seperate (optional) arrays. Because this additional information can be quite complex and varied though, we decided the most reasonable way to save them is to use [json](https://www.json.org/json-en.html).

```python
attributes_args = np.array(
    [['{number_of_decimals: 0}'],
     ['{values: ("female", "male")}'],
     ...],
    dtype='S'
)
with h5py.File('my_data.hdf5', 'r+') as f:
    domain = f['domain']
    domain.create_dataset('attributes_args', data=attributes_args)
```

That's it! Now you can create your own `.hdf5` datasets and start processing them in Orange. Remember, you will need the experimental Orange version from the *dask* branch: [see installation instructions](https://github.com/biolab/orange3/wiki/Orange-with-Dask).
