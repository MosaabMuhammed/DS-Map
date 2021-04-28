<h1 id="4exploratorydataanalysiseda">4. Exploratory Data Analysis (EDA)</h1>

<div style='width:1000px;margin:auto'>
<details><summary><b>Tips & Tricks</b></summary>

<details><summary>Multiple ways to get <b>Correlation of Continous Features with target</b> </summary>

<details><summary><b>Generate a colored table for correlation</b></summary>
<pre><code>#Features correlation
corr = train[continous_cols+['target']].corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
</code></pre>
<p><img src="imgs/20210428-225608.png" alt="" /></p>
</details>

<details><summary> <b>Better Correlation heatmap</b></summary>
<pre><code class="python language-python">def heatmap(x, y, **kwargs):
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
        &lt;b&gt;kwargs_pass_on
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
    if color_min &lt; color_max:
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
</code></pre>

</details>

<details><summary> <b>Correlation of Continous Features with target</b> pd.corrwith() </summary>
<pre><code># Thanks a lot @dwin183287 for sharing this amazinf function!
background_color = "#f6f5f5"

fig = plt.figure(figsize=(12, 8), facecolor=background_color)
gs = fig.add_gridspec(1, 1)
ax0 = fig.add_subplot(gs[0, 0])

ax0.set_facecolor(background_color)
ax0.text(-1.1, 0.26, 'Correlation of Continuous Features with Target', fontsize=20, fontweight='bold', fontfamily='serif')
ax0.text(-1.1, 0.24, 'There is no features that pass 0.22 correlation with target', fontsize=13, fontweight='light', fontfamily='serif')

chart_df = pd.DataFrame(train_df[numerical_columns].corrwith(train_df['target']))
chart_df.columns = ['corr']
sns.barplot(x=chart_df.index, y=chart_df['corr'], ax=ax0, color=primary_blue, zorder=3, edgecolor='black', linewidth=1.5)
ax0.grid(which='major', axis='y', zorder=0, color='gray', linestyle=':', dashes=(1,5))
ax0.set_ylabel('')

for s in ["top","right", 'left']:
    ax0.spines[s].set_visible(False)

plt.show()
</code></pre>
<img src="./imgs/20210423-165108.png">
</details>

</details>

<details><summary> <b>Dark Mode</b></summary>
<a href="./5_eda/EDA dark mode.html">dark mode notebook</a>
</details>

<details><summary>How to make <b>beautiful Visualizations</b></summary>
<a href="./5_eda/how to make clean visualizations.html">Notebook</a>
</details>

<details><summary>Reduce  <b>the labels </b> in any axis plot</summary>
<pre>
<code># count different values/levels
cat10_freq = df_train.cat10.value_counts()
print(cat10_freq)

# and plot frequency distribution using log scale
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(np.log10(cat10_freq))
ax.xaxis.set_major_locator(plt.MaxNLocator(20)) # reduce number of x-axis labels
plt.title('cat10 - Frequencies')
plt.ylabel('log10(Frequency)')
plt.grid()
plt.show()
</code>
</pre>
</details>

<details><summary>Plot a <b>Sparse</b> Matrix</summary><pre><code>fig = plt.figure()
plt.spy(A, markersize=0.10, aspect = 'auto')
fig.set_size_inches(8,6)
fig.savefig('doc_term_matrix.png', dpi=800)
</code></pre>
</details>

<details><summary><b>top & left ticks</b> in correlation matrix</summary><pre><code>f = plt.figure(figsize=(19, 15))
corrmat = train_features.corr()
plt.matshow(corrmat, fignum=f.number)
plt.xticks(range(train_features.shape[1]), train_features.columns, fontsize=3, rotation=50)
plt.yticks(range(train_features.shape[1]), train_features.columns, fontsize=3)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
</code></pre>
</details>

<details><summary>Draw an <b>Arrow and Text</b> on the figure</summary><pre><code>plt.annotate('Stationary Activities', xy=(-0.956, 17), xytext=(-0.9, 23), size=20, 
             va='center', ha='left', arrowprops=dict(arrowstyle='simple',
                                                     connectionstyle='arc3, rad=0.1'))
</code></pre>
</details>

