# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.projects.post import Create
from humanloop.paths.projects_id_feedback_types.post import CreateFeedbackType
from humanloop.paths.projects_id_active_config.delete import DeactivateConfig
from humanloop.paths.projects_id_active_experiment.delete import DeactivateExperiment
from humanloop.paths.projects_project_id_deployed_config_environment_id.delete import DeleteDeployedConfig
from humanloop.paths.projects_project_id_deploy_config.patch import DeployConfig
from humanloop.paths.projects_id_export.post import Export
from humanloop.paths.projects_id.get import Get
from humanloop.paths.projects_id_active_config.get import GetActiveConfig
from humanloop.paths.projects.get import List
from humanloop.paths.projects_id_configs.get import ListConfigs
from humanloop.paths.projects_id_deployed_configs.get import ListDeployedConfigs
from humanloop.paths.projects_id.patch import Update
from humanloop.paths.projects_id_feedback_types.patch import UpdateFeedbackTypes


class ProjectsApi(
    Create,
    CreateFeedbackType,
    DeactivateConfig,
    DeactivateExperiment,
    DeleteDeployedConfig,
    DeployConfig,
    Export,
    Get,
    GetActiveConfig,
    List,
    ListConfigs,
    ListDeployedConfigs,
    Update,
    UpdateFeedbackTypes,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
