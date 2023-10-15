# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.projects_project_id_experiments.post import Create
from humanloop.paths.experiments_experiment_id.delete import Delete
from humanloop.paths.projects_project_id_experiments.get import List
from humanloop.paths.experiments_experiment_id_model_config.get import Sample
from humanloop.paths.experiments_experiment_id.patch import Update


class ExperimentsApi(
    Create,
    Delete,
    List,
    Sample,
    Update,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