<details><summary><b>Date Formatter</b> when plotting date feature</summary><pre><code>fig, ax = plt.subplots(figsize=(20, 10));
fig = sns.countplot(df.timestamp, ax=ax, edgecolor='k', hue=df.label);
X_dates = df['timestamp'].dt.strftime('%I:%M').sort_values().unique();
ax.xaxis.set_major_formatter(plt.FixedFormatter(X_dates));
plt.title('How many records per minute?', y=1.05);
plt.grid();
plt.xticks(rotation=70);
</code></pre>
</details>

<details><summary>Make <b>ylabel</b> Horizontal</summary>
<pre><code class="python language-python">plt.ylabel('Count', rotation=0, labelpad=30)
</code></pre>

</details>

<details><summary>Using <b>[xkcd]</b> Drawing plotting Style</summary><pre><code class="python language-python">with plt.xkcd():
    plt.plot(roc_curve[0], roc_curve[1]);
    plt.plot([0,1], [0,1])
    plt.xlabel('FPR'); plt.ylabel('TPR'); plt.title('test AUC = %f' % (auc)); plt.axis([-0.05,1.05,-0.05,1.05]);
</code></pre>
</details>

<details><summary><b>CDF</b> Plotting</summary>
<pre><code class="python language-python">df['height'].plot.hist(bins=200,
                 range=(50, 80),
                 alpha=.3,
                 color='red',
                 cumulative=True,
                 normed=True)
</code></pre>

</details>

<details><summary><b>Greatter Matrix by mean</b> for <b>Feature Engineering</b></summary>

