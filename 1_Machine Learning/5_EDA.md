# ==4. Exploratory Data Analysis (EDA)==


<details><summary><b>Tips & Tricks<b></summary>
<p>

<details><summary><b>Greatter Matrix by mean<b> for <b>Feature Engineering<b></summary>
<p>
~~~python
df['height'].plot.hist(bins=200,
				 range=(50, 80),
				 alpha=.3,
				 color='red',
				 cumulative=True,
				 normed=True)
~~~
</p>
</details>

<details><summary><b>Greatter Matrix by mean<b> for <b>Feature Engineering<b></summary>
<p>
[<b>Notebook<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/0_My%20work/5_SpringLeaf%20Competition/EDA_Springleaf_screencast.html#Go-through) 
~~~python
def autolabel(arrayA):
    '''
    label each colored square with the corresponding data value.
    If value > 20, the text is in black, else in white.
    '''
    arrayA = np.array(arrayA)
    for i in range(arrayA.shape[0]):
        for j in range(arrayA.shape[1]):
            plt.text(j, i, "%.2f"%arrayA[i, j], ha='center', va='bottom', color='w')


def gt_matrix(df,feats,sz=16):
    a = []
    for i,c1 in enumerate(feats):
        b = [] 
        for j,c2 in enumerate(feats):
            mask = (~df[c1].isnull()) & (~df[c2].isnull())
            if i>=j:
                b.append((df.loc[mask,c1].values>=df.loc[mask,c2].values).mean())
            else:
                b.append((df.loc[mask,c1].values>df.loc[mask,c2].values).mean())

        a.append(b)

    plt.figure(figsize = (sz,sz))
    plt.imshow(a, interpolation = 'None', cmap='Spectral')
    _ = plt.xticks(range(len(feats)),feats,rotation = 90)
    _ = plt.yticks(range(len(feats)),feats,rotation = 0)
    autolabel(a)
~~~
</p>
</details>

<details><summary> <b>Better Correlation heatmap<b></summary>
<p>
~~~python

def heatmap(x, y, <b>kwargs):
    if 'color' in kwargs:
        color = kwargs['color']
    else:
        color = [1]*len(x)

    if 'palette' in kwargs:
        palette = kwargs['palette']
        n_colors = len(palette)
    else:
        n_colors = 256 # Use 256 colors for the diverging color palette
        palette = sns.color_palette("Blues", n_colors) 

    if 'color_range' in kwargs:
        color_min, color_max = kwargs['color_range']
    else:
        color_min, color_max = min(color), max(color) # Range of values that will be mapped to the palette, i.e. min and max possible correlation

    def value_to_color(val):
        if color_min == color_max:
            return palette[-1]
        else:
            val_position = float((val - color_min)) / (color_max - color_min) # position of value in the input range, relative to the length of the input range
            val_position = min(max(val_position, 0), 1) # bound the position betwen 0 and 1
            ind = int(val_position * (n_colors - 1)) # target index in the color palette
            return palette[ind]

    if 'size' in kwargs:
        size = kwargs['size']
    else:
        size = [1]*len(x)

    if 'size_range' in kwargs:
        size_min, size_max = kwargs['size_range'][0], kwargs['size_range'][1]
    else:
        size_min, size_max = min(size), max(size)

    size_scale = kwargs.get('size_scale', 500)

    def value_to_size(val):
        if size_min == size_max:
            return 1 * size_scale
        else:
            val_position = (val - size_min) * 0.99 / (size_max - size_min) + 0.01 # position of value in the input range, relative to the length of the input range
            val_position = min(max(val_position, 0), 1) # bound the position betwen 0 and 1
            return val_position * size_scale
    if 'x_order' in kwargs: 
        x_names = [t for t in kwargs['x_order']]
    else:
        x_names = [t for t in sorted(set([v for v in x]))]
    x_to_num = {p[1]:p[0] for p in enumerate(x_names)}

    if 'y_order' in kwargs: 
        y_names = [t for t in kwargs['y_order']]
    else:
        y_names = [t for t in sorted(set([v for v in y]))]
    y_to_num = {p[1]:p[0] for p in enumerate(y_names)}

    plot_grid = plt.GridSpec(1, 15, hspace=0.2, wspace=0.1) # Setup a 1x10 grid
    ax = plt.subplot(plot_grid[:,:-1]) # Use the left 14/15ths of the grid for the main plot

    marker = kwargs.get('marker', 's')

    kwargs_pass_on = {k:v for k,v in kwargs.items() if k not in [
         'color', 'palette', 'color_range', 'size', 'size_range', 'size_scale', 'marker', 'x_order', 'y_order'
    ]}

    ax.scatter(
        x=[x_to_num[v] for v in x],
        y=[y_to_num[v] for v in y],
        marker=marker,
        s=[value_to_size(v) for v in size], 
        c=[value_to_color(v) for v in color],
        <b>kwargs_pass_on
    )
    ax.set_xticks([v for k,v in x_to_num.items()])
    ax.set_xticklabels([k for k in x_to_num], rotation=45, horizontalalignment='right')
    ax.set_yticks([v for k,v in y_to_num.items()])
    ax.set_yticklabels([k for k in y_to_num])

    ax.grid(False, 'major')
    ax.grid(True, 'minor')
    ax.set_xticks([t + 0.5 for t in ax.get_xticks()], minor=True)
    ax.set_yticks([t + 0.5 for t in ax.get_yticks()], minor=True)

    ax.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5])
    ax.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])
    ax.set_facecolor('#F1F1F1')

    # Add color legend on the right side of the plot
    if color_min < color_max:
        ax = plt.subplot(plot_grid[:,-1]) # Use the rightmost column of the plot

        col_x = [0]*len(palette) # Fixed x coordinate for the bars
        bar_y=np.linspace(color_min, color_max, n_colors) # y coordinates for each of the n_colors bars

        bar_height = bar_y[1] - bar_y[0]
        ax.barh(
            y=bar_y,
            width=[5]*len(palette), # Make bars 5 units wide
            left=col_x, # Make bars start at 0
            height=bar_height,
            color=palette,
            linewidth=0
        )
        ax.set_xlim(1, 2) # Bars are going from 0 to 5, so lets crop the plot somewhere in the middle
        ax.grid(False) # Hide grid
        ax.set_facecolor('white') # Make background white
        ax.set_xticks([]) # Remove horizontal ticks
        ax.set_yticks(np.linspace(min(bar_y), max(bar_y), 3)) # Show vertical ticks for min, middle and max
        ax.yaxis.tick_right() # Show vertical ticks on the right 


