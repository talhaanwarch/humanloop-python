# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.projects.post import CreateRaw
from humanloop.paths.projects_id_feedback_types.post import CreateFeedbackTypeRaw
from humanloop.paths.projects_id_active_config.delete import DeactivateConfigRaw
from humanloop.paths.projects_id_active_experiment.delete import DeactivateExperimentRaw
from humanloop.paths.projects_id.delete import DeleteRaw
from humanloop.paths.projects_project_id_deployed_config_environment_id.delete import DeleteDeployedConfigRaw
from humanloop.paths.projects_project_id_deploy_config.patch import DeployConfigRaw
from humanloop.paths.projects_id_export.post import ExportRaw
from humanloop.paths.projects_id.get import GetRaw
from humanloop.paths.projects_id_active_config.get import GetActiveConfigRaw
from humanloop.paths.projects.get import ListRaw
from humanloop.paths.projects_id_configs.get import ListConfigsRaw
from humanloop.paths.projects_id_deployed_configs.get import ListDeployedConfigsRaw
from humanloop.paths.projects_id.patch import UpdateRaw
from humanloop.paths.projects_id_feedback_types.patch import UpdateFeedbackTypesRaw


class ProjectsApiRaw(
    CreateRaw,
    CreateFeedbackTypeRaw,
    DeactivateConfigRaw,
    DeactivateExperimentRaw,
    DeleteRaw,
    DeleteDeployedConfigRaw,
    DeployConfigRaw,
    ExportRaw,
    GetRaw,
    GetActiveConfigRaw,
    ListRaw,
    ListConfigsRaw,
    ListDeployedConfigsRaw,
    UpdateRaw,
    UpdateFeedbackTypesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass