from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class StatisticsCalc(TethysAppBase):
    """
    Tethys app class for Statistics Calculator.
    """

    name = 'Hydrostats App'
    index = 'home'
    icon = 'statistics_calc/images/icon.gif'
    package = 'statistics_calc'
    root_url = 'statistics-calc'
    color = '#158329'
    description = 'Calculates both hydrologic and forecast skill between simulated ond observed streamflow data. ' \
                  'Also contains tools for preprocessing data and visualizing data.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    controller_modules = ['controllers', 'api']

    def custom_settings(self):
        return (
            CustomSetting(
                name='api_source',
                type=CustomSetting.TYPE_STRING,
                description='Tethys portal where Streamflow Prediction Tool is installed (e.g. '
                            'https://tethys.byu.edu). Note: No trailing slash!',
                required=True
            ),
            CustomSetting(
                name='spt_token',
                type=CustomSetting.TYPE_STRING,
                description='Unique token to access data from the Streamflow Prediction Tool (API Key from the Portal)',
                required=True
            ),
        )
