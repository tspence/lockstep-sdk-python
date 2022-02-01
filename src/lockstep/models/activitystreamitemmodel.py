#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class ActivityStreamItemModel:
    """
    Represents an item belonging to the activity stream.
    """

    objectKey: str = None
    activityStreamType: str = None
    textValue: str = None
    created: str = None
    createdUserId: str = None
    groupKey: str = None
    fromEmailAddress: str = None
    toEmailAddress: str = None
    fromContactName: str = None
    toContactName: str = None

