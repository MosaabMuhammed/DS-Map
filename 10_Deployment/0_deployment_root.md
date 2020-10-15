<h1>Deployment</h1>

<div style="width:1000px;margin:auto">
<details><summary style='font-size:20px;font-weight:bold'>Make it Reproducable</summary></p><ul>
<li>Always remember to <b>set the SEED</b> for all environments.</li>
<li>Make sure <b>Dataset is Consistant</b> through the whole pipeline.</li>
<li>Record order of features, applied feature transformations, hyperparamters, ....</li>
</ul></p></details>
<details><summary style='font-size:20px;font-weight:bold'>Research Environment</summary></p><ul>
<li><a style="font-weight:bold"  href="./1_research_environment/02.6_ML_Pipeline_Step1-DataAnalysis.html">Data Analysis</a></li>
<li><a style="font-weight:bold"  href="./1_research_environment/02.7_ML_Pipeline_Step2-FeatureEngineering.html">Feature Engineering</a></li>
<li><a style="font-weight:bold"  href="./1_research_environment/02.8_ML_Pipeline_Step3-FeatureSelection.html">Feature Selection</a></li>
<li><a style="font-weight:bold"  href="./1_research_environment/02.9_ML_Pipeline_Step4-MachineLearningModelBuild.html">ML Building</a></li>
<li><a style="font-weight:bold"  href="./1_research_environment/02.10_ML_Pipeline-WrapUp_for_Deployment.html">Wrap up for Deployment</a></li>
</ul></p></details>

<details><summary style='font-size:20px;font-weight:bold'>Create Depolyment Environment</summary></p><ul>

<details><summary>Create Virtual Environment</summary>
inside your project, write the following:<br>
<pre><code># Create env
python -m venv &lt;name-of-env&gt;

# Activate it.
source &lt;name-of-env&gt;/bin/activate

# Install packages.
pip install ...

# Deactivate.
deactivate
</code></pre>
</details>

<details><summary>Create Requirment file</summary>
<pre><code># Create the file.
touch requirements.txt
# Then add packages manually.

# Add them automatically.
pip freeze &gt; requirements.txt

# Install libraries in requirments file.
pip install -r requirements.txt 
</code></pre>
</details>

<details><summary>Python Convetions</summary>
<pre><code># Type Hints.
import typing as t

def add_two_integers(first: int, second: t.Optional[int]=None) -&gt; int:
    """Sum two numbers"""
    result = first
    if second is not None:
        result = first + second
    return result
</code></pre>

<pre><code># Forcing Key Word Arguments (kwargs).
def my_function(*, foo):
    pass

# When calling this funciton, we have to name foo:
my_function(foo="bar")
</code></pre>
</details>
<details><summary>Add your ML pipeline</summary>
Make sure to follow the commit from this <a href="https://github.com/MosaabMuhammed/deploying-machine-learning-models/tree/53bc67c6a94e01f3fdaf05cbfa2b49465a0c7a1f">link</a> and make sure to make them 2 folders together with the same name.
<pre><code># Add your pipeline package to PYTHONPATH
$ export PYTHONPATH="$PYTHONPATH:path/to/your/pipeline/first_package_folder_name/"
</code></pre>
</details>

</ul></p></details>
</div>