"""
Waffle flags for instructor dashboard.
"""

from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag, WaffleFlagNamespace

WAFFLE_NAMESPACE = 'instructor'

# Waffle flag enable new data download UI on specific course.
# .. toggle_name: instructor.enable_data_download_v2
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: instructor
# .. toggle_category: Instructor dashboard
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2020-07-8
# .. toggle_expiration_date: ??
# .. toggle_warnings: ??
# .. toggle_tickets: PROD-
# .. toggle_status: supported
DATA_DOWNLOAD_V2 = CourseWaffleFlag(
    waffle_namespace=WaffleFlagNamespace(name=WAFFLE_NAMESPACE, log_prefix='instructor_dashboard: '),
    flag_name='enable_data_download_v2',
    flag_undefined_default=False
)


def data_download_v2_is_enabled(course_key):
    """
    check if data download v2 is enabled.
    """
    return DATA_DOWNLOAD_V2.is_enabled(course_key)
