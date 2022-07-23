<h1 style='color:darkcyan;text-decoration:underline'>Unit</h1>
<div style='width:1000px;margin:auto'>

<details><summary><b>unittest</b></summary>
to run: python -m pytest
<details><summary>assertIsInstance</summary>
<pre><code></code></pre>import unittest

class TestNERClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
</details>

<br></details>

<details><summary><b>pytest</b></summary>

</details>
</div>
































