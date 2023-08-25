"""
Auther: Ismail Shaikh(md.ismaaill@gmail.com)
"""


class Counter:
    """
    This module is used for counter, can store value will its maximum value.
    The loos _count can be set if the _count value need to go beyond the maximum value.
    """

    def __init__(self, name: str = "counter", max_count: int = 20, loose_type: bool = False,
                 enable_reverse_count: bool = False):
        """
        Initializing the Counter
        :param name: Name of this Counter
        :param max_count: Maximum till the Counter should counter, if Loose counter is enable this check is ignored.
        :param loose_type: Enable loose counter
        :param enable_reverse_count: Enable counter decrement.
        """
        self._counter_name = name
        self._loose_type = loose_type
        self._count: int = 0
        self._max_count = max_count
        self._enable_reverse = enable_reverse_count

    @property
    def count(self):
        """
        Return the total count value
        :return: Current counter value
        :rtype: int
        :raise None:
        """
        return self._count

    def increment(self):
        """
        This method is used to increment the counter value by 1.
        If counter is configured as loose counter it will count beyond the set maximum value.
        :return: None
        :raise None:
        """
        if self._loose_type:
            self._count += 1
        else:
            if self._count < self._max_count:
                self._count += 1

    def decrement(self):
        """
        This method is used to decrement the counter value by 1.
        Please Note: The counter value will not go beyond zero.
        :return: None
        :raise TypeError: When used this message without enabling the reverse count.
        """
        if not self.enable_reverse:
            raise TypeError("reverse counter is disabled")

        if not self._count <= 0:
            self._count -= 1

    @property
    def counter_name(self):
        """
        Returns name of the counter
        :return: Name of the counter
        :raise None:
        """
        return self._counter_name

    @counter_name.setter
    def counter_name(self, value):
        """Set counter name"""
        self._counter_name = value

    @property
    def loose_type(self):
        """
        Get loose counter status
        :return:
        """
        return self._loose_type

    @loose_type.setter
    def loose_type(self, enable: bool = False):
        """
        To set Loose counter. if this is set to True. The counter will go beyond set maximum value of counter.
        :param: enable: Set this to enable loose counter, defaults to False
        :type enable: bool
        :return: None
        :raise None:
        """
        if enable is None:
            raise enable
        self._loose_type = enable

    @property
    def max_count(self):
        """
        Get counter max limit
        :return: counter max limit
        :rtype int:
        """
        return self._max_count

    @max_count.setter
    def max_count(self, maximum_value: int = 10):
        """
        set maximum counter limit
        :param maximum_value: counter maximum limit, defaults 10
        :return: None
        :raise ValueError:
        """
        if maximum_value <= 0:
            raise ValueError("Maximum should be grater them 0")
        self._max_count = maximum_value

    @property
    def enable_reverse(self):
        """
        Check if the reverse counting is enabled or not
        :return: Status of reverse counter status
        :rtype int:
        """
        return self._enable_reverse

    @enable_reverse.setter
    def enable_reverse(self, val: bool = False):
        """
        This method is used to enable reverse count.

        :param val: Boolean value input, default is False
        :return: None
        :raise None:
        """
        self._enable_reverse = val

    def reset(self):
        """
        This method will resent the counter value to zero.
        :return: None
        :raise None:
        """
        self._count = 0

    def __str__(self):
        return (f"Counter Name: {self._counter_name}  "
                f"Counts: {self._count}  "
                f"Counter Maximum: {self._max_count}  "
                f"is Loos Count enabled? {self._loose_type}  "
                f"is Reverse Count Enabled? {self._enable_reverse} ")