def corrplot(data, size_scale=500, marker='s'):
    corr = pd.melt(data.reset_index(), id_vars='index')
    corr.columns = ['x', 'y', 'value']
    heatmap(
        corr['x'], corr['y'],
        color=corr['value'], color_range=[-1, 1],
        palette=sns.diverging_palette(20, 220, n=256),
        size=corr['value'].abs(), size_range=[0,1],
        marker=marker,
        x_order=data.columns,
        y_order=data.columns[::-1],
        size_scale=size_scale
    )


~~~
</p>
</details>
<details><summary> <b>Distrubtion of feature vs. row index<b></summary>
<p>
[<b>Example<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#Distribution-of-X8-along-with-row-index:) 

<h4> 1. Without Class labeling
~~~python
plt.figure(figsize=(16, 10))
plt.plot(train.x8, '.')
plt.xlabel('Row Index')
plt.ylabel('X8 Values')
plt.title('Distribution of X8 around row index')
~~~

<h4> 2. With class labeling
[<b>Labeling example<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#Hue-with-Class-labels:)
~~~python
plt.figure(figsize=(16, 10))
plt.scatter(range(len(train.x8)), train.sort_values('y')['x8'], c=train.sort_values('y')['y'], cmap='viridis')
~~~
</p>
</details>

<details><summary> <b>Features Grouping<b> for <b>Feature Engineering<b></summary>
<p>
<h4> 1. Clustering by KMeans
[<b>Notebook<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#With-Clustering:)
~~~python
from sklearn.cluster import KMeans

X = train.copy()

y = X['y']
X = X.drop('y', axis=1)

X = X.fillna(-999)

for col in train.columns[train.dtypes == 'object']:
    X[col] = X[col].factorize()[0]


kmeans = KMeans(n_clusters=7)
y_pred = kmeans.fit_predict(X)
~~~

~~~python
plt.figure(figsize=(16, 10))
sns.heatmap(X.corr(), cmap='viridis');
~~~

<h4> 2. Clustering by Statistics
[<b>Notebook<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#Clustering-Using-Statistics:)

~~~python
plt.figure(figsize=(16, 8))
train.mean().sort_values().plot(style='.');
~~~
</p>
</details>


<details><summary>From <b>Power Law Dist<b> to <b>Normal Disb.<b></summary>
<p>

<h4> Convert
~~~python
#converting the values to log-values to chec for log-normal
import math
frame_with_durations_modified['log_times']=[math.log(i+1) for i in frame_with_durations_modified['trip_times'].values]
~~~

<h4> Show the distribution
~~~python
#pdf of log-values
sns.FacetGrid(frame_with_durations_modified,size=6) \
      .map(sns.kdeplot,"log_times") \
      .add_legend();
plt.show();
~~~

<h4> Check the Q-Q plot.
~~~python
import scipy
#Q-Q plot for checking if trip-times is log-normal
scipy.stats.probplot(frame_with_durations_modified['log_times'].values, plot=plt)
plt.show()
~~~
</p>
</details>

<details><summary>Plot <b>Two Categorical Features<b> with sizes</summary>
<p>
~~~python
def plot_categoricals(x, y, data, annotate=True):
    '''
    Plot counts of 2 categorical.
    Size is raw count for each grouping.
    Percentages are for a given value of y.
    '''
    
    # Raw counts.
    raw_counts = pd.DataFrame(data.groupby(y)[x].value_counts(normalize=False))
    raw_counts = raw_counts.rename(columns={x: 'raw_count'})
    
    # Calculate counts for each group of x and y.
    counts = pd.DataFrame(data.groupby(y)[x].value_counts(normalize=True))
    
    # Rename the column and reset the index.
    counts = counts.rename(columns={x: 'normalized_count'}).reset_index()
    counts['percent'] = 100 * counts['normalized_count']
    
    # Add the raw count
    counts['raw_count'] = list(raw_counts['raw_count'])
    
    plt.figure(figsize=(14, 10))
    # Scatter plot sized by percent.
    plt.scatter(counts[x], counts[y], edgecolor='k', color='lightgreen',
                s=100*np.sqrt(counts.raw_count), marker='o',
                alpha=.6, linewidth=1.5)
    
    # Annotate:
    if annotate:
        # Annotate the plot with text.
        for i, row in counts.iterrows():
            # Put text with appropriate offsets
            plt.annotate(xy=(row[x] - (1/counts[x].nunique()),
                             row[y] - (.15/counts[y].nunique())),
                         color='navy', s=f"{round(row['percent'], 1)}%")
    # Set tick marks
    plt.yticks(counts[y].unique())
    plt.xticks(counts[x].unique())
    
    # Transform min and max to evenly space in square root domain.
    sqr_min = int(np.sqrt(raw_counts.raw_count.min()))
    sqr_max = int(np.sqrt(raw_counts.raw_count.max()))
    
    # 5 sizes for legend
    msizes = list(range(sqr_min, sqr_max,
                        int((sqr_max - sqr_min)/5)))
    markers = []
    
    # Markers for legend
    for size in msizes:
        markers.append(plt.scatter([], [], s=100*size,
                                   label=f'{int(round(np.square(size)/100)*100)}',
                                   color='lightgreen',
                                   alpha=.6, edgecolor='k', linewidth=1.5))
    
    # Legend and formatting
    plt.legend(handles=markers, title='Counts',
               labelspacing=3, handletextpad=2,
               fontsize=16, loc=(1.10, .19))
    plt.annotate(f'* Size represents raw count while % for a given y value.',
                 xy=(0,1), xycoords='figure points', size=10)
    
    # Adjust axes limits.
    plt.xlim((counts[x].min() - (6 / counts[x].nunique()),
              counts[x].max() + (6 / counts[x].nunique())))
    plt.ylim((counts[y].min() - (4 / counts[y].nunique()), 
              counts[y].max() + (4 / counts[y].nunique())))
    plt.grid(None)
    plt.xlabel(f"{x}"); plt.ylabel(f"{y}"); plt.title(f"{y} vs {x}");
~~~

<h4> 2. Example.
~~~python
plot_categoricals('rez_esc', 'Target', data)
~~~
</p>
</details>


<details><summary>Plot <b>How many Unique Values<b> In each column</summary>
<p>
~~~python
color = sns.color_palette()[0]
ax = train.select_dtypes(np.int64)\
     .nunique()\
     .value_counts()\
     .sort_index()\
     .plot.bar(color=color, figsize=(8, 6), edgecolor='black', linewidth=2)
show_annotation(ax)
~~~
</p>
</details>

<details><summary>Plot <b>Quantiles<b> on line chart</summary>
<p>
~~~python
plt.plot(tag_counts[:100], c='b')
plt.scatter(x=list(range(0, 100, 5)), y=tag_counts[0:100:5], c='orange', label='Quantiles with .05 intervals.')
plt.scatter(x=list(range(0,100,25)), y=tag_counts[0:100:25], c='m', label='Quantiles with .25 intevals.')

for x, y in zip(list(range(0, 100, 25)), tag_counts[0:100:25]):
    plt.annotate(s="{}, {})".format(x, y), xy=(x, y), xytext=(x-.05, y+500))
~~~
</p>
</details>

<details><summary><b>Histogram<b> For all Numerical Values</summary>
<p>
~~~python
train_df.hist(bins='auto', figsize=(18, 22), layout=(5, 2));
~~~
</p>
</details>

<details><summary> Add <b>Spaces<b> b/w <b>height<b> and <b>width<b> for subplots</summary>
<p>
~~~python
plt.subplots_adjust(wspace=.5, hspace=.5)
~~~
</p>
</details>

<details><summary> Plot <b>3D<b> figures </summary>
<p style="margin: 0">
~~~python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_3d(x, y, z, df, cmap = plt.cm.seismic_r):
    """3D scatterplot of data in df"""

    fig = plt.figure(figsize = (10, 10))
    
    ax = fig.add_subplot(111, projection='3d')
    
    # 3d scatterplot
    ax.scatter(df[x], df[y],
               df[z], c = df[z], 
               cmap = cmap, s = 40)

    # Plot labeling
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)

    plt.title('{} as function of {} and {}'.format(
               z, x, y), size = 18);
    
plot_3d('learning_rate', 'n_estimators', 'score', opt_hyp)
~~~
</p>
</details>


<details><summary> Show <b>Annotations<b> on <b>bar chart<b> </summary>
<p style="margin: 0">
<h4> Better Version
~~~python
def show_annotation(dist, n=5, total=None):
    sizes = [] # Get highest value in y
    for p in dist.patches:
        height = p.get_height()
        sizes.append(height)

        dist.text(p.get_x()+p.get_width()/2.,          # At the center of each bar. (x-axis)
               height+n,                            # Set the (y-axis)
               '{:1.2f}%'.format(height*100/total) if total else '{}'.format(height), # Set the text to be written
               ha='center', fontsize=14) 
    dist.set_ylim(0, max(sizes) * 1.15); # set y limit based on highest heights
~~~
<h4> Example:
~~~python
total = len(train)
plt.figure(figsize=(12, 6))

color = sns.color_palette()[0]
g = sns.countplot(x='target', data=train, color=color)
g.set_title('Target Distribution', fontsize=20)
g.set_xlabel('Target Values', fontsize=15)
g.set_ylabel('Count', fontsize=15)

show_annotation(g)
~~~

<h4> Another Version
~~~python
# <b><b><b><b><b><b><b><b>SHOW ANNOTATIONS<b><b><b><b><b>
def show_annotation(df, colName, n=10):
    # Add Anootations
    n_points = df.shape[0]
    col_count = df[colName].value_counts()
    locs, labels = plt.xticks() # Get the current tick locations and labels
    # Loop for through each pair of locations and labels.
    for loc, label in zip(locs, labels):
        label_text = label.get_text()
        label_text = int(label_text) if label_text.isdigit() else label_text
        count = col_count[label_text]
        text  = '{:.2f}%'.format(100*count/n_points)
        plt.text(loc, count-n, text, ha='center', color='darkblue', size=14) 
~~~
</p>
</details>

<details><summary> <b>Increase Size of (plt.title)<b> </summary>
<p>

~~~python
plt.title('Title here', size=20, y=1.06)
~~~
~~~python
plt.suptitle('Title here', fontsize=20)
~~~

<h4> OOP Version
~~~python
color = sns.color_palette()[0]
g = sns.countplot(x='target', data=train, color=color)
g.set_title('Target Distribution', fontsize=20)
g.set_xlabel('Target Values', fontsize=15)
g.set_ylabel('Count', fontsize=15)
~~~
</p>
</details>

<details><summary> <b>Change Font Size of all plots<b> </summary>
<p>

~~~python
plt.rcParams['font.size'] = 22
~~~
</p>
</details>



<details><summary> <b>Color the edge of bar chart<b> </summary>
<p>
~~~python
(app_train['DAYS_BIRTH']/-365).plot.hist(edgecolor='k', bins=30);
~~~
~~~python
plt.rcParams['font.size'] = 18
plt.rcParams['patch.edgecolor'] = 'k'
~~~
</p>
</details>

<details><summary> Make <b>grid behind bar charts<b> </summary>
<p>

~~~python
ax.grid(zorder=0)
ax.bar(range(len(y)), y, width=0.3, align='center', color='skyblue', zorder=3)
~~~
</p>
</details>

<details><summary><b>KDE<b> plot b/w <b>feature<b> and <b>TARGET<b></summary>
<p>
~~~python
# Modify it to be sutable for your needs.
def kde_target(var_name, df):
    
    # Calculate the correlation coefficient between the new variable and the target
    corr = df['TARGET'].corr(df[var_name])
    
    avg_repaid     = df.ix[df['TARGET']==0, var_name].median()
    avg_not_repaid = df.ix[df['TARGET']==1, var_name].median()
    
    plt.figure(figsize=(12, 6))
    
    sns.kdeplot(df.ix[df['TARGET']==0, var_name], label='target == 0', shade=True)
    sns.kdeplot(df[df['TARGET']==1][var_name], label='target == 1', shade=True)
    
    # LABEL THE PLOT
    plt.xlabel(var_name)
    plt.ylabel('Density')
    plt.title('%s Distribution' % var_name)
    plt.legend();
    
    print('~> The correlation between %s and the TARGET is %.4f' % (var_name, corr))
    print('~> The median value for loan that was not repaid = %.4f' % avg_not_repaid)
    print('~> The median value for loan that was repaid = %.4f' % avg_repaid)
~~~
</p>
</details>

<details><summary>Show the <b>Legend<b> outside of the plot</summary>
<p>
~~~python
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
~~~
</p>
</details>

</p>
</details>
<b>*

<details><summary><b>Pandas<b></summary>
<p>
- <b>df.plot.hist()<b>     histogram
- <b>df.plot.bar()<b>      bar chart
- <b>df.plot.barh()<b>     horizontal bar chart
- <b>df.plot.line()<b>     line chart
- <b>df.plot.area()<b>     area chart
- <b>df.plot.scatter()<b>  scatter plot
- <b>df.plot.box()<b>      box plot
- <b>df.plot.kde()<b>      kde plot
- <b>df.plot.hexbin()<b>   hexagonal bin plot
- <b>df.plot.pie()<b>      pie chart

[<b>Built-in Visualization<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/03-Pandas-Visualization/00-Pandas%20Built-in%20Data%20Visualization.html#Plot-Types) 
</p>
</details>

<details><summary><b>Matplotlib<b></summary>
<p>

- [<b>1. Matplotlib Concepts<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/3_Matplotlib%20/1_Matplotlib%20Concepts%20Lecture.html#Matplotlib-Overview-Lecture)
- [<b>2. Advanced Concepts<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/3_Matplotlib%20/2_Advanced%20Matplotlib%20Concepts.html#Advanced-Matplotlib-Concepts-Lecture)

</p>
</details>

<details><summary><b>Seaborn<b></summary>
<p>

- [<b>1. Distrubtion Plots<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/1_Distribution%20Plots.html#Distribution-Plots)
- [<b>2. Categorical Data Plots<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/2_Categorical%20Plots.html#Categorical-Data-Plots)
- [<b>3. Matrix Plots<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/3_Matrix%20Plots.html#Matrix-Plots)
- [<b>4. Regression Plots<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/4_Regression%20Plots.html#Regression-Plots) 
- [<b>5. Grids<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/5_Grids.html#Grids) 
- [<b>6. Styles & Coloring<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/6_Style%20and%20Color.html#Style-and-Color)

</p>
</details>

<details><summary><b>Plotly<b></summary>
<p>
[<b>Plotly & Cufflinks<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/6_Plotly%20&%20Cufflinks%20-%20Data%20Visualization/1_Plotly%20and%20Cufflinks.html#Plotly-and-Cufflinks) 
</p>
</details>
<b>*

<details><summary><b>Data Scientist ND<b></summary>
<p>
<h4>1. Uni-Variate Visualization:
> [<b>Bar<b> Chart](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/1_Bar%20Chart.html#Bar-Chart) 
[<b>Pie<b> Chart](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/2_Pie%20Chart.html#Pie-Chart) 
[<b>Histograms<b> Using Matplotlib](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/3_Histograms.html#Histograms-Using-Matplotlib) 
[<b>Kernal Density Estimation (KDE)<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2003_Univariate%20Exploration%20of%20Data/16.%20Extra%20Kernel%20Density%20Estimation.html) 
[<b>Waffle<b> Plots](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2003_Univariate%20Exploration%20of%20Data/17.%20Extra%20Waffle%20Plots.html) 

<h4>2. Bi-Variate Visualization:
> [<b>Scatter<b> Plot.](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/1_Scatter%20Plot.html#Scatter-Plot-using-Matplotlib) 
[<b>Heat Map<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/2_HeatMap.html#Heat-Map-using-Matplotlib) 
>> - A zoomed-in heatmap for best features have best correlation with the output.

> [<b>Violin<b> Plot](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/3_Violin%20Plot.html#Violin-Plot-using-Seaborn) 
[<b>Box<b> Plot](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/4_Box%20Plot.html#Box-Plot-vs.-Violin-Plot) 
[<b>Clustered Bar<b> Chart](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/5_Clustered%20Bar%20Chart.html#Clustered-Bar-+-Heatmap) 
[<b>Facet Grid<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/6_Facet%20Grid.html#Faced-Grid) 
[<b>Sweet Pair Grid<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Pairs-Plot) 
[<b>Adapted Bar<b> Chart,  <b>Point<b> Chart](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/7_Adapted%20Bar%20Chart.html#Adapted-Bar-Chart) 
[<b>Q-Q<b> Plot: Used to check normal distribution.](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/16.%20Extra%20Q-Q%20Plots.html) 
[<b>Swarm<b> Plot](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/17.%20Extra%20Swarm%20Plots.html) 
[<b>Rug<b> and <b>Strip<b> Plot](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/18.%20Extra%20Rug%20and%20Strip%20Plots.html) 
[<b>Stacked<b> Plots](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/19.%20Extra%20Stacked%20Plots.html) 
[<b>Ridgeline<b> Plot](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/20.%20Extra%20Ridgeline%20Plots.html) 


<h4>3. Multi-Variate Visualization:
> [<b>Shape<b>, <b>Size<b>, and <b>Color<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/1_Shape-Size-Color.html#1.-Shape) 
[<b>Facet 2d<b> Chart](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/2_Facet%202d.html#Faceting-in-col) 
[<b>Adaption Bi-variante<b> Charts](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/3_Adaption%20of%20Bivariate.html#Adaption-of-Bi-Variate-Plots) 
[<b>Plot Metrices<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/4_Plot%20Matices.html#Pair-Grid) 
</p>
</details>

<b>*
<details><summary><b>Time-Series Analysis Course<b></summary>
<p>

<details><summary><b>Time-Series with Pandas<b></summary>
<p>

- [<b>1. Datetime Index<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/00-Datetime-Index.html#Python-Datetime-Review) 

- [<b>2. Making Datetime as index and parse it as datetime64<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/01-Time-Resampling.html#Import-the-data) 

- [<b>3. Resample<b> (making aggregation over time)](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/01-Time-Resampling.html#resample())

- [<b>4. Time Shifting<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/02-Time-Shifting.html#Time-Shifting) 

- [<b>5. Rolling & Expanding<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/03-Rolling-and-Expanding.html#Rolling-and-Expanding)

- [<b>6. Visualizing Time-Series Data<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/04-Visualizing-Time-Series-Data.html#Visualizing-Time-Series-Data) 

- [<b>From month as number to String<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/06-Pandas-Time-Series-Exercises-SET-ONE-Solutions.html) 

- [<b>Extensive Time-Series EDA<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/08-Time-Series-with-Pandas-Project-Exercise-SET-TWO-Solutions.html) 
</p>
</details>

<details><summary><b>Statsmodel for Time-Series Analysis<b></summary> 
<p>

- [<b>1. Hodrick-Prescott filter<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/00-Introduction-to-Statsmodels.html) 

- [<b>2. ETS Decomposition<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/01-ETS-Decomposition.html) 

- [<b>3. EWMA (Exponantially Weighted Moving Average)<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/02-EWMA-Exponentially-Weighted-Moving-Average.html) 

- [<b>4. Holt-Winters Smoothing (Simple, Double, Triple)<b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/03-Holt-Winters-Methods.html#Holt-Winters-Methods) 
</p>
</details>

</p>
</details>