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

<details><summary>Add Tests</summary>
Make sure to follow the commit from this <a href="https://github.com/MosaabMuhammed/deploying-machine-learning-models/tree/53bc67c6a94e01f3fdaf05cbfa2b49465a0c7a1f">link</a>
<pre><code>
$ pytest packages/regression_model/tests -W ignore:DeprecationWarning
</code></pre>

<pre><code># Example of test function
import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset

def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_json = test_data[0:1].to_json(orient='records')

    # When
    subject = make_prediction(input_data=single_test_json)

    # Then
    assert subject is not None
    assert isinstance(subject.get("predictions")[0], float)
    assert math.ceil(subject.get("predictions")[0]) == 112476
</code></pre>
</details>

<details><summary>Add Emojis to your git commits [side-note]</summary>
Check <a href="https://gist.github.com/parmentf/035de27d6ed1dce0b36a">possible emojis</a>
<pre><code>https://gist.github.com/parmentf/035de27d6ed1dce0b36a

# First install emojify to allow emojis in the terminal.
$ sudo sh -c "curl https://raw.githubusercontent.com/mrowa44/emojify/master/emojify -o /usr/local/bin/emojify && chmod +x /usr/local/bin/emojify"

# Add commit
git commit -am ":tada: Initial Commit :tada:"

# Show emojis in the terminal
git log --oneline --color | emojify | less -r
git log | emojify
</code></pre>
</details>

<details><summary>Version</summary>
<pre><code>3.1.12
Major.Minor.Batch
</code></pre>
</details>

<details><summary>Package your code</summary>
Make sure to create the following files:<ul>
<li>MANIFEST.in: contains which files to be included in the package</li>
<li>requirements.txt</li>
<li>setup.py</li>
<li>README.md</li></ul>
<pre><code># Then write the following commands.
# This command to install the requirements.
pip install -r packages/regression_model/requirements.txt

# Then create the distribution & wheel.
python packages/regression_model/setup.py sdist bdist_wheel

# Then pip install your package locally, to see if working.
pip install -e packages/regression_model
</code></pre>
</details>

<details><summary>Startup Command on Azure</summary>
<pre><code>export INTENT_CLF_PACKAGE="/home/site/repository/packages/intent_clf"
export ML_API_PACKAGE="`/home/site/repository/packages/ml_api"
export PYTHONPATH="$PYTHONPATH:$ML_API_PACKAGE"
pip install -e $INTENT_CLF_PACKAGE
gunicorn -w 4 -k uvicorn.workers.UvicornWorker packages.ml_api.run:application --timeout 400
</code></pre>
</details>

</ul></p></details>

<details><summary style='font-size:20px;font-weight:bold'>Run Multiple cmds at the background</summary></p><ul>
Example, one command that you are using multi-processing workers to handle your backend, and another one to make the frontend server up and running.<br>
We are going to accomplish that with <b>supervisor</b> python package.
<h4>Local environment</h4>
<pre><code>
# This file is called "supervisord.local.conf"
# Change the pathes, and remove what is not needed.
[supervisord]
loglevel=info
logfile=/tmp/supervisord.log
#environment=data_storage="firestore",blob_storage="cloudstorage",blob_storage_bucket="blob_storage_bucket",GOOGLE_APPLICATION_CREDENTIALS="/vagrant/service_account.json"


[unix_http_server]
file=/tmp/supervisor.sock
# username=admin
# password=ndfu48f77husnmdf45bBSu89

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock

[program:be]
priority=300
stdout_logfile=/tmp/ingestbeout.log
stderr_logfile=/tmp/ingestbeerr.log
command=/home/vagrant/venv/bin/ingestiond --no_persistence --iproc_num 1 --oproc_num 2 --agg_cache_size 10
autostart=true
autorestart=true
stopwaitsecs = 60

[program:fe]
priority=200
stdout_logfile=/dev/stdout
stderr_logfile=/dev/stderr
command=/home/vagrant/venv/bin/gunicorn -b "0.0.0.0:8000" -w 1 -k uvicorn.workers.UvicornWorker ingest.frontend:app
autostart=true
autorestart=true
stopwaitsecs = 30

[program:web]
priority=200
stdout_logfile=/dev/stdout
stderr_logfile=/dev/stderr
command=/home/vagrant/venv/bin/gunicorn -b "0.0.0.0:8080" -w 1 "web.main:create_app()"
autostart=true
autorestart=true
stopwaitsecs = 30

[group:ingest]
programs=fe,be
</code></pre>


Commands to use:
<pre><code>
# Must run first command to refer to the supervisord.local.conf that you have configured.
supervisord -c supervisord.local.conf

# see them running by htop, type "t" to see the actual commands.
htop

# See the status of the running dieamans
supervisorctl -c supervisord.local.conf status

# Run the interactive model by supervisorctl
supervisorctl -c supervisord.local.conf
# ? -> see the available options.
# status all -> see the status of the commands.

# Stop the dieamon from running
supervisorctl -c supervisord.local.conf stop all

# Start running the dieamans
supervisorctl -c supervisord.local.conf start all

# Check the last 30 lines in the log.
tail -n 30 /tmp/ingestbeerr.log
</code></pre>
</ul></p></details>
</div>