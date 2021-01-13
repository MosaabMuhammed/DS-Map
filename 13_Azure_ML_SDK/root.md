# Azure ML SDK

<div style="width:1000px;margin:auto">
<details><summary><b>Install</b></summary>
<pre><code class="python language-python">!pip install --upgrade "azureml-sdk[notebooks,azureml-widgets,automl,explain]"

import azure.core
print(f"azure version {azure.core.VERSION}")
</code></pre>
</details></details>

<details><summary><b>Running an Experiment</b></summary><ul>
<li><details><summary><b>Connecting to Your Workspace</b></summary>
This is based on a json file in your configuration, where you save your subscription details.
<pre><code class="python language-python">from azureml.core import Workspace

ws = Workspace.from_config()
print(ws.name, "Workspace loaded")
</code></pre>
</details></li>
<li><details><summary><b>Running an Experiment & Viewing Results</b></summary>
<pre><code class="python language-python"># Create an Azure ML experiment in your workspace.
experiment = Experiment(workspace=ws, name="diabetes-experiment")

# Start logging data from the experiment.
run = experiment.start_logging()
print("Starting epxeriment:", experiment.name)
</code></pre>
</details></details></li>
</ul></details></details>
</div>