<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/0_My%20work/5_SpringLeaf%20Competition/EDA_Springleaf_screencast.html#Go-through"><b>Notebook</b></a> <pre><code class="python language-python">def autolabel(arrayA):
    '''
    label each colored square with the corresponding data value.
    If value &gt; 20, the text is in black, else in white.
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
            mask = (~df[c1].isnull()) &amp; (~df[c2].isnull())
            if i&gt;=j:
                b.append((df.loc[mask,c1].values&gt;=df.loc[mask,c2].values).mean())
            else:
                b.append((df.loc[mask,c1].values&gt;df.loc[mask,c2].values).mean())

        a.append(b)

    plt.figure(figsize = (sz,sz))
    plt.imshow(a, interpolation = 'None', cmap='Spectral')
    _ = plt.xticks(range(len(feats)),feats,rotation = 90)
    _ = plt.yticks(range(len(feats)),feats,rotation = 0)
    autolabel(a)
</code></pre>

</details>


<details><summary> <b>Distrubtion of feature vs. row index</b></summary>

<a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&amp;%20Visualization.html#Distribution-of-X8-along-with-row-index:"><b>Example</b></a>  

<h4> 1. Without Class labeling</h4><pre><code class="python language-python">plt.figure(figsize=(16, 10))
plt.plot(train.x8, '.')
plt.xlabel('Row Index')
plt.ylabel('X8 Values')
plt.title('Distribution of X8 around row index')
</code></pre>

<h4> 2. With class labeling</h4>
<a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&amp;%20Visualization.html#Hue-with-Class-labels:"><b>Labeling example</b></a><pre><code class="python language-python">plt.figure(figsize=(16, 10))
plt.scatter(range(len(train.x8)), train.sort_values('y')['x8'], c=train.sort_values('y')['y'], cmap='viridis')
</code></pre>

</details>

<details><summary> <b>Features Grouping</b> for <b>Feature Engineering</b></summary>

<h4> 1. Clustering by KMeans</h4>
<a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&amp;%20Visualization.html#With-Clustering:"><b>Notebook</b></a><pre><code class="python language-python">from sklearn.cluster import KMeans

X = train.copy()

y = X['y']
X = X.drop('y', axis=1)

X = X.fillna(-999)

for col in train.columns[train.dtypes == 'object']:
    X[col] = X[col].factorize()[0]


kmeans = KMeans(n_clusters=7)
y_pred = kmeans.fit_predict(X)
</code></pre>
<pre><code class="python language-python">plt.figure(figsize=(16, 10))
sns.heatmap(X.corr(), cmap='viridis');
</code></pre>

<h4> 2. Clustering by Statistics</h4>
<a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&amp;%20Visualization.html#Clustering-Using-Statistics:"><b>Notebook</b></a>
<pre><code class="python language-python">plt.figure(figsize=(16, 8))
train.mean().sort_values().plot(style='.');
</code></pre>

</details>


<details><summary>From <b>Power Law Dist</b> to <b>Normal Disb.</b></summary>


<h4> Convert</h4><pre><code class="python language-python">#converting the values to log-values to chec for log-normal
import math
frame_with_durations_modified['log_times']=[math.log(i+1) for i in frame_with_durations_modified['trip_times'].values]
</code></pre>

<h4> Show the distribution</h4><pre><code class="python language-python">#pdf of log-values
sns.FacetGrid(frame_with_durations_modified,size=6) \
      .map(sns.kdeplot,"log_times") \
      .add_legend();
plt.show();
</code></pre>

<h4> Check the Q-Q plot.</h4><pre><code class="python language-python">import scipy
#Q-Q plot for checking if trip-times is log-normal
scipy.stats.probplot(frame_with_durations_modified['log_times'].values, plot=plt)
plt.show()
</code></pre>

</details>

<details><summary>Plot <b>Two Categorical Features</b> with sizes</summary>
<pre><code class="python language-python">def plot_categoricals(x, y, data, annotate=True):
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
</code></pre>

<h4> 2. Example.</h4><pre><code class="python language-python">plot_categoricals('rez_esc', 'Target', data)
</code></pre>

</details>


<details><summary>Plot <b>How many Unique Values</b> In each column</summary>
<pre><code class="python language-python">color = sns.color_palette()[0]
ax = train.select_dtypes(np.int64)\
     .nunique()\
     .value_counts()\
     .sort_index()\
     .plot.bar(color=color, figsize=(8, 6), edgecolor='black', linewidth=2)
show_annotation(ax)
</code></pre>

</details>

<details><summary>Plot <b>Quantiles</b> on line chart</summary>

<img src="imgs/20191030-123738.png" width="1000" height='500' /><pre><code class="python language-python">plt.plot(tag_counts[:100], c='b')
plt.scatter(x=list(range(0, 100, 5)), y=tag_counts[0:100:5], c='orange', label='Quantiles with .05 intervals.')
plt.scatter(x=list(range(0,100,25)), y=tag_counts[0:100:25], c='m', label='Quantiles with .25 intevals.')

for x, y in zip(list(range(0, 100, 25)), tag_counts[0:100:25]):
    plt.annotate(s="{}, {})".format(x, y), xy=(x, y), xytext=(x-.05, y+500))
</code></pre>

</details>

<details><summary><b>Histogram</b> For all Numerical Values</summary>
<pre><code class="python language-python">train_df.hist(bins='auto', figsize=(18, 22), layout=(5, 2));
</code></pre>

</details>

<details><summary> Add <b>Spaces</b> b/w <b>height</b> and <b>width</b> for subplots</summary>
<pre><code class="python language-python">plt.subplots_adjust(wspace=.5, hspace=.5)
</code></pre>

</details>

<details><summary> Plot <b>3D</b> figures </summary>
<p style="margin: 0"><pre><code class="python language-python">from mpl_toolkits.mplot3d import Axes3D
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
</code></pre>

</details>


<details><summary> Show <b>Annotations</b> on <b>bar chart [Horizontal, Vertical]</b> </summary>
<h4> Vertical Bar</h4><pre><code class="python language-python">def show_annotation(dist, n=5, total=None):
    sizes = [] # Get highest value in y
    for p in dist.patches:
        height = p.get_height()
        sizes.append(height)

        dist.text(p.get_x()+p.get_width()/2.,          # At the center of each bar. (x-axis)
               height+n,                            # Set the (y-axis)
               '{:1.2f}%'.format(height*100/total) if total else '{}'.format(height), # Set the text to be written
               ha='center', fontsize=14) 
    dist.set_ylim(0, max(sizes) * 1.15); # set y limit based on highest heights
</code></pre>
<h4> Example:</h4><pre><code class="python language-python">total = len(train)
plt.figure(figsize=(12, 6))

color = sns.color_palette()[0]
g = sns.countplot(x='target', data=train, color=color)
g.set_title('Target Distribution', fontsize=20)
g.set_xlabel('Target Values', fontsize=15)
g.set_ylabel('Count', fontsize=15)

show_annotation(g)
</code></pre>

<h4> Horizontal Bar</h4><pre><code>def show_annotations_horizontal(ax):
    sizes = []
    for p in ax.patches:
        width = p.get_width()
        sizes.append(width)
        percentage = f'{width:.2f}'
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        ax.annotate(percentage, (x, y))
        ax.set_xlim(0, max(sizes) * 1.15); # set x limit based on highest width
</code></pre>

</details>

<details><summary> <b>Increase Size of (plt.title)</b> </summary>

<pre><code class="python language-python">plt.title('Title here', size=20, y=1.06)
</code></pre><pre><code class="python language-python">plt.suptitle('Title here', fontsize=20)
</code></pre>

<h4> OOP Version</h4><pre><code class="python language-python">color = sns.color_palette()[0]
g = sns.countplot(x='target', data=train, color=color)
g.set_title('Target Distribution', fontsize=20)
g.set_xlabel('Target Values', fontsize=15)
g.set_ylabel('Count', fontsize=15)
</code></pre>

</details>

<details><summary> <b>Change Font Size of all plots</b> </summary>

<pre><code class="python language-python">plt.rcParams['font.size'] = 22
</code></pre>

</details>



<details><summary> <b>Color the edge of bar chart</b> </summary>
<pre><code class="python language-python">(app_train['DAYS_BIRTH']/-365).plot.hist(edgecolor='k', bins=30);
</code></pre><pre><code class="python language-python">plt.rcParams['font.size'] = 18
plt.rcParams['patch.edgecolor'] = 'k'
</code></pre>

</details>

<details><summary> Make <b>grid behind bar charts</b> </summary>

<pre><code class="python language-python">ax.grid(zorder=0)
ax.bar(range(len(y)), y, width=0.3, align='center', color='skyblue', zorder=3)
</code></pre>

</details>

<details><summary><b>KDE</b> plot b/w <b>feature</b> and <b>TARGET</b></summary>
<pre><code class="python language-python"># Modify it to be sutable for your needs.
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

    print('~&gt; The correlation between %s and the TARGET is %.4f' % (var_name, corr))
    print('~&gt; The median value for loan that was not repaid = %.4f' % avg_not_repaid)
    print('~&gt; The median value for loan that was repaid = %.4f' % avg_repaid)
</code></pre>
</details>

<details><summary>Show the <b>Legend</b> outside of the plot</summary>
<pre><code class="python language-python"># To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Note:
# ncol=1 (default) is another parameter, you can tweak to change the number of columns to fill in a raw in the legend.
</code></pre>
</details>
<details><summary>Add <b>Vertical</b> or <b>Horizontal</b> line in a plot</summary><pre><code># Vertical Line.
plt.axvline(x=np.mean(df.weight), color="red", label="mean")

# Horizontal Line.
plt.axhline(y=.5, color="red", label="something")
</code></pre>
</details>

</details>

<hr>

<details><summary><b>Pandas</b></summary><ul>
<li><b>df.plot.hist()</b>     histogram</li>

<li><b>df.plot.bar()</b>      bar chart</li>

<li><b>df.plot.barh()</b>     horizontal bar chart</li>

<li><b>df.plot.line()</b>     line chart</li>

<li><b>df.plot.area()</b>     area chart</li>

<li><b>df.plot.scatter()</b>  scatter plot</li>

<li><b>df.plot.box()</b>      box plot</li>

<li><b>df.plot.kde()</b>      kde plot</li>

<li><b>df.plot.hexbin()</b>   hexagonal bin plot</li>

<li><b>df.plot.pie()</b>      pie chart</li>
</ul>

<a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/03-Pandas-Visualization/00-Pandas%20Built-in%20Data%20Visualization.html#Plot-Types"><b>Built-in Visualization</b></a> 
</details>

<details><summary><b>Matplotlib</b></summary><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/3_Matplotlib%20/1_Matplotlib%20Concepts%20Lecture.html#Matplotlib-Overview-Lecture"><b>1. Matplotlib Concepts</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/3_Matplotlib%20/2_Advanced%20Matplotlib%20Concepts.html#Advanced-Matplotlib-Concepts-Lecture"><b>2. Advanced Concepts</b></a></li>
</ul>


</details>

<details><summary><b>Seaborn</b></summary><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/1_Distribution%20Plots.html#Distribution-Plots"><b>1. Distrubtion Plots</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/2_Categorical%20Plots.html#Categorical-Data-Plots"><b>2. Categorical Data Plots</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/3_Matrix%20Plots.html#Matrix-Plots"><b>3. Matrix Plots</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/4_Regression%20Plots.html#Regression-Plots"><b>4. Regression Plots</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/5_Grids.html#Grids"><b>5. Grids</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/4_Seaborn%20/6_Style%20and%20Color.html#Style-and-Color"><b>6. Styles &amp; Coloring</b></a></li>


</ul>


</details>

<details><summary><b>Plotly</b></summary><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/6_Plotly%20&amp;%20Cufflinks%20-%20Data%20Visualization/1_Plotly%20and%20Cufflinks.html#Plotly-and-Cufflinks"><b>Plotly &amp; Cufflinks</b></a> </li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/10_Plotly_tutorials/Notebook.html#INTRODUCTION"><b>Plotly Tutorials</b></a> </li> 

<li><details><summary><b>Scatter plot</b> - Plotly Express</summary><pre><code>import plotly.express as px

# Create a scatter plot.
fig = px.scatter(data, x='gdp', y='co2', animation_frame='year', animation_group='country', color='region', hover_name='country', facet_col='region', width=1579, height=400, log_x=True, size_max=45, range_x=[xmin, xmax], range_y=[ymin, ymax])

fig.show()
</code></pre>
</details></li>
<li><details><summary><b>Geographic</b> - Code 3 Alpha</summary><pre><code>import plotly.express as px
fig = px.choropleth(internet_usage_2016,
                    locations="Code",
                    color="Individuals using the Internet (% of population)",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.update_layout(
    title_text="Internet Usage across the world (% population) - 2016",
    # geo_scope='africa'
    geo = dict(projection={'type': 'natural earth'})
)
fig.show()
</code></pre>
</details></li>
<li><details><summary><b>Geographic</b> - Lat & Lon - Scatter</summary><pre><code>import plotly.graph_objects as go

fig = go.Figure(data=go.Scattergeo(
                 lon=df['LON'],
                 lat=df['LAT'],
                 text=df['street_addr'], # Value to be displied when hovering
                 mode='markers',
                 ))
fig.update_layout(title='Walmart stores across world',
                geo_scope='usa')
fig.show()
</code></pre>
</details></li>
</ul></details>

<details><summary><b>Bokeh</b></summary><ul>
There are files inside eda_file, wait until you read the book about bokeh, then start documenting.
</ul></details>

<details><summary><b>Altair</b></summary><ul>
<li><a href="./5_eda/01-alt-Iris-Demo.html"><b>IRIS Demo</b></a> </li>
<li><a href="./5_eda/01-Cars-Demo.html"><b>Car Demo</b></a> </li>
<li><a href="./5_eda/02-Simple-Charts.html"><b></b>Simple Charts</a> </li>
<li><a href="./5_eda/03-Binning-and-aggregation.html"><b>Binning & Aggregation</b></a> </li>
<li><a href="./5_eda/04-Compound-charts.html"><b>Compound Charts</b></a> </li>
<li><a href="./5_eda/06-Selections.html"><b>Selections</b></a> </li>
<li><a href="./5_eda/07-Transformations.html"><b>Transformations</b></a> </li>
<li><a href="./5_eda/08-Configuration.html"><b>Configuration</b></a> </li>
<li><a href="./5_eda/09-Geographic-plots.html"><b>Geographic Plots</b></a> </li>
</ul></details>
<hr>

<details><summary><b>Data Scientist ND</b></summary>

<h4>1. Uni-Variate Visualization:</h4> 

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/1_Bar%20Chart.html#Bar-Chart"><b>Bar</b> Chart</a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/2_Pie%20Chart.html#Pie-Chart"><b>Pie</b> Chart</a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/1_Univariate%20Visualization/3_Histograms.html#Histograms-Using-Matplotlib"><b>Histograms</b> Using Matplotlib</a> </li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2003_Univariate%20Exploration%20of%20Data/16.%20Extra%20Kernel%20Density%20Estimation.html"><b>Kernal Density Estimation (KDE)</b></a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2003_Univariate%20Exploration%20of%20Data/17.%20Extra%20Waffle%20Plots.html"><b>Waffle</b> Plots</a> </li>
</ul>

<h4>2. Bi-Variate Visualization:</h4>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/1_Scatter%20Plot.html#Scatter-Plot-using-Matplotlib"><b>Scatter</b> Plot.</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/2_HeatMap.html#Heat-Map-using-Matplotlib"><b>Heat Map</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/3_Violin%20Plot.html#Violin-Plot-using-Seaborn"><b>Violin</b> Plot</a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/4_Box%20Plot.html#Box-Plot-vs.-Violin-Plot"><b>Box</b> Plot</a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/5_Clustered%20Bar%20Chart.html#Clustered-Bar-+-Heatmap"><b>Clustered Bar</b> Chart</a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/6_Facet%20Grid.html#Faced-Grid"><b>Facet Grid</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Pairs-Plot"><b>Sweet Pair Grid</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/2_Bivariate%20Visualization/7_Adapted%20Bar%20Chart.html#Adapted-Bar-Chart"><b>Adapted Bar</b> Chart,  <b>Point</b> Chart</a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/16.%20Extra%20Q-Q%20Plots.html"><b>Q-Q</b> Plot: Used to check normal distribution.</a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/17.%20Extra%20Swarm%20Plots.html"><b>Swarm</b> Plot</a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/18.%20Extra%20Rug%20and%20Strip%20Plots.html"><b>Rug</b> and <b>Strip</b> Plot</a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/19.%20Extra%20Stacked%20Plots.html"><b>Stacked</b> Plots</a></li>

<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2008-Module%2001-Lesson%2004_Bivariate%20Exploration%20of%20Data/20.%20Extra%20Ridgeline%20Plots.html"><b>Ridgeline</b> Plot</a></li>

<li><details><summary><b>catplot</b></summary><pre><code># Used as countplot for categorical feature with its count.
sns.catplot("cut", data=df, aspect=1.5, kind="count", color="b")
</code></pre>
</details></li>

<li><details><summary><b>lineplot</b></summary>
The solid line represent the mean of the y axis feature at the corresponding x coordinate.<br>The shaded area around the line plot shows the confidence interval for the y axis feature. (by default, seaborn set this to 95% confidence interval)<br><br>Line plots are great visualization techniques for scenarios where we have data that changes over time.<pre><code>ax = sns.lineplot(x="cat_col", y="num_col", data=df, ci=68)
</code></pre>
</details></li>

<li><details><summary><b>clustermap</b></summary>
We can can determine the similarity(distance) metrics by using (metric) parameter, and the possible values ["euclidean"(default), "manhattan", "correlation", ...]<pre><code>pd_pivoted = df.pivot("month", "year", "passenegers")

# We can cluster by "year" (row_cluster=False, col_cluster=True).
# We can cluster them by both "year" and "month".
# The following is clustered by "month".
ax = sns.clustermap(df_pivoted, col_cluster=False, row_cluster=True, metric="euclidean")
</code></pre>

Appling linkage in Heatmaps:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- If we define the distance b/w 2 clusters as the distance b/w the 2 points across the clusters <b>closest</b> to each other, the rule is called <b>single linkage</b>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;- If the rule is to define the distance b/w 2 clusters as the distance b/w the points <b>farthest</b> from each other, it is called <b>complete linkage</b>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;- If the rule is to define the distance as the <b>average</b> of all possible pairs of rows in the 2 clusters, it's called <b>average linkage</b>.<pre><code>sns.clustermap(df_pivoted, row_cluster=False, metric="correlation", method="single")
</code></pre>
</details></li>
</ul>

<h4>3. Multi-Variate Visualization:</h4>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/1_Shape-Size-Color.html#1.-Shape"><b>Shape</b>, <b>Size</b>, and <b>Color</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/2_Facet%202d.html#Faceting-in-col"><b>Facet 2d</b> Chart</a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/3_Adaption%20of%20Bivariate.html#Adaption-of-Bi-Variate-Plots"><b>Adaption Bi-variante</b> Charts</a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Scientist%20ND/html/3_Multivariate%20Visualization/4_Plot%20Matices.html#Pair-Grid"><b>Plot Metrices</b></a> </li>
</ul>
</details>

<hr>

<details><summary><b>NOTES</b></summary><ul>
<details><summary><b>KDE</b></summary>
The kernel density estimation (KDE) is a non-parametric way to estimate the probability density function of a random variable. Usually, a KDE doesn't tell us anything more than what we can infer from the histogram itself. However, it is
helpful when comparing multiple histograms on the same plot.
</details>

<details><summary><b>Histogram</b></summary>

<ul>Three observations are important in a histogram:
<li>Which feature values are more frequent in the dataset. you may log() the data in order to inspect better.</li>
<li>How many peaks exist in the data (the peaks need to be further inspected for possible causes in the context of the data).</li>
<li>Whether there are any outliers in the data</li>
<li>df.hist() & sns.distplot()</li></ul>
</details>
</ul></details>
</div>